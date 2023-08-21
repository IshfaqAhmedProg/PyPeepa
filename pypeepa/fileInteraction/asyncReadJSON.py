import json
from utils import loggingHandler


async def asyncReadJSON(file_name: str):
    read_data = []
    try:
        with open(file_name, "r") as openfile:
            read_data = json.load(openfile)
    except:
        loggingHandler(log_mssg=f"Error reading JSON file {file_name}")
    return read_data
