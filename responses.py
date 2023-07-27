from helper import check_if_starting


# handles various user messages
def handle_responses(m):
    message = m.lower()

    if message == "!status":
        return check_if_starting()
    if message == "!help":
        return "try !status"
    return "try !help"
