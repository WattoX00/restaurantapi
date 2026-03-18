let token = "";

document.getElementById("loginForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const res = await fetch("http://localhost:8001/login", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({username, password})
    });

    const data = await res.json();
    if(res.ok){
        token = data.access_token;
        showToast("Login successful!", "success");
    } else {
        showToast(data.detail || "Login failed", "error");
    }
});

document.getElementById("addForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    if(!token){ showToast("Please login first!", "warning"); return; }

    const food_name = document.getElementById("food_name").value;
    const category = document.getElementById("category").value;
    const price = parseFloat(document.getElementById("price").value);
    const ingredients = document.getElementById("ingredients").value
        .split(",")
        .map(s => s.trim())
        .filter(s => s);
    const allergies = document.getElementById("allergies").value
        .split(",")
        .map(s => s.trim())
        .filter(s => s);
    const availability = document.getElementById("availability").value === "True";

    const res = await fetch("http://localhost:8001/new_item", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token
        },
        body: JSON.stringify({food_name, category, price, ingredients, allergies, availability})
    });

    const data = await res.json();
    showToast("Item added!", "success");
    fetchMenu();
});

let currentSort = null;

function setSort(type){
    currentSort = type;
    fetchMenu();
}

async function fetchMenu(){

    const res = await fetch("http://localhost:8001/get_menu");
    let items = await res.json();

    // sorting
    if(currentSort === "priceAsc"){
        items.sort((a,b)=>a.price-b.price);
    }

    if(currentSort === "priceDesc"){
        items.sort((a,b)=>b.price-a.price);
    }

    if(currentSort === "nameAsc"){
        items.sort((a,b)=>a.food_name.localeCompare(b.food_name));
    }

    if(currentSort === "category"){
        items.sort((a,b)=>a.category.localeCompare(b.category));
    }

    const ul = document.getElementById("menuList");
    ul.innerHTML = "";

    items.forEach(item => {

        const li = document.createElement("li");

        const info = document.createElement("div");
        info.className = "item-info";

        const name = document.createElement("div");
        name.className = "item-name";
        name.textContent = item.food_name;

        const category = document.createElement("div");
        category.className = "item-category";
        category.textContent = item.category;

        info.appendChild(name);
        info.appendChild(category);

        const price = document.createElement("div");
        price.className = "item-price";
        price.textContent = "$" + item.price;

        const status = document.createElement("div");
        status.className = "item-status";
        status.textContent = item.availability ? "Available" : "Unavailable";

        const actions = document.createElement("div");
        actions.className = "item-actions";

        const delBtn = document.createElement("button");
        delBtn.className = "delete-btn";
        delBtn.textContent = "Delete";

        delBtn.onclick = async () => {
            if(!token){ showToast("Please login first!", "warning"); return; }

            const res = await fetch(`http://localhost:8001/delete_item/${item.id}`, {
                method:"DELETE",
                headers:{ "Authorization": "Bearer " + token }
            });

            const data = await res.json();
            showToast(data.message,"success");
            fetchMenu();
        };

        const patchBtn = document.createElement("button");
        patchBtn.className = "toggle-btn";
        patchBtn.textContent = "Toggle";

        patchBtn.onclick = async () => {

            if(!token){ showToast("Please login first!", "warning"); return; }

            const res = await fetch(`http://localhost:8001/patch_item/${item.id}`,{
                method:"PATCH",
                headers:{
                    "Authorization":"Bearer "+token,
                    "Content-Type":"application/json"
                },
                body:JSON.stringify({availability:!item.availability})
            });

            const data = await res.json();
            showToast(data.message,"success");
            fetchMenu();
        };

        actions.appendChild(delBtn);
        actions.appendChild(patchBtn);

        li.appendChild(info);
        li.appendChild(price);
        li.appendChild(status);
        li.appendChild(actions);

        ul.appendChild(li);
    });
}

document.getElementById("refreshBtn").addEventListener("click", fetchMenu);

fetchMenu();

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
