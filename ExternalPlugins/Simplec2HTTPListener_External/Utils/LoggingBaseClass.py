'''

A base class for handling errors
'''
import logging

class BaseLogging:
    def __init__(self, name="BaseLogger", level="DEBUG", print_to_screen=False, log_file_name="plugin.log"):
        self.logger = logging.getLogger(name)
        self.log_file_name = log_file_name
        self.function_debug_symbol = "[^]"
        self.logging_warning_symbol = "[!]"
        self.logging_info_symbol = "[*]"
        self.logging_debug_symbol = "[D]"
        self.configure_logger(level, print_to_screen)

    def configure_logger(self, level, print_to_screen):
        log_level = getattr(logging, level.upper(), None)
        if not isinstance(log_level, int):
            raise ValueError(f'Invalid log level: {level}')

        logging.basicConfig(filename=self.log_file_name, filemode='a', 
                            format='%(asctime)s - %(levelname)s - %(message)s', 
                            force=True, datefmt='%Y-%m-%d %H:%M:%S')
        self.logger.setLevel(log_level)

        if print_to_screen:
            screen_handler = logging.StreamHandler()
            screen_handler.setLevel(log_level)
            self.logger.addHandler(screen_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

