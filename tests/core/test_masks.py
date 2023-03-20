"""
"""
import unittest

from core import masks


class MasksTests(unittest.TestCase):
    """
    """

    @classmethod
    def setUpClass(cls) -> None:
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_local_ip_mask(self):
        data = "This is a string with IP address 127.0.0.1"
        found = masks.IPMask.find(data)
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0], "127.0.0.1")

    def test_non_local_ip_mask(self):
        data = "This is a string with non local 172.217.22.14 IP address"
        found = masks.IPMask.find(data)
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0], "172.217.22.14")

    def test_a_few_local_ip_addresses(self):
        data = "This is a string with a few 172.217.22.14 IP address 127.0.0.1"
        found = masks.IPMask.find(data)
        self.assertEqual(len(found), 2)
        self.assertTrue("172.217.22.14" in found)
        self.assertTrue("127.0.0.1" in found)

    def test_name_without_lastname(self):
        data = "Adam is going to do some cool shit in this world"
        found = masks.NamesMask.find(data)
        self.assertEqual(len(found), 1)
        self.assertTrue("Adam" in found)

    def test_name_with_lastname(self):
        data = "Adam Cohen is going to do some cool shit in this world"
        found = masks.NamesMask.find(data)
        self.assertEqual(len(found), 2)
        self.assertTrue("Adam" in found)
        self.assertTrue("Cohen" in found)

    def test_name_with_long_lastname(self):
        data = "Adam Cohen Hillel is going to do some cool shit in this world"
        found = masks.NamesMask.find(data)
        self.assertEqual(len(found), 2)
        self.assertTrue("Adam" in found)
        self.assertTrue("Cohen Hillel" in found)

    def test_short_link(self):
        data = "The user clicked on google.com"
        found = masks.LinkMask.find(data)
        self.assertEqual(len(found), 1)
        self.assertTrue("google.com" in found)

    def test_www_link(self):
        data = "The user clicked on www.google.com"
        found = masks.LinkMask.find(data)
        self.assertEqual(len(found), 1)
        self.assertTrue("www.google.com" in found)

    def test_http_link(self):
        data = "The user clicked on https://www.google.com"
        found = masks.LinkMask.find(data)
        self.assertEqual(len(found), 1)
        self.assertTrue("https://www.google.com" in found)

    def test_uk_international_phone_number(self):
        data = "The user called +447831879184"
        found = masks.PhoneMask.find(data)
        self.assertEqual(len(found), 1)
        self.assertTrue("+447831879184" in found)

    def test_us_international_phone_number(self):
        data = "The user called +12025550196"
        found = masks.PhoneMask.find(data)
        self.assertEqual(len(found), 1)
        self.assertTrue("+12025550196" in found)

    def test_no_international_phone_number(self):
        data = "The user called 07831879184"
        found = masks.PhoneMask.find(data)
        self.assertEqual(len(found), 1)
        self.assertTrue("07831879184" in found)

    def test_email_gmail(self):
        data = "testing with thisisatest@gmail.com"
        found = masks.EmailMask.find(data)
        self.assertEqual(len(found), 1)
        self.assertTrue("thisisatest@gmail.com" in found)

    def test_not_known_mail_address(self):
        data = "testing with thisisatest@company.com"
        found = masks.EmailMask.find(data)
        self.assertEqual(len(found), 1)
        self.assertTrue("thisisatest@company.com" in found)

    def test_credit_card(self):
        """From `https://www.paypalobjects.com/en_AU/vhelp/paypalmanager_help/credit_card_numbers.htm`
        """
        data = "testing with 4012-8888-8882-1881"
        found = masks.CreditCardMask.find(data)
        print('*********', found, '*********')
        self.assertEqual(len(found), 1)
        self.assertTrue("4012888888881881" in found)
