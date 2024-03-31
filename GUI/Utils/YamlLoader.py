'''
YAML loader. handy, and I needed a template for one so here we go.


'''


import yaml
from Utils.Logger import LoggingSingleton

class YamlLoader:
    def __init__(self, config_file_path):
        self.logger = LoggingSingleton.get_logger()
        self._config_file_path = config_file_path
        self._config = None

    ## Getter for config_file_path
    @property
    def config_file_path(self):
        return self._config_file_path

    ## This is the setter for the above method, ex: obj.config_file_path = mypath, this 
    @config_file_path.setter
    def config_file_path(self, value):
        self._config_file_path = value

    def load_config(self):
        print("LOAD CONFIG")
        try:
            with open(self._config_file_path, 'r') as config_file:
                #self._config = yaml.safe_load(config_file)
                self._config = yaml.safe_load(self._config_file_path)
                print(self._config)
                if self._config == None:
                    print("BROKEN")
            return self._config
        except Exception as e:
            print(f"[!] Error loading configuration from {self._config_file_path}: {e}")
            return False




# Example usage:
'''
if __name__ == "__main__":
    config_file_path = "sample_plugin_config.yaml"  # Replace with your config file path
    plugin_config = PluginConfig(config_file_path)

    if plugin_config.load_config():
        option1_value = plugin_config.get_value("configuration.option1")
        option2_value = plugin_config.get_value("configuration.option2")
        
        print(f"Option 1 value: {option1_value}")
        print(f"Option 2 value: {option2_value}")
'''