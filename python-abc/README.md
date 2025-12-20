# Python Abstract Classes Project

## Description

This project demonstrates the use of **Abstract Base Classes (ABC)** in Python.  
It contains examples of creating abstract classes and enforcing subclasses to implement specific methods.

---

## Tasks

### Task 0: Abstract Animal Class and Subclasses

- **Abstract class** `Animal` with an abstract method `sound`.
- **Subclasses**:
  - `Dog` → implements `sound()` and returns `"Bark"`
  - `Cat` → implements `sound()` and returns `"Meow"`
- Attempting to instantiate `Animal()` directly raises `TypeError`.

---

## Files

| File | Description |
|------|-------------|
| `task_00_abc.py` | Contains the abstract class `Animal` and its subclasses `Dog` and `Cat`. |
| `main_00_abc.py` | Test script to demonstrate the functionality of `Dog`, `Cat`, and `Animal`. |

---

## Usage

```bash
# Make files executable
chmod +x task_00_abc.py main_00_abc.py

# Run the test script
./main.py

