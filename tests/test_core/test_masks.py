"""
"""
import unittest

from core.masks import (
    IPMask,
    NamesMask,
    LinkMask,
    CreditCardMask,
    EmailMask,
    PhoneMask
)


class MasksTests(unittest.TestCase):
    """
    """

    def test_local_ip_mask(self) -> None:
        data = "This is a string with IP address 127.0.0.1"
        found = IPMask.find(data)
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0], "127.0.0.1")

    def test_non_local_ip_mask(self) -> None:
        data = "This is a string with non local 172.217.22.14 IP address"
        found = IPMask.find(data)
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0], "172.217.22.14")

    def test_a_few_local_ip_addresses(self) -> None:
        data = "This is a string with a few 172.217.22.14 IP address 127.0.0.1"
        found = IPMask.find(data)
        self.assertEqual(len(found), 2)
        self.assertTrue("172.217.22.14" in found)
        self.assertTrue("127.0.0.1" in found)

    def test_name_without_lastname(self) -> None:
        data = "Adam is going to do some cool shit in this world"
        found = NamesMask.find(data)
        self.assertEqual(len(found), 1)
        self.assertTrue("Adam" in found)

    def test_name_with_lastname(self) -> None:
        data = "Adam Cohen is going to do some cool shit in this world"
        found = NamesMask.find(data)
        self.assertEqual(len(found), 2)
        self.assertTrue("Adam" in found)
        self.assertTrue("Cohen" in found)

    def test_name_with_long_lastname(self) -> None:
        data = "Adam Cohen Hillel is going to do some cool shit in this world"
        found = NamesMask.find(data)
        self.assertEqual(len(found), 2)
        self.assertTrue("Adam" in found)
        self.assertTrue("Cohen Hillel" in found)

    def test_short_link(self) -> None:
        data = "The user clicked on google.com"
        found = LinkMask.find(data)
        self.assertEqual(len(found), 1)
        self.assertTrue("google.com" in found)

    def test_www_link(self) -> None:
        data = "The user clicked on www.google.com"
        found = LinkMask.find(data)
        self.assertEqual(len(found), 1)
        self.assertTrue("www.google.com" in found)

    def test_http_link(self) -> None:
        data = "The user clicked on https://www.google.com"
        found = LinkMask.find(data)
        self.assertEqual(len(found), 1)
        self.assertTrue("https://www.google.com" in found)

    def test_uk_international_phone_number(self) -> None:
        data = "The user called +447831879184"
        found = PhoneMask.find(data)
        self.assertEqual(len(found), 1)
        self.assertTrue("+447831879184" in found)

    def test_us_international_phone_number(self) -> None:
        data = "The user called +12025550196"
        found = PhoneMask.find(data)
        self.assertEqual(len(found), 1)
        self.assertTrue("+12025550196" in found)

    def test_no_international_phone_number(self) -> None:
        data = "The user called 07831879184"
        found = PhoneMask.find(data)
        self.assertEqual(len(found), 1)
        self.assertTrue("07831879184" in found)

    def test_email_gmail(self) -> None:
        data = "testing with thisisatest@gmail.com"
        found = EmailMask.find(data)
        self.assertEqual(len(found), 1)
        self.assertTrue("thisisatest@gmail.com" in found)

    def test_not_known_mail_address(self) -> None:
        data = "testing with thisisatest@company.com"
        found = EmailMask.find(data)
        self.assertEqual(len(found), 1)
        self.assertTrue("thisisatest@company.com" in found)

    def test_credit_card(self) -> None:
        """From `https://www.paypalobjects.com/en_AU/vhelp/paypalmanager_help/credit_card_numbers.htm`
        """
        data = "testing with 4012-8888-8882-1881"
        found = CreditCardMask.find(data)
        self.assertEqual(len(found), 1)
        self.assertTrue("4012-8888-8882-1881" in found)
