def make_instance(cls):
    """Return a new object instance"""
    def get_value(name):
        if name in attributes:
            return attributes[name]
        else:
            value = cls['get'](name)
            return bind_method(value, instance)
    def set_value(name, value):
        attributes[name] = value
    attributes = {}
    instance = {'get': get_value, 'set': set_value}
    return instance
    
def bind_method(value, instance):
    """Return a bound method if value is callable, or value otherwise"""
    if callable(value):
        def method(*args):
            return value(instance, *args)
        return method
    else:
        return value
        
def init_instance(cls, *args):
    """Return a new object with type cls, initialized with args"""
    instance = make_instance(cls)
    init = cls['get']('__init__')
    if init:
        init(instance, *args)
    return instance
        
def make_class(attributes, base_class=None):
    """Return a new class, which is a dispatch dictionary"""
    def get_value(name):
        if name in attributes:
            return attributes[name]
        elif base_class is not None:
            return base_class['get'](name)
    def set_value(name, value):
        attributes[name] = value
    def new(*args):
        return init_instance(cls, *args)
    cls = {'get': get_value, 'set': set_value, 'new': new}
    return cls
   
# Let's implement a real class    
def make_account_class():
    """Let's test the implementation"""
    interest = 0.02
    def __init__(self, account_holder):
        self['set']('holder', account_holder)
        self['set']('balance', 0)
    def deposit(self, amount):
        new_balance = self['get']('balance') + amount
        self['set']('balance', new_balance)
        return self['get']('balance')
    def withdraw(self, amount):
        balance = self['get']('balance')
        if amount > balance:
            return "Insufficient funds"
        self['set']('balance', balance - amount)
        return self['get']('balance')
    return make_class(locals())
    
# Let's implement inheritance
def make_checking_account_class():
    interest = 0.01
    withdraw_fee = 1
    def withdraw(self, amount):
        fee = self['get']('withdraw_fee')
        return Account['get']('withdraw')(self, amount + fee)
    return make_class(locals(), Account)
    
Account = make_account_class()
CheckingAccount = make_checking_account_class()
    
