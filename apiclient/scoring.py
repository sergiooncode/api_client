import requests


def get_consumer_scoring(endpoint, income, zipcode, age):
    url = "{endpoint}?income={income}&zipcode={zipcode}&age={age}".format(**{
        "endpoint": endpoint,
        "income": income,
        "zipcode": zipcode,
        "age": age,
    })
    resp = requests.get(url)
    return resp.json()
