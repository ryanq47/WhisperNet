class Data:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            # print("==== INIT =====")
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_initialized'):
            return
        self.Models = Models()
        self.Endpoints = Endpoints()
        self._initialized = True


# Info about the models/where they are at, etc
class Models:
    def __init__(self):
        # self._models = []  # Now private
        # temp placeholder for models until it gets working
        self._models = []
    # Models methods

    @property
    def models(self):
        return self._models

    @models.setter
    def models(self, models_list):
        self._models = models_list

    def add_model(self, name=None, path=None, desc=None):
        """
            Add a model to self.models, which is a list of dicts. (easy to turn into JSON that way)

            name: Name of Model
            path: API Path of Model.
                Ex: /api/model/MySuperCoolModel

        """
        model_dict = {
            "name": name,
            "api_path": path,
            "desc": desc
        }

        self._models.append(model_dict)

    def get_model(self, name):
        for model in self._models:
            if model['name'] == name:
                return model
        return None


class Endpoints:
    def __init__(self):
        self.python_endpoint = None
        self.javascript_endpoint = None
        self.c_endpoint = None
        self.cpp_endpoint = None
        self.rust_endpoint = None
        self.ruby_endpoint = None
