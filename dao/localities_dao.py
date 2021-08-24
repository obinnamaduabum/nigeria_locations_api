from nigerian_locations.models import Localities
from my_modules.my_utils import MyUtils

class LocalitiesDao:

    def check_if_exits(self, name):
        if Localities.objects.filter(name=name).exists():
            return True
        return False
    
    def find_by_name(self, name):
        try:
            # return Localities.objects.exclude(pk=self.instance.pk).get(name=name)
            found = Localities.objects.get(name__iexact=name)
            return MyUtils().serialize_model_to_json(found)

        except Localities.DoesNotExist:
            return None
    
    def find_by_id(self, id):
        try:
            found = Localities.objects.get(id=id)
            return MyUtils().serialize_model_to_json(found)
            # return State.objects.exclude(pk=self.instance.pk).get(name=name)
        except Localities.DoesNotExist:
            return None