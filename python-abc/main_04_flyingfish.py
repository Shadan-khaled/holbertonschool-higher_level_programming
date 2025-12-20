#!/usr/bin/env python3
from task_04_flyingfish import Fish, FlyingFish

flying_fish = FlyingFish()
flying_fish.swim()  # The flying fish is swimming!
flying_fish.fly()  # The flying fish is soaring!
flying_fish.habitat()  # The flying fish lives both in water and the sky!

# Optional: check Method Resolution Order (MRO)
print(FlyingFish.mro())
