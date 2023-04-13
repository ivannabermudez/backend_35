from flask import Flask, request, abort #from tool file import class / function/ variable
import json
from about import me
from data import mock_data
from config import db
from flask_cors import CORS

app = Flask(__name__) # create a instance of Flask class. needs a name inside ().
CORS (app) #warning: this disables cors

### web server ###
@app.get("/")
def home():
    return "hello world from a flask server"

@app.get("/test")
def test():
    return "this is a test page"


###############
# ####### API SERVER ################
########################################
#application programming interface- a program designed to be consumed by the other service
# data back and forth

@app.get("/api/version")
def version():
    return json.dumps("1.0")

@app.get("/api/about")
def about():
    return json.dumps(me)

#get /api/developer/Name
# return the full name of the developer plus the 
@app.get("/api/developer/name")
def dev_name():
    name = me["name"]
    last = me["last_name"]
    email = me["email"]
    response = f"{name} {last} -- {email}"
    return json.dumps(response)

# return json.dumps(f")

# get/api/catalog
#return all products as a json string
@app.get("/api/catalog")
def get_catalog():
    cursor = db.products.find({})
    results = []
    for prod in cursor:
            results.append(fix_id(prod))
    return json.dumps(mock_data)

def fix_id(record):
    record["_id"] = str(record["_id"])
    return record

@app.post("/api/catalog")
def save_product():
    product = request.get_json() # get the json payload from the request
    # save product to db
    db.products.insert_one(product)

    return json.dumps(fix_id(product))

#get /api/product/count 
# return the number of products in the catalog
@app.get("/api/product/count")
def products_count():
    count = db.products.count_documents({})
    return json.dumps(count)

# get/api/categories 
# return a list of categories
@app.get("/api/products/total")
def sum_prices():
    #get all products from db 
    #iterate over the cursor instead of mock data
    cursor = db.products.find({})
    total = 0 
    for product in cursor:
        price = product("price")
        total = total + price
    
    print(total) 
    return json.dumps(total)

@app.get("/api/categories")
def categories():
    cursor = db.products.find({})
    #cursor
    cats = []
    for prod in cursor:
        category = prod["category"]
        #if category does not exist inside the list only then you will push 
        if category not in cats:
            cats.append(category)

    return json.dumps(cats)

@app.get("/api/catalog/<category>")
def products_by_category(category):
    cursor = db.products.find({"category": category})
    results = []
    for prod in cursor:
        results.append(fix_id(prod))

        return json.dumps(results)

# create a list 
# travel mock_date with a for loop
# from the product, get the category
# if category is equal to the category we received 
# if so, append product to the lsit 
# at the end of the for loop, return the list

#categoories = ["milk", "barista", "sweeteners"]

@app.get("/api/products/lower/<price>")
def products_lower_price(price):
    fixed_price = float(price)
    cursor = db.products.find({})
    results = []
    for prod in cursor:
        if prod["price"] < fixed_price: 
            results.append(fix_id(prod))

    return json.dumps(results)

@app.get("/api/products/greater/<price>")
def products_greater_price(price):
    fixed_price = float(price)
    cursor = db.products.find({})
    results = []
    for prod in cursor:
        if prod["price"] >= fixed_price: 
            results.append(fix_id(prod))

    return json.dumps(results)

@app.get('/api/products/search/<term>')
def search_products(term):
    cursor = db.products.find({"title": {'$regex':term, "$options": "i" }})
    results = []
    for prod in cursor:
            results.append(fix_id(prod))

    return json.dumps(results)


@app.post("/api/coupons")
def save_coupon():
    coupon = request.get_json()
    db.coupons.insert_one(coupon)

    return json.dumps(fix_id(coupon))

@app.get("/api/coupons")
def get_coupons():
    cursor = db.coupons.find({})
    results = []
    for coupon in cursor:
        results.append(fix_id(coupon))

        return json.dumps(results)
    
#get api/coupons/<code>
# return the coupon with the given code 

@app.get("/api/coupons/<code>") 
def get_coupon_by_code(code):
    cursor = db.coupons.find_one({"code": code})
    if coupon == None:
        return abort(404, "Invalid coupon code")
    

    return json.dumps(fix_id(coupon))

# start the server
app.run(debug=True)   #do not use in production
