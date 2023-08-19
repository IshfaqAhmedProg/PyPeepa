import os


async def getFilePath(message, endswith=(""), invalid_filetype_message="", folder=True):
    while True:
        file_path = input(message)
        file_path = await sanitizeFilePath(file_path)
        if not folder:
            if file_path.endswith(endswith):
                return file_path
            else:
                print(invalid_filetype_message)
        else:
            return file_path


async def sanitizeFilePath(user_input):
    # Remove leading/trailing whitespaces and quotes from the user input
    user_input = user_input.strip(" '\"")

    # Replace backslashes with forward slashes (for cross-platform compatibility)
    user_input = user_input.replace("\\", "/")

    # Remove any leading './' from the path
    if user_input.startswith("./"):
        user_input = user_input[2:]

    # Get the absolute path to handle relative paths
    sanitized_path = os.path.abspath(user_input)

    return sanitized_path
