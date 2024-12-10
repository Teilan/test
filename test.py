import requests
# если все хорошо
url = "http://localhost:8000/get_form"
data = {
    "user_email": "example@mail.com",
    "user_phone": "+7 123 456 78 90",
    "order_date": "2023-12-10"
}

response = requests.post(url, json=data)
print(response.json())


# если все плохо
data_bad = {
    "user_email": "example@mail.com",
    "user_phone": "+7 123 456 78 90",
    "order_date": "2023-12-10",
    "textasd": "safddfgd"
}

response = requests.post(url, json=data_bad)
print(response.json())