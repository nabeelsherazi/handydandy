import argparse
import tweepy
import yaml

parser = argparse.ArgumentParser(
    description="List accounts you follow that don't follow you back")
parser.add_argument("--ignore-verified", action="store_true",
                    help="Don't list accounts you follow that are verified")
parser.add_argument("--save", action="store_true",
                    help="Save accounts that don't follow back in a text file")
parser.add_argument("--ignore-threshold", type=int, metavar="N",
                    help="Don't list accounts you follow with more than N followers")

args = parser.parse_args()

with open("./config.yaml") as f:
    config = yaml.load(f)

try:
    print(f"Checking account {config['account_name']}")

    auth = tweepy.OAuthHandler(
        config['consumer_key'], config['consumer_secret'])

    auth.set_access_token(config['access_token_key'],
                          config['access_token_secret'])

    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True, compression=True)

    user = api.get_user(config["account_name"])
except KeyError as e:
    print(f"Missing value {e} in config.yaml go fix it")
    quit()

print("Processing following".center(80, '-'))

c = tweepy.Cursor(api.friends, skip_status=True)
following = []
i = 0
for f in c.items():
    i += 1
    print(f"Processed {i} following")
    if args.ignore_verified and f.verified:
        continue
    if args.ignore_threshold and f.followers_count > args.ignore_threshold:
        continue
    following.append(f.screen_name)

print("Processing followers".center(80, '-'))

c = tweepy.Cursor(api.followers, skip_status=True)
followers = []
i = 0
for f in c.items():
    i += 1
    print(f"Processed {i} followers")
    followers.append(f.screen_name)

print("Calculating diff".center(80, '-'))

diff = set(following) - set(followers)

print()
print("People who are not following back:")
print()
for user in diff:
    print(user)
print()
if args.save:
    print("Saving to text file")
    with open("./unfollowers.txt", "w") as f:
        f.writelines(diff)
    print("Saved to unfollowers.txt")
