import requests
import json

class ApiHandler(object):
    def nuevoEstudiante(self, estudiante):

       # url = "http://cfgsddi.hopto.org:5000/users"
        url = "http://localhost:5000/students"
        #_json = {'hola':'rafa'}
        _json = estudiante.__dict__
        _headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=json.dumps(_json), headers=_headers)

        dataJson = response.json()

        print(dataJson)