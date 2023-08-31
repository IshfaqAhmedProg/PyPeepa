import os
import sys

# Calculate the project root directory (parent of tests directory)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from pypeepa import (
    askSelectRangeQuestion,
)


async def askrange():
    arr = ["first", "second", "third"]
    ans = askSelectRangeQuestion("select", 1, len(arr))
    print(ans)


if __name__ == "__main__":
    import asyncio

    asyncio.run(askrange())
