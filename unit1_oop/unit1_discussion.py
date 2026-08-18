"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    device_category = "Network Device"

    def __init__(self, name, ip_address):
        self.name = name
        self.ip_address = ip_address

    def display_info(self):
        return f"Device: {self.name}, IP Address: {self.ip_address}"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    device_type = "Firewall"

    def __init__(self, name, ip_address, security_level, allowed_ports):
        super().__init__(name, ip_address)
        self.security_level = security_level
        self.allowed_ports = allowed_ports

    def display_info(self):
        return (
            f"Firewall: {self.name}, IP Address: {self.ip_address}, "
            f"Security Level: {self.security_level}"
        )

    def display_ports(self):
        return f"Allowed Ports: {self.allowed_ports}"

    # Student-created extension
    def is_port_allowed(self, port):
        return port in self.allowed_ports


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    firewall1 = ChildClass("Main Firewall", "192.168.1.1", "High", [22, 80, 443])
    firewall2 = ChildClass("Backup Firewall", "192.168.1.2", "Medium", [80, 443])

    # Access class variable through the class
    print("Class variable through class:", ChildClass.device_type)

    # Access the same class variable through an object
    print("Class variable through object:", firewall1.device_type)

    # Add an attribute to only one instance
    firewall1.location = "Main Office"

    # Display instance namespaces
    print("Firewall 1 namespace:", firewall1.__dict__)
    print("Firewall 2 namespace:", firewall2.__dict__)

    # Display information about the class namespace
    print("Child class namespace:", ChildClass.__dict__)


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    original = ChildClass(
        "Firewall Copy Test",
        "10.0.0.1",
        "High",
        [22, 80, 443]
    )

    shallow_copy = copy(original)
    deep_copy = deepcopy(original)

    # A shallow copy creates a new object, but nested mutable objects
    # such as lists are still shared with the original object.

    # A deep copy creates a completely independent copy, including
    # nested mutable objects.

    original.allowed_ports.append(8080)

    print("Original object ports:", original.allowed_ports)
    print("Shallow copy ports:", shallow_copy.allowed_ports)
    print("Deep copy ports:", deep_copy.allowed_ports)


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n=== Parent Object ===")
    router = ParentClass("Home Router", "192.168.1.1")
    print(router.display_info())

    print("\n=== Child Object ===")
    firewall = ChildClass(
        "Main Firewall",
        "192.168.1.2",
        "High",
        [22, 80, 443]
    )

    print(firewall.display_info())
    print(firewall.display_ports())

    # Demonstrate the student-created extension
    print("Is port 443 allowed?", firewall.is_port_allowed(443))
    print("Is port 21 allowed?", firewall.is_port_allowed(21))
    # Edge case: test an invalid value that is not a valid port
print("Is invalid port None allowed?", firewall.is_port_allowed(None))

    demonstrate_namespaces()
    demonstrate_copying()
if __name__ == "__main__":
    main()
