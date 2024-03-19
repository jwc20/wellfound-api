
class Companies:
    def __init__(self, **kwargs):
        self.companies = kwargs.get("companies", [])
        self.data = self.get_companies() 

    def get_companies(self):
        return self.companies
