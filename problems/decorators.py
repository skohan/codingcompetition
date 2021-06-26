from datetime import datetime

from django.shortcuts import redirect
from codingcompetition.settings import contest_start_time

def contest_timing_handler(view_func):
    '''
        Redirects to landing page if the contest has not started
    '''

    def wrapper(request, *args, **kwargs):
        current_time = datetime.now

        if current_time < contest_start_time:
            return redirect('landing_page')

        # if current_time <= contest_end_time:
        #     return view_func(*args, **kwargs)

        # we want to let user solves even if the contest is over
        return view_func(request, *args, **kwargs)

    return wrapper
