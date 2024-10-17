# Understand Visitor Design Pattern

This repo is my playground exploring the Visitor pattern

This pattern is ideal for scenarios where you need to perform operations on objects of a structure without modifying their classes.

It’s particularly useful when classes are stable on their main purpose but there need to perform unrelated or unstable operations.

Here are some examples of use cases:
* Extending functionality without modifying classes (e.g., library classes or stable structures).  
* Performing different operations on elements of a complex object structure (e.g., parsing ASTs).
* When you have a set of related classes and need to perform a set of varied but related operations on them.
* Avoiding bloated classes where numerous unrelated methods are added.
* Simplifying the addition of new operations while maintaining backward compatibility.
* Gathering information or performing transformations over a collection of objects with different types (e.g., serialization, validation, or reporting).

I would describe this as a plug and play system. 


# How to run this demo
```python
    #clone repo
    python -m visitor_pattern
```