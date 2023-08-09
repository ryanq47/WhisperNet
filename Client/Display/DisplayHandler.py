'''
Prints display outputs, for big ticket items. Does not include things like help menus

'''
import Utils.PlatformData


class Display:
    @staticmethod
    def print_startup():
        """
        A method for printing everything needed at startup
        """
        Display.print_banner()
        Display.print_credits()
    

    @staticmethod
    def print_banner():
        print(AsciiText.shadow_whispernet)

    @staticmethod
    def print_credits():
        print("\t\tDeveloped by: ryanq.47\t\tgithub.com/ryanq47")

    def print_platform_data():
        '''
        Prints the platform data
        '''
        print(f"OS\t:\t{Utils.PlatformData.Platform.os}")



class AsciiText:
    shadow_whispernet = r"""
 \ \        /   |      _)                                 \  |          |   
  \ \  \   /    __ \    |    __|   __ \     _ \    __|     \ |    _ \   __| 
   \ \  \ /     | | |   |  \__ \   |   |    __/   |      |\  |    __/   |   
    \_/\_/     _| |_|  _|  ____/   .__/   \___|  _|     _| \_|  \___|  \__| 
                                  _|                                        

    """
