## move to different file eventually
import yaml
import ApiEngine.ErrorDefinitions
import Utils.ErrorDefinitions

class UrlSchema:
    '''
    Holds the URL schemas.

    Named short for orginzation (full nane is UrlSchema)
    '''
    def __init__(self, api_config_profile = None):
        self.api_config_profile = api_config_profile
        self.yaml_parser = None
        self.SPAWN_TCP_LISTENER_ENDPOINT = ""
        self.SERVER_BASE_ENDPOINT        = ""

        self.AGENT_BASE_ENDPOINT         = ""

        self.UPLOAD_BASE_ENDPOINT        = ""
        self.UPLOAD_FOLDER               = ""

        self.HOME_BASE                   = ""

    def load(self):
        if self.load_schema():
            self.assign_schema()
        else:
            print("yamlerr")

    def load_schema(self):
        '''
        Opens yaml schema file
        returns yaml handler
        '''
        ## YamlLoad
        with open(self.api_config_profile, "r") as yaml_stream:
            try:
                self.yaml_parser = yaml.safe_load(yaml_stream)
                return True
            except yaml.YAMLError as ye:
                raise ApiEngine.ErrorDefinitions.YAML_LOAD_ERROR
            except Exception as e:
                raise Utils.ErrorDefinitions.GENERAL_ERROR()

    def assign_schema(self):
        '''
        Assigns schemas to respective variables
        '''
        ## Server
        self.SERVER_BASE_ENDPOINT       = self.yaml_parser["Server"]["Base"]
        SPAWN_TCP_LISTENER_ENDPOINT     = self.yaml_parser["Server"]["SpawnTcpListener"]

        ## Agent
        self.AGENT_BASE_ENDPOINT        = self.yaml_parser["Agent"]["Base"]

        ## Fileserver
        self.UPLOAD_BASE_ENDPOINT       = self.yaml_parser["FileServer"]["Base"]
        self.UPLOAD_FOLDER              = self.yaml_parser["FileServer"]["Uploads"]

        ## Home
        self.HOME_BASE                  = self.yaml_parser["Home"]["Base"]