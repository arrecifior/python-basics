###################################################################################
###   Simulating phone temperature fluctuations, logging data into a log file   ###
###################################################################################

import logging
import random

# format string
FORMAT = '%(levelname)s - %(message)s'

class BatterySimulation:
    def __init__(self, logger):
        self.logger = logger

    # simulating temperature fluctuations for an hour
    def simulate_last_hour(self):
        for minute in range (1, 60 + 1):
            temperature = random.randint(20, 40)

            if temperature < 30:
                self.logger.debug('{0} C'.format(temperature))
            elif temperature >= 30 and temperature <= 35:
                self.logger.warning('{0} C'.format(temperature))
            elif temperature > 35:
                self.logger.critical('{0} C'.format(temperature))
            else:
                raise Exception('Temperature out of range.')

# setting logger
logger = logging.getLogger('battery.temperature')
logger.setLevel(logging.DEBUG)

#setting logger handler
handler = logging.FileHandler('battery_temperature.log', mode='w')
handler.setLevel(logging.DEBUG)

# setting formatter
formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)
 
# adding formatter handler
logger.addHandler(handler)

sim = BatterySimulation(logger)
sim.simulate_last_hour()