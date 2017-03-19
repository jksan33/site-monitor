# site-monitor
A simple program written in Python to monitor a web page for changes. Doesn't work with every single website, but with simpler websites it should be fine. We used Weebly to test.

## Setup
- $ pip install beautifulsoup4
- $ pip install requests
- $ pip install lxml


## Further dependencies (should be installed by default):
- time
- difflib

## Changes
- Will Farris: Site headers specify a user agent, could in theory help with the program detecting false changes due to the target site thinking the bot is on a different web browser. Set the site headers to be used by the requests library, this tells requests to use the same user agent every time it refreshes just in case requests changes user agents for some reason, not sure but this will/should prevent that
