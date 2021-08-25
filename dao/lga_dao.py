from nigerian_locations.models import State, LGA, Area, Localities
from my_modules.my_utils import MyUtils

class LGADao:

    def check_if_exits(self, name):
        if LGA.objects.filter(name=name).exists():
            return True
        return False
    
    def find_by_name(self, name):
        try:
            # return LGA.objects.exclude(pk=self.instance.pk).get(name=name)
            found = LGA.objects.get(name__iexact=name)
            # return MyUtils().serialize_model_to_json(found)
            return found
        except LGA.DoesNotExist:
            return None
    
    def find_by_id(self, id):
        try:
            found = LGA.objects.get(id=id)
            # return MyUtils().serialize_model_to_json(found)
            # return State.objects.exclude(pk=self.instance.pk).get(name=name)
            return found
        except LGA.DoesNotExist:
            return None