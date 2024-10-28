from ExtractedData import ExtractedData

class InputStream:
    def __init__(self):
        self.EntityName = None
        self.payload = None

    def sendData(self, name, state):
        # Call the method in ExtractedData, passing the parameters
        extracted_data = ExtractedData.getDataFromStream(name, state)
        return extracted_data  # You can choose to return it if needed
