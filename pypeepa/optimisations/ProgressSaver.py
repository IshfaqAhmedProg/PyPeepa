from pypeepa.fileInteraction.asyncReadJSON import asyncReadJSON  # check
from pypeepa.utils.loggingHandler import loggingHandler  # check
from typing import Optional, List, Any
from logging import Logger
import json


class ProgressSaver:
    """
    Saves any kind of state in an array.\n
    @init\n
        @param: `file_name`: Name of the file where the progress states will be saved in.\n
    @func: `initialiseJSONSaver`: Initialise the saver before using.\n
    @func: `saveToJSON`: Append the progress state to an array containing previous states and save to `file_name`.json\n
        @param: `new_data`: Data to save.\n
        @param: `name`: (Optional)If the save state has any name, it will be used for logging.\n
        @param: `logger` (Optional)A logger object to enable logging.\n
    """

    def __init__(self, file_name) -> None:
        self.file_name: str = file_name
        self.saved_data: Optional[List] = None

    async def initialiseJSONSaver(self):
        self.saved_data = await asyncReadJSON(self.file_name)
        return self.saved_data

    def saveToJSON(
        self, new_data: List[Any], name: str = None, logger: Optional[Logger] = None
    ):
        self.saved_data.append(new_data)
        with open(self.file_name, "w+") as completed_output:
            loggingHandler(
                logger, f"Saving file: -> {name}" if name else "Saving file!"
            )
            json.dump(self.saved_data, completed_output)

    def clearJSON(self, logger: Optional[Logger]):
        self.saved_data = []
        with open(self.file_name, "w+") as completed_output:
            loggingHandler(logger, f"Clearing saved progress!")
            json.dump(self.saved_data, completed_output)