"""
Security
"""

from random import randint

ISSUES = [
    'You ponder the existential meaning of CSRF, then decide to write the fix in assmebly language.', 
    'You want to buy the entire Security Team a beer -- laced with a laxative! But you just fix the issues and wait for the Publisher\'s Clearing House check to arive.', 
    'You wake up in the middle of the floor wearing a diaper, rocking gently back and forth and asking for the rabbit with the pretty waistcoat to come back with your hairbrush.'
]

def remediate_issues():
    print('  ' + ISSUES[randint(0,  len(ISSUES) - 1)])
