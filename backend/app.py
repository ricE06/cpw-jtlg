import typing
from flask import Flask

app = Flask(__name__)  # I think this is right? Should be for single module

@app.route("/")
def index():
    # todo: make the homepage and put it into a html file
    return "<p>Hello, World!</p>" 


@app.route("/challenges/<loc>/<challenge_title>")
def get_challenge(loc: str, challenge_title: str) -> dict[str, str|float]:
    """
    Gets a challenge. 

    The challenge file must exist in `/challenges/<loc>/<challenge_title>.md`.
    If it doesn't exist, a 404 is returned.

    The challenge file must be formatted in the following way:

        # Challenge Title

        ## Description
        < a short description of the challenge > 

        ## Rules
         - < a specific rule / constraint to be obeyed >
         - < another rule >
         - etc.

    Args:
        loc: the name of the location that has this challenge, case-insensitive
        challenge_title: the internal name of the challenge, also case-insensitive
    Returns:
        a dictionary with keys, 
            'challenge', that contains the 
                challenge text and rules in the markdown file as a string
                if the challenge exists, otherwise returns a 404 error code
            'multiplier', a float representing the multiplier of this challenge
                (e.g. 1.5, 2, 3, etc.)
    """
    raise NotImplementedError

@app.route("/all_challenges/<loc>")
def get_all_challenges(loc: str) -> dict[str, list[str]]:
    """
    Gets all challenges associated with a certain location.

    If the location doesn't exist in `/challenges`, returns
    a 404 error code.

    Args:
        loc: the name of the game location, case insensitive
    Returns:
        a dictionary with one key, 'challenges', that contains a
        list of challenge titles as strings
    """
    raise NotImplementedError
