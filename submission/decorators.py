from datetime import datetime
from codingcompetition.settings import contest_start_time, contest_end_time

def contest_is_over():
    '''
        Returns true if it's over
    '''
    current_time = datetime.now

    if current_time < contest_start_time or  current_time > contest_end_time:
        return True
    
    return False

