from fastapi import FastAPI, Query
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

# Question 3 --> Recieve Feedback

@app.post('/feedback')
def get_feedback(customer_feedback : CustomerFeedback):
    
    feedback.append(customer_feedback.model_dump())
    return {'message':"Feedback submitted succcessfully", "feedback": customer_feedback.model_dump(), "total_feedback":len(feedback)}
