from django.core import serializers
import json

class MyUtils:

    def serialize_model_to_json(self, data):
        serialized_obj = serializers.serialize('json', [data])
        # print("!!!!!!!!!!!!!!!!!!!")
        print(type(serialized_obj))
        obj_as_json = json.loads(serialized_obj)
        fields_obj = obj_as_json[0]['fields']
        print(type(fields_obj))
        # print("!!!!!!!!!!!!!!!!!!!")
        return fields_obj