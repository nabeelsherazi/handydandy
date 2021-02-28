# twitter-unfollowers

Gets the people who don't follow you back.

## Setup:

- `pip install tweepy pyyaml`
- Create a new Twitter app: https://apps.twitter.com/app/new
- Generate the needed access tokens by using one of the methods described [here](https://github.com/bear/python-twitter#api) (either use the `get_access_token.py` or generate it via Twitter).
- Fill in config.yaml

## Run:

From command line:
`python twitter-unfollowers.py`

Optional args:
`--ignore-verified` - don't list at verified accounts
`--ignore-threshold N` - don't list accounts with more than N followers
`--save` - save results to a text file

## Why

idk i was curious
