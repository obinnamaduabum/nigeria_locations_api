from nigerian_locations.models import State

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
            found_state = State.objects.get(name=name)
            return found_state
            # return State.objects.exclude(pk=self.instance.pk).get(name=name)
        except State.DoesNotExist:
            return None