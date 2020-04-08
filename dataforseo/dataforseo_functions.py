from django.http import JsonResponse, HttpRequest
from .client import RestClient
client = RestClient("login", "password")

# Funciones V3
def paises_v3():
    response = client.get("/v3/dataforseo_labs/locations_and_languages")
    paises = list()
    if response["status_code"] == 20000:
        resultado = response['tasks'][0]['result']
        # do something with result
        for res in resultado:
            paises.append(
                (str(res['location_code'])+'/'+res['available_languages'][0]['language_code'], res['available_languages'][0]['language_code']+'/'+res['country_iso_code'])
            )
        return paises

    else:
        print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))

def related_keywords_v3(keyword, country_code, language_code, depth, limit):
    post_data = dict()
    # simple way to set a task
    post_data[len(post_data)] = dict(
        keyword=keyword,
        location_code=country_code,
        language_code=language_code,
        depth = depth,
        limit = limit,
    )
    response = client.post("/v3/dataforseo_labs/related_keywords/live", post_data)

    if response["status_code"] == 20000:
        # do something with result
        return response['tasks'][0]['result'][0]
    else:
        print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))

def keyword_suggestions_v3(keyword, country_code, language_code, limit):
    post_data = dict()
    # simple way to set a task
    post_data[len(post_data)] = dict(
        keyword=keyword,
        location_code=country_code,
        language_code=language_code,
        limit = limit,
    )
    response = client.post("/v3/dataforseo_labs/keyword_suggestions/live", post_data)
    if response["status_code"] == 20000:
        # do something with result
        return response['tasks'][0]['result'][0]
    else:
        print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))

def keyword_ideas_v3(keyword, country_code, language_code, limit):
    post_data = dict()
    # simple way to set a task
    post_data[len(post_data)] = dict(
        keyword=keyword,
        location_code=country_code,
        language_code=language_code,
        limit = limit,
    )
    # POST /v3/dataforseo_labs/keyword_ideas/live
    response = client.post("/v3/dataforseo_labs/keyword_ideas/live", post_data)
    if response["status_code"] == 20000:
        # do something with result
        return response['tasks'][0]['result'][0]
    else:
        print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))