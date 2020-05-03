from django.http import JsonResponse, HttpRequest
from .client import RestClient

client = RestClient("login", "password")

# Funciones V3
KEY = "key"
COMPETITION = "competition"
CPC = "cpc"
SEARCH_VOLUME = "search_volume"

filtrosAPI_related = {KEY: "keyword_data.keyword", COMPETITION: "keyword_data.keyword_info.competition", CPC: "keyword_data.keyword_info.cpc", SEARCH_VOLUME: "keyword_data.keyword_info.search_volume",}
filtrosAPI = {KEY: "keyword", COMPETITION: "keyword_info.competition", CPC: "keyword_info.cpc", SEARCH_VOLUME: "keyword_info.search_volume",}

# Extracción de países e Idiomas
def paises_v3():
    response = client.get("/v3/dataforseo_labs/locations_and_languages")
    paises = list()
    if response["status_code"] == 20000:
        resultado = response["tasks"][0]["result"]
        # do something with result
        for res in resultado:
            paises.append(
                (
                    str(res["location_code"])
                    + "/"
                    + res["available_languages"][0]["language_code"],
                    res["available_languages"][0]["language_code"]
                    + "/"
                    + res["country_iso_code"],
                )
            )
        return paises

    else:
        print(
            "error. Code: %d Message: %s"
            % (response["status_code"], response["status_message"])
        )

# Keywords relacionadas
def related_keywords_v3(keyword, country_code, language_code, depth, limit, filters):
    post_data = dict()
    name = {"name": "relacionadas"}
    # simple way to set a task
    post_data[len(post_data)] = dict(
        keyword=keyword,
        location_code=country_code,
        language_code=language_code,
        depth=depth,
        limit=limit,
    )

    # Comprobar si filtros y añadirlos
    if filters:
        for row in filters:
            if type(row) is list:
                row[0] = filtrosAPI_related[row[0]]

        post_data[0]['filters'] = filters

    response = client.post("/v3/dataforseo_labs/related_keywords/live", post_data)
    if response["status_code"] == 20000:
        print(response)
        # Si hay resultados
        if response["tasks"][0]["result_count"] != 0:
            # do something with result
            response["tasks"][0]["result"][0]['name'] = "relacionadas"
            return response["tasks"][0]["result"][0]
        else:
            response["tasks"][0]["result"] = list()
            response["tasks"][0]["result"].append(name)
            return response["tasks"][0]["result"][0]

    else:
        print(
            "error. Code: %d Message: %s"
            % (response["status_code"], response["status_message"])
        )

# Keywords sugeridas
def keyword_suggestions_v3(keyword, country_code, language_code, limit, filters):
    post_data = dict()
    name = {"name": "similares"}
    # simple way to set a task
    post_data[len(post_data)] = dict(
        keyword=keyword,
        location_code=country_code,
        language_code=language_code,
        limit=limit,
    )

    # Comprobar si filtros y añadirlos
    if filters:
        for row in filters:
            if type(row) is list:
                row[0] = filtrosAPI[row[0]]
        post_data[0]['filters'] = filters

    response = client.post("/v3/dataforseo_labs/keyword_suggestions/live", post_data)
    if response["status_code"] == 20000:
        # Si hay resultados
        if response["tasks"][0]["result_count"] != 0:
            # do something with result
            return response["tasks"][0]["result"][0]
        else: 
            response["tasks"][0]["result"] = list()
            response["tasks"][0]["result"].append(name)
            return response["tasks"][0]["result"][0]
    else:
        print(
            "error. Code: %d Message: %s"
            % (response["status_code"], response["status_message"])
        )

# Funciones V2
# Search Volume Bulk
def bulk_search_volume(parameter_list):
    keyword_list = [
        dict(
            language="en",
            loc_name_canonical="United States",
            keys=[
                "average page rpm adsense",
                "adsense blank ads how long",
                "leads and prospects",
            ],
        )
    ]
    response = client.post("/v2/kwrd_sv_batch", dict(data=keyword_list))
    if response["status"] == "error":
        print(
            "error. Code: %d Message: %s"
            % (response["error"]["code"], response["error"]["message"])
        )
    else:
        print(response["results"])
