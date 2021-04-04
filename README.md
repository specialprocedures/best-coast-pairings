# Best Coast Pairings Data
A simple command line script to pull Warhammer 40K data from Best Coast Pairings. This currently seems to work without valid login data.

# Usage
Running ```$ scrape.py``` will pull all available tournament and match data from 2020 on and dump to ```/json``` in the folder in which the script is run.

# Notes
- The script currently pulls tournaments and games from 2020-01-01 onwards. Not passing the "startDate" parameter during the tournament request results in a server error, as does passing an arbitrarily early date (e.g. 1999-01-01).
- The returned json is somewhat trimmed at the game level, as the full response includes unnecessary tournament level data which is returned separately.

# To do
- Tell BCP their database seems to be accessible without a password
- Add CLI arguments for user and password, date range and game type

