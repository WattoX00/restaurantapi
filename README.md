pip install -r requirements.txt

This been read

FastAPI routes:

MasterData (menu):

@router.get("/get_menu")

@router.post("/new_item")

@router.delete("/delete_item/{id}")

@router.patch("/patch_item/{id}")

Orders: 

@router.post("/add_order")

@router.get("/view_orders")

@router.get("/view_order/{id}")

@router.patch("/update_odrder/{id}")

@router.patch("/finish_order/{id}")


Statistics:

@router.get("/most_items_sold")

@router.get("/least_items_sold")

@router.get("/monthly_data")
