from abc import ABCMeta, abstractmethod, abstractproperty

# Interface
class Module(object):
    __metaclass__ = ABCMeta
    @abstractproperty
    def name(self): pass
    @abstractproperty
    def out(self): pass
    @abstractmethod
    def run(self): pass