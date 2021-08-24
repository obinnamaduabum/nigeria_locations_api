from dao.area_dao import AreaDao
from dao.states_dao import StateDao
from dao.lga_dao import LGADao
from dao.localities_dao import LocalitiesDao
from nigerian_locations.models import State, LGA, Area, Localities

class StateService:

    def create(self, state_name, lga_name, area_name, locality_name):
        if state_name and lga_name and area_name and locality_name:
                state = None
                state_dao = StateDao()
                if state_dao.check_if_exits(name=state_name):
                    state = state_dao.find_by_name(name=state_name)
                else:    
                    state = State.objects.create(name=state_name)
                    state.save()

                lga = None
                lga_dao = LGADao()
                if lga_dao.check_if_exits(name=lga_name):
                    lga = lga_dao.find_by_name(name=lga_name)
                else:    
                    lga = LGA.objects.create(name=lga_name, state=state)
                    lga.save()    

                area = None
                area_dao = AreaDao()
                if area_dao.check_if_exits(name=area_name):
                    area = area_dao.find_by_name(name=area_name)
                else:
                    area = Area.objects.create(name=area_name, lga=lga)
                    area.save()
            
                locality = None
                localities_dao = LocalitiesDao()
                if localities_dao.check_if_exits(name=locality_name):
                    locality = localities_dao.find_by_name(name=locality_name)
                else:
                    locality = Localities.objects.create(name=locality_name, area=area)
                    locality.save()