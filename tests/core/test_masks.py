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
        self.assertTrue("127.0.01" in found)

    def test_name_without_lastname(self):
        pass

    def test_name_with_lastname(self):
        pass

    def test_name_wit_long_lastname(self):
        pass

    def test_www_link(self):
        pass

    def test_uk_phone_number(self):
        pass

    def test_us_phone_number(self):
        pass

    def test_no_zone_phone_number(self):
        pass

    def test_name_without_lastname(self):
        pass

    def test_name_without_lastname(self):
        pass

    def test_name_without_lastname(self):
        pass

    def test_email_gmail(self):
        pass

    def test_not_known_mail_address(self):
        pass

    def test_credit_card(self):
        pass
