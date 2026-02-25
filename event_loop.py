"""
Event Loop Demo Script
Run this file to understand how the asyncio event loop works.
"""

import asyncio



# Runnable Example

async def task1():
    print("Task 1 start")
    await asyncio.sleep(2)
    print("Task 1 end")


async def task2():
    print("Task 2 start")
    await asyncio.sleep(1)
    print("Task 2 end")


async def main():
    # Run both tasks concurrently
    await asyncio.gather(task1(), task2())


if __name__ == "__main__":
    asyncio.run(main())



# EXPLANATION 

# What is an Event Loop?
#
# The event loop is the core engine of asyncio.
#
# It:
# - Starts coroutines
# - Switches between them
# - Resumes them when they are ready
# - Manages all asynchronous tasks
#
# Without the event loop, async code will NOT run.


# Simple Analogy
#
# Think of the event loop as:
#
#  A smart waiter handling multiple tables.
#
# Instead of waiting at one table for food to cook,
# the waiter serves other tables and returns when food is ready.
#
# This makes everything faster and efficient.


# Code Explanation
#
# async def task1():
#     print("Task 1 start")
#     await asyncio.sleep(2)
#     print("Task 1 end")
#
# async def task2():
#     print("Task 2 start")
#     await asyncio.sleep(1)
#     print("Task 2 end")
#
# async def main():
#     await asyncio.gather(task1(), task2())
#
# asyncio.run(main())
#
#
# Step-by-Step Execution:
#
# 1. asyncio.run(main()) starts the event loop.
# 2. main() schedules task1 and task2 together.
# 3. Both tasks start running.
# 4. task2 finishes first (1 second).
# 5. task1 finishes later (2 seconds).
# 6. Program ends.


# Important Concept: Concurrency
#
# Tasks run concurrently (not sequentially).
#
# Sequential time:
#     2 sec + 1 sec = 3 sec (wrong)
#
# Concurrent time:
#     max(2 sec, 1 sec) = 2 sec (right)


# What is asyncio.gather()?
#
# It runs multiple coroutines at the same time and waits
# until all of them are finished.


# How User Should Run
#
# After reading this file:
#
#     python event_loop.py
