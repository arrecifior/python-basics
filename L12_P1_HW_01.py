##################################################################
###   Temperature conversion, getting data from an xml file   ###
#################################################################

import xml.etree.ElementTree as ET

class TemperatureConverter: # temperature converter class
    def convert_celsius_to_fahrengeit(self, temperature):
        return 9 / 5 * int(temperature) + 32

class ForecastXMLParser: # forecast parser class
    def __init__(self, temperature_converter): 
        # adding temp. converter object to a parser class
        self.temperature_converter = temperature_converter

    def parse(self, file_path): # xml parsing method
        tree = ET.parse(file_path)
        root = tree.getroot()
        for day in root:
            print(day[0].text + ': ' + day[1].text + ' Celsisuis, ' + str(round(self.temperature_converter.convert_celsius_to_fahrengeit(day[1].text), 1)) + ' Fahrenheit', sep='')

tc = TemperatureConverter()
fxp = ForecastXMLParser(tc)
fxp.parse('forecast.xml')
