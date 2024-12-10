from tinydb import TinyDB, Query


db = TinyDB('db.json')
Form = Query()

def get_templates():
    return db.all()

def add_template(template: dict):
    db.insert(template)
    

# temp ={
#         "name": "Simple Form",
#         "text_short": "text",
#         "email": "email"
#     }

# add_template(temp)