from dao.area_dao import AreaDao
from dao.states_dao import StateDao
from dao.lga_dao import LGADao
from dao.localities_dao import LocalitiesDao
from nigerian_locations.models import State, LGA, Area, Localities
from my_modules.excel_reader import ExcelReader
from my_modules.my_utils import MyUtils

class StateService:

    def find(self, name):

        found_state = StateDao().find_by_name(name)
        found_lga = LGADao().find_by_name(name)
        found_area = AreaDao().find_by_name(name)
        found_locality = LocalitiesDao().find_by_name(name)


        if found_locality != None and found_area == None:
            found_area = AreaDao().find_by_id(id=found_locality['area'])
        if found_area != None and found_lga == None:
            found_lga = LGADao().find_by_id(id=found_area['lga'])
        if found_lga != None and found_state == None:
            found_state = StateDao().find_by_id(id=found_lga['state'])

        return {
            'state': found_state,
            'lga': found_lga,
            'area': found_area,
            'locality': found_locality
        }

    def save_json_obj(self):
        json_list = self.read_json()

        for json_obj in json_list:
            state_obj = json_obj['state']

            state = None
            state_dao = StateDao()
            if state_dao.check_if_exits(name=state_obj):
                state = state_dao.find_by_name(name=state_obj)
            else:
                state = State.objects.create(name=state_obj)
                state.save()

            for json_lga in json_obj['lgas']:
                lga = None
                lga_dao = LGADao()
                if lga_dao.check_if_exits(name=json_lga):
                    lga = lga_dao.find_by_name(name=json_lga)
                else:    
                    lga = LGA.objects.create(name=json_lga, state=state)
                    lga.save()

    def init(self):
        # print("Started addding JSON")
        # self.save_json_obj()
        # print("Done adding JSON")

        print("Started addding Excel")
        excel_reader = ExcelReader()
        data = excel_reader.fetch_excel_reader()
        for row in data.iterrows():
            # print(type(row))

            my_size = list(row)
            #print(len(my_size)) #length is 2 thus data is stored on the object
            columns = row[1]
            state_name = columns['State Name']
            lga_name = columns['Lga Name']
            area_name = columns['Area Name']
            locality_name = columns['Locality Name']
            self.create(state_name, lga_name, area_name, locality_name)
            
            # with transaction.atomic():
            #     state_obj.save()
            # break
            # for j, column in list(row):
            #     print(column)

            # try:
            #     #print(row[1])
            #     #print(row[2])
            #     #print(row[4])
            #     print(row)
            #     # print(row[6])
            #     # print(row[7])
            #     # print(row[8])
            #     # print(row[9])
            #     # print(row[10])
            # except:
            #     pass
        print("Done adding Excel")
    
    def read_json(self):
        util = MyUtils()
        json_url = "./assets/json/state_and_lga.json"
        state_and_lga_list = util.read_file(json_url)
        
        list_of_states = []
        for state_and_lga in state_and_lga_list:
            state = state_and_lga['state']
            lgas = state_and_lga['lgas']
            obj = {'state': state, 'lgas': lgas }
            list_of_states.append(obj)
        return list_of_states

    def create(self, state_name, lga_name, area_name, locality_name):

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