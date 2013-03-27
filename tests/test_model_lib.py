# -*- coding: utf-8 -*-

import unittest

from noodle.core.model.lib import IPAddress
from sqlalchemy.dialects.sqlite.base import SQLiteDialect
from sqlalchemy.dialects.postgresql.base import PGDialect


class TestIPAddress(unittest.TestCase):
    '''Test the IPAddress column type'''

    def setUp(self):
        self.ipaddress = IPAddress()

    def test_ip2int(self):
        '''IPAddress ip2int'''
        addr = self.ipaddress.process_bind_param('1.2.3.4', SQLiteDialect)
        self.assertEqual(addr, 16712194)

    def test_int2ip(self):
        '''IPAddress int2ip'''
        addr = self.ipaddress.process_result_value(16712194, SQLiteDialect)
        self.assertEqual(addr, '1.2.3.4')

    def test_ip2int_postgresql(self):
        '''IPAddress ip2int for postgresql'''
        addr = self.ipaddress.process_bind_param('1.2.3.4', PGDialect)
        self.assertEqual(addr, '1.2.3.4')

    def test_int2ip_postgresql(self):
        '''IPAddress int2ip for postgresql'''
        addr = self.ipaddress.process_result_value('1.2.3.4', PGDialect)
        self.assertEqual(addr, '1.2.3.4')
