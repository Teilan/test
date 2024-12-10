from errors import errorDateNotValidate, errorEmailNotValidate, errorPhonelNotValidate
import re

def validate_email(email: str) -> str:
    if re.fullmatch(r'^[^@]+@[^@]+\.[^@]+$', email):
        return True
    else:
        return errorEmailNotValidate

def validate_phone_number(phone_number: str) -> str:
    if re.fullmatch(r'\+7 \d{3} \d{3} \d{2} \d{2}', phone_number):
        return True
    else:
        return errorPhonelNotValidate
        

def validate_date(date: str) -> str:
    if re.fullmatch(r'\d{4}-\d{2}-\d{2}', date) or re.fullmatch(r'\d{2}\.\d{2}\.\d{4}', date):
        return True
    else:
        return errorDateNotValidate
    
def get_field_type(value: str) -> str:
    if validate_date(value) is True:
        return "DATE"
    
    elif validate_phone_number(value) is True:
        return "PHONE"
    
    elif validate_email(value) is True:
        return "EMAIL"
    
    else:
        return "TEXT"