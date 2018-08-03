"""
Drupal
"""

from random import randint

GOTCHAS = [
    'and find the upgrade went smoothly.', 
    'over and over and it still times out before finishing because everyone is flooding the server.', 
    'and install it -- but realize it crashes and you forgot to back up the database first.', 
    'but weren\'t paying close enough attention, so you downloaded malware and have to spend the next few hours rebuilding your laptop.',
    'then come to the realization that this is no way to live. You install Django and pretend nothing ever happened.'
]

def _do_drupal_upgrade(leader='You download the new Drupal'):
    print('  ' + leader + ' ' + GOTCHAS[randint(0,  len(GOTCHAS) - 1)])

def upgrade_drupal():
    _do_drupal_upgrade()

def upgrade_drupal_after_hours():
    _do_drupal_upgrade(leader='You come home, fall exhausted into your chair, '
                       'start eating a cold sandwich you bought on the way home '
                       '(and sat on). You power on your computer and download the '
                       'new Drupal')
