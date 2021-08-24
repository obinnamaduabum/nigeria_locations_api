from nigerian_locations.models import Area
from django.core import serializers
from django.forms.models import model_to_dict
from my_modules.my_utils import MyUtils

class AreaDao:

    def check_if_exits(self, name):
        if Area.objects.filter(name=name).exists():
            return True
        return False
    
    def find_by_name(self, name):
        try:
            # return Area.objects.exclude(pk=self.instance.pk).get(name=name)
            found = Area.objects.get(name__iexact=name)
            return MyUtils().serialize_model_to_json(found)
    
        except Area.DoesNotExist:
            return None
    
    def find_by_id(self, id):
        try:
            found = Area.objects.get(id=id)
            return MyUtils().serialize_model_to_json(found)
            # return State.objects.exclude(pk=self.instance.pk).get(name=name)
        except Area.DoesNotExist:
            return None