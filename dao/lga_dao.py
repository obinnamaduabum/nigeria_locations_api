from nigerian_locations.models import State, LGA, Area, Localities

class LGADao:

    def check_if_exits(self, name):
        if LGA.objects.filter(name=name).exists():
            return True
        return False
    
    def find_by_name(self, name):
        try:
            # return LGA.objects.exclude(pk=self.instance.pk).get(name=name)
            found = LGA.objects.get(name=name)
            return found
        except LGA.DoesNotExist:
            return None