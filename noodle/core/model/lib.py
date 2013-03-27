# -*- coding: utf-8 -*-
""""""
#TODO: Check validity of value in process_bind_param
#TODO: Check if value in process_bind_param is maybe already converted


from sqlalchemy.types import TypeDecorator, TypeEngine, BigInteger
from sqlalchemy.dialects.postgresql import INET


class IPAddress(TypeDecorator):
    '''Converts IP addresses from (string) dot-notation to an integer'''

    impl = TypeEngine

    def load_dialect_impl(self, dialect):
        if dialect.name == 'postgresql':
            return dialect.type_descriptor(INET)
        else:
            return dialect.type_descriptor(BigInteger)

    def process_bind_param(self, value, dialect):
        if dialect.name == 'postgresql':
            return value
        else:
            ret = 0
            for val in value.split('.', 3):
                ret *= 255
                ret += int(val)
            return ret

    def process_result_value(self, value, dialect):
        if dialect.name == 'postgresql':
            return value
        else:
            ret = []
            for _ in xrange(4):
                ret.append(str(value % 255))
                value /= 255
            return '.'.join(reversed(ret))
