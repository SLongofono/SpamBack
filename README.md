# SpamBack
This is a little demo of how to use the Twilio API to make a simple call.
Running this script periodically via cron allows you to place the call over
and over.  The demo file is a recording of Rick Astley's classic "Never gonna
give you up".

Note that you need to actually set up a billable account to make calls.  You can
test this out on your own number for free.

# Quick Setup
0. Install twilio: ```sudo pip install twilio```
1. Clone this repo on a computer that will stay on
2. [Set up your Twilio dev account here](https://www.twilio.com/)
3. Copy the xml file to somewhere publicly accessible.  For example, your personal website or blog.
4. Consult the Twilio fees page to plan out what revenge is worth to you.  Add monies accordingly.
5. Setup a cron job to run your script 'callem.py' at intervals throughout the day.  Alternately, adjust the outer for loop to run it for a predetermined number of iterations.  With 10 numbers to call, you do the whole list plus wait times in 15 minutes, or about 96 iterations per day.
