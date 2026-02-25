"""
Coroutine Demo Script
Run this file to see how Python coroutines work.
"""

import asyncio


# -----------------------------
# Runnable Coroutine Example
# -----------------------------
async def order_pizza():
    print("Ordering pizza...")
    await asyncio.sleep(2)   # Simulates waiting time (pause point)
    print("Pizza received!")


# Start the coroutine using the event loop
if __name__ == "__main__":
    asyncio.run(order_pizza())



#  EXPLANATION 


# What is a Coroutine?
#
# A coroutine is:
# - A special function that can pause and resume execution.
# - Useful for handling tasks like network requests, delays,
#   file operations, or anything that involves waiting.
#
# Coroutines help programs run efficiently without blocking
# the entire application.


# How do we define a Coroutine?
#
# Using the keyword:
#
#     async def my_function():
#         ...
#
# Example:
#
#     async def order_pizza():
#         print("Ordering pizza...")
#         await asyncio.sleep(2)
#         print("Pizza received!")


# Explanation of Important Keywords
#
# 1. async def
#    - Declares a coroutine function.
#    - It does NOT run immediately when called.
#
# 2. await
#    - Marks a pause point inside a coroutine.
#    - Allows other tasks to run while waiting.
#
# 3. asyncio.run()
#    - Starts the event loop.
#    - Executes the coroutine.
#    - Required to actually run async code.


# How Execution Works
#
# Step 1: Program starts
# Step 2: asyncio.run(order_pizza()) starts event loop
# Step 3: "Ordering pizza..." prints
# Step 4: Program waits 2 seconds (non-blocking)
# Step 5: "Pizza received!" prints
# Step 6: Program ends


# How User Should Run
#
# After reading this file:
#
#     python coroutine.py
#
# The coroutine will execute.
