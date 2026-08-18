# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.

## Implementation Documentation

For this assignment, I created a parent class that represented a network device. The parent class included a class variable for the device category and instance variables for the device name and IP address. I also created a method that displayed information about each network device.

I created a child class that represented a firewall and inherited from the parent class. The child class added a security level and a list of allowed ports. I overrode the display method to provide firewall-specific information and added a method to display the allowed ports.

I demonstrated class and instance namespaces by creating two firewall objects and adding a location attribute to only one of them. I used `__dict__` to display the differences between their instance namespaces and the class namespace.

I also demonstrated shallow and deep copying using the firewall's list of allowed ports. After modifying the original list, the shallow copy reflected the modification because it shared the nested list, while the deep copy remained unchanged.

As my student-created extension, I added the `is_port_allowed()` method. This method checked whether a specific port existed in the firewall's allowed ports list. I tested the program with ports 443 and 21 and verified that the program correctly returned `True` and `False`.
I also tested an edge case by passing None to the is_port_allowed() method. The method returned False because the invalid value was not contained in the list of allowed ports. This demonstrated that the method could handle a missing or invalid value without causing the program to fail.
