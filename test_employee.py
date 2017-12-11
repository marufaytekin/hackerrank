import unittest
from unittest.mock import patch

from employee import Employee


class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        self.e1 = Employee("maruf", "veli", 1000)
        self.e2 = Employee("betul", "aytekin", 2000)
        print("setUp")

    def tearDown(self):
        """
        add files or entries data base delete them. 
        """
        print("tearDown")

    def test_email(self):
        self.assertEqual(self.e1.email, "maruf.veli@email.com")
        self.assertEqual(self.e2.email, "betul.aytekin@email.com")

        self.e1.first = "ayse"
        self.e2.first = "hande"

        self.assertEqual(self.e1.email, "ayse.veli@email.com")
        self.assertEqual(self.e2.email, "hande.aytekin@email.com")

    def test_apply_raise(self):
        print("test_apply_raise")

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'
            schedule = self.e1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/veli/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False
            schedule = self.e2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/aytekin/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()
