class ExtractedData:
    def __init__(self):
        self.DataEntityName = None
        self.payload = None

    @classmethod
    def getDataFromStream(cls, name, state):
        # Create a new object of ExtractedData class
        extracted_data = cls()
        
        # Assign the passed values to the object attributes
        extracted_data.DataEntityName = name
        extracted_data.payload = state
        
        return extracted_data
