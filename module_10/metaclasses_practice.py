import abc


class MetaClassTest(abc.ABCMeta):
    def __new__(cls, name, bases, dct):
        dct['field1'] = 'field1 value'
        dct['field2'] = 'field2 value'
        return super().__new__(cls, name, bases, dct)


class TestClass(metaclass=MetaClassTest):
    pass


print(TestClass.field1)
