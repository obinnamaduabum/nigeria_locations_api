from nigerian_locations.models import Area, Localities

class AreaDao:

    def check_if_exits(self, name):
        if Area.objects.filter(name=name).exists():
            return True
        return False
    
    def find_by_name(self, name):
        try:
            return Area.objects.exclude(pk=self.instance.pk).get(name=name)
        except Area.DoesNotExist:
            return None