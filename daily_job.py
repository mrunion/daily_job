"""
Daily Job
"""

from random import randint

import meetings
import begging
import drupal
import security

def daily_job():
    # Everyone starts out alive...
    alive = True
    day = 0
    while alive:
        day += 1
        print('\nDay %03d\n-----' % day)
        print('Another day dawns, and another line appears on your weary face.')
        
        # The eternal moring meeting looms.....
        print('The morning meeting commences....')
        meetings.morning_meeting()
        
        # There's always a chance Drupal needs an upgrade
        print('You wonder if there are any Drupal upgrades to do....')
        do_drupal_upgrade = randint(1,  5) % 2
        if do_drupal_upgrade:
            print('  There are Drupal upgrades to do! You plead your case for more time....',  end='')
            success = begging.beg_for_time()
            if success:
                drupal.upgrade_drupal()
            else:
                print('  Your pleas fell on deaf ears, so you have to do the upgrade tonight.')
                drupal.upgrade_drupal_after_hours()
        else:
            print('  There were no Drupal upgrades!')
        
        # Do any security updates
        print('You wonder if there are any security issues that needs addressed...')
        is_security_remediation_needed = True
        if is_security_remediation_needed:
            security.remediate_issues()
        
        # Any more meetings today?
        
        
        # Recalculate whether we are living or not....
        alive = randint(0,  20) is not 0
    
    # You're dead
    print('\nAnd so closes your life. You lived %d days.\n' % day)

if __name__ == '__main__':
    daily_job()
