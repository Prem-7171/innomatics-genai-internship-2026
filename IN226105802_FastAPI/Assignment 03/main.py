from fastapi import FastAPI, Query, HTTPException, status, Response
from pydantic import BaseModel, Field
 
app = FastAPI()

# Class For pydantic Model
class CustomerFeedback(BaseModel):
    customer_name : str = Field(..., min_length = 2)
    product_id : int = Field(..., gt=0)
    rating : int = Field(..., ge=1, le=5)
    comment : str | None = Field(None, max_length=300)
    
# Empty List for storing Feedback
feedback = []

# Empty List for recievening Orders
orders = []
 
# Pydantic model for OrderItems
class OrderItem(BaseModel):
    product_id : int = Field(..., gt=0)
    quantity : int = Field(..., ge=1, le=50)
    
# Pydantic model for Bulk Orders
class BulkOrder(BaseModel):
    company_name : str = Field(..., min_length=2)
    contact_email : str = Field(...,min_length=5)
    items : list[OrderItem] = Field(..., min_items = 1 )
 
# ── Temporary data — acting as our database for now ──────────
products = [
    {'id': 1, 'name': 'Wireless Mouse', 'price': 499,  'category': 'Electronics', 'in_stock': True },
    {'id': 2, 'name': 'Notebook',       'price':  99,  'category': 'Stationery',  'in_stock': True },
    {'id': 3, 'name': 'USB Hub',         'price': 799, 'category': 'Electronics', 'in_stock': False},
    {'id': 4, 'name': 'Pen Set',          'price':  49, 'category': 'Stationery',  'in_stock': True },
    {'id': 5, 'name': 'Laptop Stand',      'price':  399, 'category': 'Accessories',  'in_stock': False },
    {'id': 6, 'name': 'Mechanical Keyboard',          'price':  1300, 'category': 'Electronics',  'in_stock': True },
    {'id': 7, 'name': 'Normal Keyboard',          'price':  1300, 'category': 'Electronics',  'in_stock': True },
    {'id': 8, 'name': 'Webcam',          'price':  599, 'category': 'Electronics',  'in_stock': True },
]
 
# ── Endpoint 0 — Home ────────────────────────────────────────
@app.get('/')
def home():
    return {'message': 'Welcome to our E-commerce API'}
 
# ── Endpoint 1 — Return all products ──────────────────────────
@app.get('/products')
def get_all_products():
    return {'products': products, 'total': len(products)}

# Filtering
@app.get('/products/filter')
def filter_products(
    category:  str  = Query(None, description='Electronics or Stationery'),
    max_price: int  = Query(None, description='Maximum price'),
    in_stock:  bool = Query(None, description='True = in stock only'),
    min_price: int = Query(None, description='Minimum Price ')
):
    result = products          # start with all products
 
    if category:
        result = [p for p in result if p['category'] == category]
 
    if max_price:
        result = [p for p in result if p['price'] <= max_price]
 
    if in_stock is not None:
        result = [p for p in result if p['in_stock'] == in_stock]
        
    # Question 1 min Price    
    if min_price:
        result = [p for p in products if p['price'] >= min_price]
 
    return {'filtered_products': result, 'count': len(result)}
 
# ── Endpoint 2 — Return one product by its ID ──────────────────
@app.get('/products/product_id/{product_id}')
def get_product(product_id: int):
    for product in products:
        if product['id'] == product_id:
            return {'product': product}
    return {'error': 'Product not found'}


@app.get('/products/category/{category}')
def get_category(category):
    matching_products = []
    for product in products:
        if product['category'] == category:
            matching_products.append(product)
    
    if matching_products:
        return {'Products':matching_products, 'total':len(matching_products)}
    else:
        return {'error':'Product not found'}
    


@app.get('/products/instock/')  
def get_instock():
    in_stock = []
    count = 0
    for p in products:
        if p['in_stock']:
            in_stock.append(p)
            count += 1
    
    if in_stock:
        return {'in_stock_products':in_stock, 'count':count}
    else:
        return {'error':'Nothing in stock'}
    

@app.get('/store/summary')
def get_summary():
    total_products = len(products)
    stock_count = sum(1 for product in products if product['in_stock'])
    no_stock_count = len(products) - stock_count
    
    categories = [p['category'] for p in products ]
    categories = set(categories)
    categories = list(categories)
    
    return {"store_name": "My E-commerce Store", "total_products": total_products, "in_stock": stock_count, "out_of_stock": no_stock_count, "categories":categories}
        
        

@app.get('/products/search/{keyword}')
def search(keyword):
    product_found =[product for product in products if keyword.lower() in product['name'].lower()]
    
    if product_found:
        return {"matched_products": product_found, "total_products_found": len(product_found)}
    else:
        return {"message": "No products matched your search"}
            
            

@app.get('/products/deals')
def get_deals():
    best_deals = min(products, key = lambda p: p['price'])
    expensive_deals = max(products, key = lambda p: p['price'])
    
    return {"best_deal":best_deals, "premium_pick": expensive_deals}

# Question 2 --> Getting only name and price of product
@app.get('/products/{product_id}/price')
def get_price(product_id: int):
    for product in products:
        if product['id'] == product_id:
            return {'name': product['name'], 'price':product['price']}
    return {'error': 'Product not found'}



@app.post('/feedback')
def get_feedback(customer_feedback : CustomerFeedback):
    
    feedback.append(customer_feedback.model_dump())
    return {'message':"Feedback submitted succcessfully", "feedback": customer_feedback.model_dump(), "total_feedback":len(feedback)}


@app.get('/products/summary')
def get_summary():
    in_stock_count = sum(1 for p in products if p['in_stock'])
    out_of_stock_count = len(products) - in_stock_count
    expensive_product = max(products, key = lambda p : p['price'])
    most_expensive = {'name' : expensive_product['name'], 'price': expensive_product['price']}
    cheapest = min(products, key = lambda p : p['price'])
    most_cheapest = {'name' : expensive_product['name'], 'price': expensive_product['price']}
    categories = list(set(p['category'] for p in products))
    return {'total_products': len(products), 'in_stock_count':in_stock_count, 'out_of_stock_count':out_of_stock_count, 'most_expensive': most_expensive, 'cheapest': most_cheapest,"categories":categories}
    
@app.post('/orders/bulk')
def take_order(orders : BulkOrder):
    confirmed = []
    failed = []
    grand_total = 0
    
    for item in orders.items:
        product = None
        for p in products:
            if p['id'] == item.product_id:
                product = p
                break
    
        if product is None:
            failed.append({'product_id': item.product_id, 'reason': 'product not found'})
            continue
        elif not product['in_stock']:
            failed.append({'product_id': item.product_id, 'reason': f"{product['name']} out of stock"})
            continue
        else:
            subtotal = product['price']*item.quantity
            confirmed.append({'product':product['name'], 'qty': item.quantity, 'subtotal': subtotal})
            grand_total += subtotal
            
    return {'company':orders.company_name, 'confirmed': confirmed, 'failed': failed, 'grand_total':grand_total}   
    
        
@app.post('/orders')
def place_order(product : str, qty : int):
    order_id = len(orders) + 1
    ordered = {'id': order_id, 'product': product, 'qty':qty, 'status':'pending'}
    orders.append(ordered)
    return {"order": ordered}

@app.get('/orders/{order_id}')
def get_order(order_id : int):
    for order in orders:
        if order_id == order['id']:
            return{'order':order}
       
    return {'error': 'order not found'}

@app.patch('/orders/{order_id}/confirm')
def confirm_order(order_id :int):
    for order in orders:
        if order['id'] == order_id:
            order['status'] = "confirmed"
            return {"order": order}
    return {'error': 'order not found'}


# Assignment 3

# Question 1
@app.post('/products')
def add_product(name : str,
                price: int,
                category : str,
                in_stock : bool,
                response : Response):
    for p in products:
        if name.lower() == p['name'].lower():
                raise HTTPException(
                    status_code=400,
                    detail="Product with this name already exists"
                )
    
    id = len(products) + 1
    new_product = {'id': id, 'name': name, 'price':  price,  'category': category,  'in_stock': in_stock }
    products.append(new_product)
        
        
    response.status_code = status.HTTP_201_CREATED
    return {'message': 'product added', 'product' : new_product}
    