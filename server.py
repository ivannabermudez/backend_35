from simpleflaskproject import Flask #from tool file import class / function/ variable
import json
from about import me
from data import mock_data

app = Flask(__name__) # create a instance of Flask class. needs a name inside ().

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
    return json.dumps(mock_data)

#get /api/product/count 
# return the number of products in the catalog
@app.get("/api/product/count")
def products_count():
    count = len(mock_data)
    return json.dumps(count)

# get/api/categories 
# return a list of categories
@app.get("/api/products/total")
def sum_prices():
    total = 0 
    for product in mock_data:
        price = product("price")
        total = total + price
    
    print(total) 
    return json.dumps(total)

@app.get("/api/categories")
def categories():
    cats = []
    for prod in mock_data:
        category = prod["category"]
        #if category does not exist inside the list only then you will push 
        if category not in cats:
            cats.append(category)

    return json.dumps(cats)

@app.get("/api/catalog/<category>")
def products_by_category(category):
    results = []
    for prod in mock_data:
        if prod["category"].lower() == category.lower():
            results.append(prod)

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
    results = []
    for prod in mock_data:
        if prod["price"] < fixed_price: 
            results.append(prod)

    return json.dumps(results)

@app.get("/api/products/greater/<price>")
def products_greater_price(price):
    fixed_price = float(price)
    results = []
    for prod in mock_data:
        if prod["price"] >= fixed_price: 
            results.append(prod)

    return json.dumps(results)

@app.get('/api/products/search/<term>')
def search_products(term):
    results = []
    for prod in mock_data:
        if term.lower() in prod["title"].lower():
            results.append(prod)
            
    return json.dumps(results)






# start the server
app.run(debug=True)   #do not use in production
