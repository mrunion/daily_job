"""
Meetings
"""

from random import randint

SENTIMENTS = [
    'and ends without any incidents.', 
    'and drags on past its prime.', 
    'and only one person showed up!', 
    'but arguing about the pronounciation of "gif" ensued and everything fell apart after that.'
]

TOPICS = [
    'A meeting about what to meet about next time is called, and nothing is accomplished.', 
    'You are pulled in to a meeting to answer a question about a topic you know nothing about -- so you lie.'
]

def morning_meeting():
    print('  ' + SENTIMENTS[randint(0,  len(SENTIMENTS) - 1)])

def impromptu_meeting():
    print('  ' + TOPICS[randint(0,  len(TOPICS) - 1)])
