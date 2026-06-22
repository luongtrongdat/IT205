import unittest
from main import calculate_energy_financials


class TestEnergyFinancials(unittest.TestCase):

    # Case 1: duoi nguong 50000 -> khong giam gia
    def test_case_1(self):
        devices = [
            {
                "id": "M01",
                "location": "A",
                "old_index": 0,
                "new_index": 10000,
                "status": "Normal"
            }
        ]

        result = calculate_energy_financials(devices)

        self.assertEqual(result, (10000, 0, 30000000))

    # Case 2: bang 50000 -> giam 3%
    def test_case_2(self):
        devices = [
            {
                "id": "M01",
                "location": "A",
                "old_index": 0,
                "new_index": 50000,
                "status": "Normal"
            }
        ]

        result = calculate_energy_financials(devices)

        self.assertEqual(result, (50000, 3, 145500000))

    # Case 3: lon hon 50000 -> giam 3%
    def test_case_3(self):
        devices = [
            {
                "id": "M01",
                "location": "A",
                "old_index": 0,
                "new_index": 60000,
                "status": "Normal"
            }
        ]

        result = calculate_energy_financials(devices)

        self.assertEqual(result, (60000, 3, 174600000))


if __name__ == "__main__":
    unittest.main()