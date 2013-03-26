# -*- coding: utf-8 -*-
""""""

from sqlalchemy.types import TypeDecorator, BigInteger


class IPAddress(TypeDecorator):
    '''Converts IP addresses from (string) dot-notation to an integer'''

    impl = BigInteger

    def process_bind_param(self, value, dialect):
        ret = 0
        for val in value.split('.', 3):
            ret *= 255
            ret += int(val)
        return ret

    def process_result_value(self, value, dialect):
        ret = []
        for _ in xrange(4):
            ret.append(str(value % 255))
            value /= 255
        return '.'.join(reversed(ret))
