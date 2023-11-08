'''
YAML loader. handy, and I needed a template for one so here we go.


'''


import yaml

class PluginConfig:
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        self.config = None

    def load_config(self):
        try:
            with open(self.config_file_path, 'r') as config_file:
                self.config = yaml.safe_load(config_file)
            return True
        except Exception as e:
            print(f"Error loading configuration from {self.config_file_path}: {e}")
            return False

    def get_value(self, key, default=None):
        if self.config is not None:
            keys = key.split('.')
            value = self.config
            for k in keys:
                if k in value:
                    value = value[k]
                else:
                    return default
            return value
        else:
            print("Configuration is not loaded. Call load_config() first.")
            return default

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