from visitor_pattern.visitors import VisitableModel


class Foo(VisitableModel):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        visitor.visit_foo(self)

    def get_value(self):
        return self.value


class Bar(VisitableModel):
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def accept(self, visitor):
        visitor.visit_bar(self)

    def get_name(self):
        return self.name

    def get_quantity(self):
        return self.quantity