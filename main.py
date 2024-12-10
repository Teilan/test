from fastapi import FastAPI, HTTPException
from errors import errorEmptyValue
from db import get_templates
from validate import validate_email, validate_phone_number, validate_date, get_field_type

app = FastAPI(swagger_ui_parameters={"defaultModelsExpandDepth": -1})

def convert_to_field_types(data):
    result = {}
    for key, value in data.items():
        field_type = get_field_type(value)
        result[key] = field_type
    return result

@app.post("/get_form", tags=['Запрос'])
async def get_form(form_data: dict):
    if not form_data:
        raise HTTPException(errorEmptyValue.app_code, errorEmptyValue.err_text)
    valid = True
    for key, value in form_data.items():
        if key == 'order_date':
            valid = validate_date(value)
        elif key == 'user_phone':
            valid = validate_phone_number(value)
        elif key == 'user_email':
            valid = validate_email(value)
        if valid != True:
            raise HTTPException(valid.app_code, valid.err_text)
    matched_template = {}
    db_all = get_templates()
    for template in db_all:
        if set(list(form_data.keys())).issubset(list(template.keys())):
            matched_template['name'] = template['name']
    if matched_template:
        return matched_template
    else:
        return convert_to_field_types(form_data)
    

    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)