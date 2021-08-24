from nigerian_locations.models import State, LGA, Area, Localities

class StateDao:

    def check_if_exits(self, name):
        if State.objects.filter(name=name).exists():
            return True
        return False
    
    def find_by_name(self, name):
        try:
            return State.objects.exclude(pk=self.instance.pk).get(name=name)
        except State.DoesNotExist:
            return None