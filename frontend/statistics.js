const API_URL = "http://127.0.0.1:8003";
let token = "";

let mostChart = null;
let leastChart = null;
let monthlyChart = null;

function setTodayDefaults(){
    const today = new Date().toISOString().split("T")[0];
    document.getElementById("most_end").value = today;
    document.getElementById("least_end").value = today;
}

async function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const res = await fetch(`${API_URL}/login`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({username, password})
    });

    const data = await res.json();

    if(res.ok){
        token = data.access_token;
        showToast("Login successful!", "success");
    }else{
        showToast(data.detail || "Login failed", "error");
    }
}

async function mostSold(){
    const start = document.getElementById("most_start").value;
    const end = document.getElementById("most_end").value;

    const res = await fetch(API_URL + "/most_items_sold?start_date=" + start + "&end_date=" + end, {
        method: "GET",
        headers: {"Authorization":"Bearer " + token}
    });

    const data = await res.json();

    if(data.detail && data.detail.toLowerCase().includes("token")){
        showToast("Invalid token. Please login.", "error");
        return;
    }

    const container = document.getElementById("most_result");
    container.innerHTML = "";

    const labels = [];
    const quantities = [];

    data.forEach(item=>{
        const div = document.createElement("div");
        div.textContent = "Food: " + item.food_name + " | Quantity: " + item.quantity + " | Revenue: " + item.revenue;
        container.appendChild(div);

        labels.push(item.food_name);
        quantities.push(item.quantity);
    });

    if(mostChart) mostChart.destroy();

    const ctx = document.getElementById("most_chart").getContext("2d");
    mostChart = new Chart(ctx,{
        type:"bar",
        data:{
            labels:labels,
            datasets:[{
                label:"Quantity Sold",
                data:quantities
            }]
        },
        options:{
            responsive:true,
            plugins:{legend:{display:true}}
        }
    });
}

async function leastSold(){
    const start = document.getElementById("least_start").value;
    const end = document.getElementById("least_end").value;

    const res = await fetch(API_URL + "/least_items_sold?start_date=" + start + "&end_date=" + end, {
        method: "GET",
        headers: {"Authorization":"Bearer " + token}
    });

    const data = await res.json();

    if(data.detail && data.detail.toLowerCase().includes("token")){
        showToast("Invalid token. Please login.", "error");
        return;
    }
    const container = document.getElementById("least_result");
    container.innerHTML = "";

    const labels = [];
    const quantities = [];

    data.forEach(item=>{
        const div = document.createElement("div");
        div.textContent = "Food: " + item.food_name + " | Quantity: " + item.quantity + " | Revenue: " + item.revenue;
        container.appendChild(div);

        labels.push(item.food_name);
        quantities.push(item.quantity);
    });

    if(leastChart) leastChart.destroy();

    const ctx = document.getElementById("least_chart").getContext("2d");
    leastChart = new Chart(ctx,{
        type:"bar",
        data:{
            labels:labels,
            datasets:[{
                label:"Quantity Sold",
                data:quantities
            }]
        },
        options:{
            responsive:true
        }
    });
}

async function monthlyData() {
    const dateInput = document.getElementById("monthPicker").value;

    if (!dateInput) {
       showToast("Please select a date.", "error");        return;
    }

    const [yearStr, monthStr] = dateInput.split("-");
    const year = parseInt(yearStr);
    const month = parseInt(monthStr) - 1;
    const res = await fetch(`${API_URL}/monthly_data?year=${year}&month=${month}`, {
        method: "GET",
        headers: { "Authorization": "Bearer " + token }
    });

    const data = await res.json();
    if(data.detail && data.detail.toLowerCase().includes("token")){
        showToast("Invalid token. Please login.", "error");
        return;
    }
    const container = document.getElementById("monthly_result");
    container.innerHTML = `
        <div>Total Revenue: ${data.total_revenue}</div>
        <div>Morning Revenue: ${data.morning}</div>
        <div>Noon Revenue: ${data.noon}</div>
        <div>Afternoon Revenue: ${data.afternoon}</div>
    `;

    if (monthlyChart) monthlyChart.destroy();

    const ctx = document.getElementById("monthly_chart").getContext("2d");
    monthlyChart = new Chart(ctx, {
        type: "pie",
        data: {
            labels: ["Morning", "Noon", "Afternoon"],
            datasets: [{ data: [data.morning, data.noon, data.afternoon] }]
        },
        options: { responsive: true }
    });
}

function showToast(message, type="success", duration=3000){
    const container = document.getElementById("toast-container");

    const toast = document.createElement("div");
    toast.className = `toast ${type}`;
    toast.textContent = message;

    container.appendChild(toast);

    setTimeout(() => {
        toast.style.opacity = "0";
        toast.style.transform = "translateX(30px)";
        setTimeout(()=> toast.remove(),300);
    }, duration);
}
