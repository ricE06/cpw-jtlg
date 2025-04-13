import typing
import json
from flask import Flask

app = Flask(__name__)  # I think this is right? Should be for single module
challenges_dict = json.load(open("challenges.json", "r"))  # Load the challenges dictionary from the JSON file

@app.route("/")
def index():
    # todo: make the homepage and put it into a html file
    return "<p>Jet The Lag Game, CPW Edition | Backend Server</p>" 


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
    
    # Check input validity
    loc = loc.lower()
    if loc not in challenges_dict:
        return {"error": "Location not found"}, 404
    challenge_title = challenge_title.lower()
    if challenge_title not in challenges_dict[loc]["challenges"]:
        return {"error": "Challenge not found"}, 404
    # Get challenge data
    data = challenges_dict[loc]["challenges"][challenge_title]
    try:
        with open(f"challenges/{challenge_title}.md", "r") as f:
            challenge = f.read()
    except FileNotFoundError:
        return {"error": "Challenge file not found"}, 404
    return {
        "challenge": challenge,
        "multiplier": data["multiplier"],
    }


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
    loc = loc.lower()
    if loc not in challenges_dict:
        return {"error": "Location not found"}, 404
    all_location_challenges = challenges_dict[loc]["challenges"]
    return {
        "challenges": [
            {
                "title": all_location_challenges[challenge_name]["title"],
                "multiplier": all_location_challenges[challenge_name]["multiplier"],
                "slug": challenge_name,
            }
            for challenge_name in all_location_challenges.keys()
        ]
    }

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)