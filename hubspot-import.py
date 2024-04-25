import json
import os

import requests

token = os.environ["HUBSPOT_ACCESS_TOKEN"]
listname = os.environ["LISTNAME"]
csvfile = os.environ["CSVFILE"]

url = "https://api.hubapi.com/crm/v3/imports"

headers = {
    'authorization': 'Bearer %s' % token
}

data = {
    "name": f"{listname}",
    "importOperations": {
        "0-1": "CREATE"
    },
    "dateFormat": "DAY_MONTH_YEAR",
    "createContactListFromImport": True,
    "files": [
        {
            "fileName": f"{csvfile}",
            "fileType": "CONTACTS",
            "fileFormat": "CSV",
            "fileImportPage": {
                "hasHeader": True,
                "columnMappings": [
                    {
                        "columnObjectTypeId": "0-1",
                        "columnName": "firstname",
                        "propertyName": "firstname"
                    },
                    {
                        "columnObjectTypeId": "0-1",
                        "columnName": "lastname",
                        "propertyName": "lastname"
                    },
                    {
                        "columnObjectTypeId": "0-1",
                        "columnName": "email",
                        "propertyName": "email",
                        "columnType": "HUBSPOT_ALTERNATE_ID"
                    },
                    {
                        "columnObjectTypeId": "0-1",
                        "columnName": "company",
                        "propertyName": "company"
                    },
                    {
                        "columnObjectTypeId": "0-1",
                        "columnName": "jobtitle",
                        "propertyName": "jobtitle"
                    },
                    {
                        "columnObjectTypeId": "0-1",
                        "columnName": "address",
                        "propertyName": "address"
                    },
                    {
                        "columnObjectTypeId": "0-1",
                        "columnName": "city",
                        "propertyName": "city"
                    },
                    {
                        "columnObjectTypeId": "0-1",
                        "columnName": "state",
                        "propertyName": "state"
                    },
                    {
                        "columnObjectTypeId": "0-1",
                        "columnName": "country",
                        "propertyName": "country"
                    }
                ]
            }
        }
    ]
}

datastring = json.dumps(data)

payload = {"importRequest": datastring}

current_dir = os.path.dirname(__file__)
relative_path = f"./{csvfile}"

absolute_file_path = os.path.join(current_dir, relative_path)

files = [
    ('files', open(absolute_file_path, 'rb'))
]

response = requests.request("POST", url, data=payload, files=files, headers=headers)

print(response.text.encode('utf8'))
print(response.status_code)
