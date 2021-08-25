from nigerian_locations.models import State
from my_modules.my_utils import MyUtils

class StateDao:

    def __init__(self):
        pass

    def check_if_exits(self, name):
        if State.objects.filter(name=name).exists():
            return True
        return False

    def count(self):
        return State.objects.count()

    def find_by_name(self, name):
        try:
            input = name.lower()
            # name__iexact - this ignores all cases 
            found = State.objects.get(name__iexact=input)
            # return MyUtils().serialize_model_to_json(found)
            return found
            # return State.objects.exclude(pk=self.instance.pk).get(name=name)
        except State.DoesNotExist:
            return None


    def find_by_id(self, id):
        try:
            found = State.objects.get(id=id)
            return found
            # return MyUtils().serialize_model_to_json(found)
            # return State.objects.exclude(pk=self.instance.pk).get(name=name)
        except State.DoesNotExist:
            return None