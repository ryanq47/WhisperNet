## move to different file eventually
import yaml
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

        self.SERVER_LOGIN_ENDPOINT       = ""

        self.UPLOAD_BASE_ENDPOINT        = ""
        self.UPLOAD_FOLDER               = ""

        self.HOME_BASE                   = ""

        self.CREATE_USER                 = ""
        self.DELETE_USER                 = ""

        self.HOMEPAGE_LIST               = ""

        self.NOT_FOUND_LIST_404          = ""

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
                raise Utils.ErrorDefinitions.YAML_LOAD_ERROR
            except Exception as e:
                raise Utils.ErrorDefinitions.GENERAL_ERROR()

    def assign_schema(self):
        '''
        Assigns schemas to respective variables
        '''
        ## Server
        self.SERVER_BASE_ENDPOINT       = self.yaml_parser["Server"]["Base"]
        SPAWN_TCP_LISTENER_ENDPOINT     = self.yaml_parser["Server"]["SpawnTcpListener"]

        ## Client
        self.SERVER_LOGIN_ENDPOINT      = self.yaml_parser["Misc"]["Login"]

        ## Agent
        self.AGENT_BASE_ENDPOINT        = self.yaml_parser["Agent"]["Base"]

        ## Fileserver
        self.UPLOAD_BASE_ENDPOINT       = self.yaml_parser["FileServer"]["Base"]
        self.UPLOAD_FOLDER              = self.yaml_parser["FileServer"]["Uploads"]

        ## Home
        self.HOME_BASE                  = self.yaml_parser["Home"]["Base"]

        ##management
        self.CREATE_USER                = self.yaml_parser["Management"]["CreateUser"]
        self.DELETE_USER                = self.yaml_parser["Management"]["DeleteUser"]

        ## Homepage HTML
        self.HOMEPAGE_LIST              = self.yaml_parser["HomepageList"]

        ## 404 Error list
        self.NOT_FOUND_LIST_404         = self.yaml_parser["NotFoundList_404"]