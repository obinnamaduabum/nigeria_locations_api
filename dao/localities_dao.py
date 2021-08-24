from nigerian_locations.models import Localities

class LocalitiesDao:

    def check_if_exits(self, name):
        if Localities.objects.filter(name=name).exists():
            return True
        return False
    
    def find_by_name(self, name):
        try:
            return Localities.objects.exclude(pk=self.instance.pk).get(name=name)
        except Localities.DoesNotExist:
            return None