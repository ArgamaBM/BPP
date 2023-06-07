import unittest
import numpy as np
from main import *

class Test_EMController(unittest.TestCase):
    def setUp(self):
        self.controller = EMController(0, 0, 0, 0, None, "", "")

    def tearDown(self):
        pass

    # Test basic battery scenarios
    def test_basic_battery_charge(self):
        self.controller.pv_production = 6000
        self.controller.house_consumption = 4000
        self.controller.storage_capacity = 5000
        self.controller.batt_state = 0
        self.controller.key = None
        self.controller.commands = ""
        self.controller.result = 'Charge'

        self.controller.power_management()
        self.assertEqual(self.controller.get(), self.controller.result)

        self.controller.reset_state()
        self.assertNotEqual(self.controller.get(), self.controller.result)

    def test_basic_battery_sell_to_grid(self):
        self.controller.pv_production = 8000
        self.controller.house_consumption = 3000
        self.controller.storage_capacity = 5000
        self.controller.batt_state = 1
        self.controller.key = None
        self.controller.commands = ""
        self.controller.result = 'Sell to grid'

        self.controller.power_management()
        self.assertEqual(self.controller.get(), self.controller.result)

        self.controller.reset_state()
        self.assertNotEqual(self.controller.get(), self.controller.result)

    def test_basic_battery_discharge(self):
        self.controller.pv_production = 2000
        self.controller.house_consumption = 6000
        self.controller.storage_capacity = 5000
        self.controller.batt_state = 1
        self.controller.key = None
        self.controller.commands = ""
        self.controller.result = 'Discharge'

        self.controller.power_management()
        self.assertEqual(self.controller.get(), self.controller.result)

        self.controller.reset_state()
        self.assertNotEqual(self.controller.get(), self.controller.result)

    def test_basic_battery_buy_from_grid(self):
        self.controller.pv_production = 1000
        self.controller.house_consumption = 8000
        self.controller.storage_capacity = 5000
        self.controller.batt_state = 0
        self.controller.key = None
        self.controller.commands = ""
        self.controller.result = 'Buy from grid'

        self.controller.power_management()
        self.assertEqual(self.controller.get(), self.controller.result)

        self.controller.reset_state()
        self.assertNotEqual(self.controller.get(), self.controller.result)

    def test_basic_battery_pv_supplies_house(self):
        self.controller.pv_production = 5000
        self.controller.house_consumption = 5000
        self.controller.storage_capacity = 5000
        self.controller.batt_state = 0
        self.controller.key = None
        self.controller.commands = ""
        self.controller.result = 'PV supplies house'

        self.controller.power_management()
        self.assertEqual(self.controller.get(), self.controller.result)

        self.controller.reset_state()
        self.assertNotEqual(self.controller.get(), self.controller.result)

    # Test standard battery scenarios
    def test_standard_battery_charge(self):
        self.controller.pv_production = 9000
        self.controller.house_consumption = 7000
        self.controller.storage_capacity = 10000
        self.controller.batt_state = 0
        self.controller.key = None
        self.controller.commands = ""
        self.controller.result = 'Charge'

        self.controller.power_management()
        self.assertEqual(self.controller.get(), self.controller.result)

        self.controller.reset_state()
        self.assertNotEqual(self.controller.get(), self.controller.result)

    

if __name__ == '__main__':
    unittest.main()