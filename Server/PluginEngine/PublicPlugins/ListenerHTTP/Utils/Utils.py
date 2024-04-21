
class Standalone:
    
    @staticmethod
    def init_logger():
        """
            For when plugin is IN standalone mode, init the logging singleton as it
            may not be init'd yet.
        """
        import logging
        from Utils.Logger import LoggingSingleton
        logger = LoggingSingleton.get_logger(log_level=logging.DEBUG)
        del(logger)