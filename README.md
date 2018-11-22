# airplaneFacts
Python program that pulls flight data and gives interesting facts from that data. Still a work in progress.

Using the flightradar24 library I was able to pull the flight data and build off of that.

## How to use:
1. Install the required packages
2. Go to https://ipstack.com and make an account to get your api key
3. Copy and paste your API key to the findLocation function
4. Run it
## Issues
1. I think I improperly used flightradar24. Still learning... oops.
2. version2 coming soon
3. Slow loading times.
## Updates as I learn more
1. So, did some digging in the flightradar24 module/package(?) and broke down the request it makes. From here I could see that the get_flights function returns a json... I think... and from there instead of iterating through all of the returned values, I discovered that it runs headers(?) that each correspond to an airplane.
2. I then pulled the headers and pulled the values straight from the headers and with initial testing, it seems to cut down the time in half.
## Extra info
1. Typing in 7 gives you the loading time. Version2 is faster most of the time, sometimes up to 2 seconds faster.
