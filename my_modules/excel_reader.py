import pandas as pd

from django.db import transaction
from service.state_service import StateService

class ExcelReader:

    
    def fetch_excel_reader(self):
        data = pd.read_excel('./assets/excel/nigeria-state-and-localities.xlsx')
        # area_name_list = data['Area Name'].tolist()
        # locality_list = data['Locality Name'].tolist()
        # area_name_set = set(area_name_list)
        # locality_set = set(locality_list)
        # print(data)
        for row in data.iterrows():
            # print(type(row))

            my_size = list(row)
            #print(len(my_size)) #length is 2 thus data is stored on the object

            columns = row[1]
            state_name = columns['State Name']
            lga_name = columns['Lga Name']
            area_name = columns['Area Name']
            locality_name = columns['Locality Name']

            state_service = StateService()
            state_service.create(state_name, lga_name, area_name, locality_name)
            break
            
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
    
    