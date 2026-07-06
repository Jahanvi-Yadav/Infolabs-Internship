# Practice 3 : Python Dictionary Task

mydata = {
    "ecommerce": {
        "categories": [
            {
                "name": "Electronics",
                "products": [
                    {
                        "product": "Laptop",
                        "price": 50000
                    },
                    {
                        "product": "Mobile",
                        "price": 25000
                    }
                ]
            },
            {
                "name": "Fashion",
                "products": [
                    {
                        "product": "Shirt",
                        "price": 1000
                    }
                ]
            }
        ]
    }
}

# Print Electronics
print(mydata["ecommerce"]["categories"][0]["name"])

# Print Laptop
print(mydata["ecommerce"]["categories"][0]["products"][0]["product"])

# Print Laptop price
print(mydata["ecommerce"]["categories"][0]["products"][0]["price"])

# Print Mobile
print(mydata["ecommerce"]["categories"][0]["products"][1]["product"])

# Print Mobile price
print(mydata["ecommerce"]["categories"][0]["products"][1]["price"])

# Print Fashion
print(mydata["ecommerce"]["categories"][1]["name"])

# Print Shirt
print(mydata["ecommerce"]["categories"][1]["products"][0]["product"])

# Print Shirt price
print(mydata["ecommerce"]["categories"][1]["products"][0]["price"])

# Print total categories
print(len(mydata["ecommerce"]["categories"]))

# Print total products in Electronics
print(len(mydata["ecommerce"]["categories"][0]["products"]))