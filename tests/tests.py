import os
import sys

# Calculate the project root directory (parent of tests directory)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)


from pypeepa.debugging import initLogging
from pypeepa import concurrentFutures
from jobs.counting import counting


async def testConcurrentFutures():
    logger = await initLogging("TestingConcurrantFutures")

    tasks = [8000000, 9000000]  # tasks for counting job

    concurrentFutures(counting, tasks, logger=logger)


if __name__ == "__main__":
    import asyncio

    asyncio.run(testConcurrentFutures())
