class Parent(object):

    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("Child, before parent altered()")
        super(Child, self).altered()
        print("Child, after parent altered()")


dad=Parent()
son=Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

"""will get:
PARENT implicit
PARENT implicit

PARENT override
CHILD override

PARENT altered
CHILD after parent altered"""
