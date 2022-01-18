class Sticker:
    def __init__(self, model):
        self.model = model
        self.return_dict = {}

    def get_package_sticker(self):
        self.return_dict['full sticker'] = f'Full name {self.model.recipent_name} {self.model.recipent_surname} /n Street: {self.model.street} {self.model.house_number}/{self.model.apartment_number} /n{self.model.city}  /n{self.model.region} /n {self.model.country}'

    def get_data(self):
        return self.return_dict
