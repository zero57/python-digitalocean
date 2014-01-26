class Size(object):
    def __init__(self, client_id="", api_key=""):
        self.client_id = client_id
        self.api_key = api_key

        self.name = None
        self.id = None
        self.memory = None
        self.cpu = None
        self.disk = None
        self.cost_per_hour = None
        self.cost_per_month = None
