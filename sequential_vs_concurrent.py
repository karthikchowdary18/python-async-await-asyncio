"""
Sequential vs Concurrent Execution Demo
Run this file to compare blocking code vs async code.
"""

import time
import asyncio



# Blocking (Sequential) Version


def blocking_order(food, time_to_wait):
    print(f"Ordering {food}")
    time.sleep(time_to_wait)   # Blocks entire program
    print(f"{food} received!")


def run_blocking():
    print("\n--- Blocking Version Start ---")
    start = time.time()

    blocking_order("Pizza", 5)
    blocking_order("Burger", 3)

    end = time.time()
    print(f"Blocking Total Time: {round(end - start, 2)} seconds")



# Async (Concurrent) Version


async def async_order(food, time_to_wait):
    print(f"Ordering {food}")
    await asyncio.sleep(time_to_wait)   # Non-blocking pause
    print(f"{food} received!")


async def run_async():
    print("\n--- Async Version Start ---")
    start = time.time()

    await asyncio.gather(
        async_order("Pizza", 5),
        async_order("Burger", 3)
    )

    end = time.time()
    print(f"Async Total Time: {round(end - start, 2)} seconds")



# Main Execution


if __name__ == "__main__":
    run_blocking()
    asyncio.run(run_async())

#  EXPLANATION 


# What is Sequential Execution?
#
# Tasks run one after another.
#
# Pizza → wait 5 sec
# Burger → wait 3 sec
#
# Total time = 8 seconds


# Why Blocking Happens?
#
# time.sleep() blocks the entire program.
#
# Nothing else can run during sleep.


# What is Concurrent Execution?
#
# Tasks run during the same time period using async.
#
# Pizza → 5 sec
# Burger → 3 sec
#
# Total time = 5 seconds (maximum time, not sum)


# Why Async is Faster?
#
# await asyncio.sleep() does NOT block the program.
#
# It pauses only the coroutine and allows other tasks
# to execute.


# Key Difference
#
# Blocking:
#     time.sleep()
#     Stops entire program ❌
#
# Async:
#     await asyncio.sleep()
#     Stops only coroutine ✅


# Real-World Analogy
#
# Blocking:
#     One chef cooking orders one by one.
#
# Async:
#     Multiple chefs cooking at the same time.


# How User Should Run
#
# After reading this file:
#
#     python sequential_vs_concurrent.py
