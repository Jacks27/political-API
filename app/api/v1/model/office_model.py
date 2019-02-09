office_list=[]

class OfficeModel:
    def __init__(self):
        self.offices = office_list

    def create_office(self, name, office_type):
        office = {
            'id': len(self.offices)+1,
            'name' : name,
            'office_type': office_type      
        }
        self.offices.append(office)
        return office
    def get_all_office(self):
        return self.offices

    def getoffice(self, id):
        if self.offices:
            for office_n in self.offices:
                if office_n.get('id') == id:
                    return office_n 

        
    

        