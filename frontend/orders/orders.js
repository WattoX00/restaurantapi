const API_URL = "http://localhost:8002";
let token = null;

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

async function addOrder(){
    const foods = document.getElementById("food_names").value.split(",").map(x => x.trim());
    const table = Number(document.getElementById("table_number").value);
    const description = document.getElementById("description").value;

    const payload = {
        food_names: foods,
        table_number: table,
        description: description,
        time: new Date().toISOString(),
        finished: false
    };

    const res = await fetch(`${API_URL}/add_order`, {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify(payload)
    });

    const data = await res.json();

    if(res.ok){
        showToast("Order added successfully!", "success");
    }else{
        showToast(data.detail || "Failed to add order", "error");
    }
}

async function viewOrders(){
    const res = await fetch(`${API_URL}/view_orders`);
    const data = await res.json();

    const container = document.getElementById("orders");
    container.innerHTML = "";

    data.forEach(o=>{
        const div = document.createElement("div");
        div.textContent = `ID:${o.id} | Table:${o.table_number} | Foods:${o.food_names.join(",")} | Finished:${o.finished}`;
        container.appendChild(div);
    });
}

async function viewFinishedOrders(){
    const res = await fetch(`${API_URL}/view_finished`);
    const data = await res.json();
 
    const container = document.getElementById("finished_orders");
    container.innerHTML = "";
 
    data.forEach(o=>{
        const div = document.createElement("div");
        div.textContent = `ID:${o.id} | Table:${o.table_number} | Foods:${o.food_names.join(",")} | Finished:${o.finished}`;
        container.appendChild(div);
    });
}

async function viewOrder() {
    const id = document.getElementById("view_id").value;

    const res = await fetch(`${API_URL}/view_order/${id}`);
    const data = await res.json();

    const container = document.getElementById("single_order");

    container.innerHTML = `
        <div class="order-card">

            <div class="order-header">
                <span>Order #${data.id}</span>
                <span>Table ${data.table_number}</span>
            </div>

            <div class="order-body">

                <div class="order-row">
                    <span class="order-label">Time</span>
                    <span class="order-value">${new Date(data.time).toLocaleString()}</span>
                </div>

                <div>
                    <div class="order-label">Foods</div>
                    <ul class="food-list">
                        ${data.food_names.map(food => `<li>${food}</li>`).join("")}
                    </ul>
                </div>

                <div class="order-label">Description</div>
                <div class="order-description">
                    ${data.description || "None"}
                </div>

                <div class="order-status ${data.finished ? "status-finished" : "status-progress"}">
                    ${data.finished ? "Finished" : "In Progress"}
                </div>

            </div>
        </div>
    `;
}

async function updateOrder(){
    const id = document.getElementById("update_id").value;
    const foods = document.getElementById("update_food_names").value.split(",").map(x => x.trim());
    const table = Number(document.getElementById("update_table_number").value);
    const description = document.getElementById("update_description").value;
    const finished = document.getElementById("update_finished").checked;

    const payload = {
        food_names: foods,
        table_number: table,
        description: description,
        time: new Date().toISOString(),
        finished: finished
    };

    const res = await fetch(`${API_URL}/update_odrder/${id}`, {
        method: "PATCH",
        headers:{
            "Content-Type":"application/json",
            "Authorization":`Bearer ${token}`
        },
        body: JSON.stringify(payload)
    });

    const data = await res.json();

    if(res.ok){
        showToast("Order updated successfully", "success");
    }else{
        showToast(data.detail || "Failed to update order", "error");
    }
}

async function finishOrder(){
    const id = document.getElementById("finish_id").value;

    const res = await fetch(`${API_URL}/finish_order/${id}`,{
        method:"PATCH",
        headers:{
            "Authorization":`Bearer ${token}`
        }
    });

    const data = await res.json();

    if(res.ok){
        showToast("Order marked as finished", "success");
    }else{
        showToast(data.detail || "Failed to finish order", "error");
    }
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
