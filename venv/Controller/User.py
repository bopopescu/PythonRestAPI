class User:

    def __init__(self):
        '''self.uname = "abc"
        self.pwd = "hq"'''

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
