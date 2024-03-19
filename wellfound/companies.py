
class Companies:
    def __init__(self, **kwargs):
        self.companies = kwargs.get("companies", [])
        self.data = self.get_data() 

    def get_data(self):
        return self.companies
