from visitor_pattern.models import Bar, Foo
from visitor_pattern.visitors import JsonExporterVisitor

items = [Foo(value="foo"), Bar(name="bar", quantity=10)]
export_json_visitor = JsonExporterVisitor()

for item in items:
    item.accept(export_json_visitor)

print(export_json_visitor.export())