# -*- coding: utf-8 -*-

import unittest

from noodle.core.model.lib import IPAddress


class TestIPAddress(unittest.TestCase):
    '''Test the IPAddress column type'''

    def setUp(self):
        self.ipaddress = IPAddress()

    def test_ip2int(self):
        '''IPAddress ip2int'''
        addr = self.ipaddress.process_bind_param('1.2.3.4', None)
        self.assertEqual(addr, 16712194)

    def test_int2ip(self):
        '''IPAddress int2ip'''
        addr = self.ipaddress.process_result_value(16712194, None)
        self.assertEqual(addr, '1.2.3.4')
