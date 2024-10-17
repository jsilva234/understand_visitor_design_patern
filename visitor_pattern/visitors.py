import json
from abc import abstractmethod, ABC


class VisitableModel(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class Visitor(ABC):
    @abstractmethod
    def visit_foo(self, foo):
        pass

    @abstractmethod
    def visit_bar(self, bar):
        pass


class JsonExporterVisitor(Visitor):
    def __init__(self):
        self.data = {}

    def visit_foo(self, foo):
        self.data['Foo'] = {"value": foo.get_value()}

    def visit_bar(self, bar):
        self.data['Bar'] = {
            "name": bar.get_name(),
            "quantity": bar.get_quantity()
        }

    def export(self):
        return json.dumps(self.data, indent=2)