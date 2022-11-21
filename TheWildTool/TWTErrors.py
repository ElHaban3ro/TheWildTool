class NoHeaderError(Exception):
    """Raise your no header into file. Error: Your file does not contain a header with the proper syntax. Check the documentation to learn more.
    """    
    def __init__(self):
        super().__init__('Your file does not contain a header with the proper syntax. Check the documentation to learn more.')
class TimeTypeError(Exception):
    """Rais your wrong time format. Error: The time format is wrong or not yet supported.
    """    
    def __init__(self):
        super().__init__('The time format is wrong or not yet supported.')