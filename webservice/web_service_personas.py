import json
from collections import namedtuple
from webservice.web_service import WebService

def custom_data_decoder(response_data_dictionary):
    print(response_data_dictionary)
    
    return namedtuple("Empresas",response_data_dictionary.keys())(response_data_dictionary.values())

def get_personas_activas() -> int:
    json_elementos = WebService("https://meetfever.eu/interface/api/meetfever/persona/ObtenerPersonasActivas").get_request_json()
    
    return json.loads(json_elementos, object_hook=custom_data_decoder)

def get_personas_registradas() ->int :
    
    json_elementos = WebService("https://meetfever.eu/interface/api/meetfever/persona/ObtenerPersonasRegistradas").get_request_json()
    
    return json.loads(json_elementos, object_hook=custom_data_decoder)