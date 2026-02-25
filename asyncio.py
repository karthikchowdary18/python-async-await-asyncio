"""
Asyncio Tasks Demo Script
Run this file to understand create_task() and concurrent execution.
"""

import asyncio



# Runnable Example
async def order(food, time):
    print(f"Ordering {food}")
    await asyncio.sleep(time)
    print(f"{food} received!")


async def main():
    # Creating tasks (they start running immediately)
    t1 = asyncio.create_task(order("Pizza", 5))
    t2 = asyncio.create_task(order("Burger", 3))

    # Wait for tasks to finish
    await t1
    await t2


if __name__ == "__main__":
    asyncio.run(main())



#  EXPLANATION 


# What is asyncio.create_task()?
#
# asyncio.create_task() schedules a coroutine to run concurrently.
#
# It immediately registers the coroutine with the event loop
# and allows it to run in the background.
#
# Example:
#
#     task = asyncio.create_task(my_coroutine())
#
# The task starts running without waiting.


# What is asyncio.gather()?
#
# asyncio.gather() runs multiple coroutines together and waits
# until ALL of them complete.
#
# Example:
#
#     await asyncio.gather(task1(), task2(), task3())
#
# It is useful when you want results from multiple tasks.


# Running Multiple Tasks Concurrently
#
# Concurrent means tasks run during the same time period,
# not one after another.
#
# Example:
#
# Pizza → 5 seconds
# Burger → 3 seconds
#
# Sequential execution:
#     5 + 3 = 8 seconds ❌
#
# Concurrent execution:
#     max(5, 3) = 5 seconds ✅


# Code Explanation
#
# t1 = asyncio.create_task(order("Pizza", 5))
# t2 = asyncio.create_task(order("Burger", 3))
#
# Both tasks start immediately.
#
# await t1
# await t2
#
# We wait until both tasks finish.


# create_task() vs gather()
#
# create_task():
#     - Gives more control over tasks
#     - Can await individually
#     - Can cancel tasks
#
# gather():
#     - Runs multiple tasks together
#     - Waits for all automatically
#     - Simpler for many coroutines


# Alternative Using gather()
#
# async def main():
#     await asyncio.gather(
#         order("Pizza", 5),
#         order("Burger", 3)
#     )


# How User Should Run
#
# After reading this file:
#
#     python asyncio.py
