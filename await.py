"""
Await Keyword Demo Script
Run this file to understand how `await` works in Python.
"""

import asyncio



# Runnable Example

async def cook():
    print("Cooking started")
    await asyncio.sleep(3)   # Pause only this coroutine (non-blocking)
    print("Cooking done")


if __name__ == "__main__":
    asyncio.run(cook())



# EXPLANATION 


# What does `await` do?
#
# `await` is used inside a coroutine to:
#
# 1. Suspend (pause) the coroutine temporarily.
# 2. Give control back to the event loop.
# 3. Resume execution when the awaited task is complete.
#
# It allows efficient multitasking without blocking the program.


# IMPORTANT CONCEPT
#
# Code does NOT block the entire program.
#
# Only this coroutine pauses.
#
# That means other tasks can run while waiting.


# Example Explanation
#
# async def cook():
#     print("Cooking started")
#     await asyncio.sleep(3)
#     print("Cooking done")
#
#
# Step-by-step execution:
#
# Step 1: "Cooking started" prints immediately.
# Step 2: await asyncio.sleep(3) pauses this coroutine for 3 seconds.
# Step 3: During the pause, event loop can run other tasks.
# Step 4: After 3 seconds, coroutine resumes.
# Step 5: "Cooking done" prints.


# What is asyncio.sleep()?
#
# It is a non-blocking delay.
#
# Difference from time.sleep():
#
# time.sleep(3)  → blocks entire program ❌
# asyncio.sleep(3) → pauses only coroutine ✅


# Why `await` is Powerful?
#
# It enables:
#
# - Concurrent programs
# - High-performance servers
# - Network applications
# - APIs
# - Web scraping
# - Real-time systems
#
# All without using threads.


# How User Should Run
#
# After reading this file:
#
#     python await.py