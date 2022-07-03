## This function is used to query a yes no question to the user in the terminal

import sys

def query_yes_stop(question, default=None):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
            It must be "yes" (the default), "no" or None (meaning
            an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    from: https://stackoverflow.com/questions/3041986/apt-command-line-interface-like-yes-no-input
    """
    valid = {"y": True, "stop": False}

    while True:
        sys.stdout.write(question)
        choice = input().lower()
        if choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'y' or 'stop'.\n")

if __name__ == "__main__":
    for i in range(0,5):
        proceed = query_yes_stop(question="This is a test question: ")
        print(i)
        if not proceed:
            break
