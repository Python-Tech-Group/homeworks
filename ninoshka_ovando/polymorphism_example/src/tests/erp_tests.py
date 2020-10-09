import unittest
import datetime
from src.tests.test_data import *
from src.human_resources import Contract, Piecework, Practitioner


class Test(unittest.TestCase):

    def test_contract_with_8_years(self):

        date_str = '2010/01/01'
        format_str = '%Y/%m/%d'
        datetime_temploral = datetime.datetime.strptime(date_str, format_str)

        contract = Contract("12345", "name", "lastname", datetime_temploral, 9000)

        self.assertEqual(contract.__str__(), CONTRACT_8YEAR)

    def test_contract_with_16_years(self):

        date_str = '2000/01/01'
        format_str = '%Y/%m/%d'
        datetime_temploral = datetime.datetime.strptime(date_str, format_str)

        contract = Contract("12345", "name", "lastname", datetime_temploral, 9000)

        self.assertEqual(contract.__str__(), CONTRACT_16YEAR)


    def test_piecework_with_20_clients(self):

        date_str = '2000/01/01'
        format_str = '%Y/%m/%d'
        datetime_temploral = datetime.datetime.strptime(date_str, format_str)

        piecework = Piecework("12345", "name", "lastname", datetime_temploral, 20)

        self.assertEqual(piecework.__str__(), PIECEWORK_20_CLIENTS)

    def test_piecework_with_20_clients(self):
        date_str = '2000/01/01'
        format_str = '%Y/%m/%d'
        datetime_temploral = datetime.datetime.strptime(date_str, format_str)

        practitioner = Practitioner("12345", "name", "lastname", datetime_temploral, 80)

        self.assertEqual(practitioner.__str__(), PRACTITIONER_80_EVALUATION)
