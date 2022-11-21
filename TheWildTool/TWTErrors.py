class NoHeaderError(Exception):
    """Raise your no header into file. Error: Your file does not contain a header with the proper syntax. Check the documentation to learn more.

    Args:
        Exception (_type_): _description_
    """    
    def __init__(self):
        super().__init__('Your file does not contain a header with the proper syntax. Check the documentation to learn more.')