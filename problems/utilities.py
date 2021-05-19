
from django.contrib.auth.models import User, AnonymousUser
from home.models import Solved
from .models import Problem
from itertools import zip_longest

def get_all_problems(user):
	'''
		Returns the zipped list of all problems and flag of if it is solved or not
	'''

	all_problems = Problem.objects.all()
	problems_solved = []
	
	if user.is_authenticated :
		problems_solved = Solved.objects.filter(user = user).all()


	# If there is no entry in ``Solved`` database for given user 
	# OR
	# user is NOT authenticated
	# then the ``zip_longest`` padd the elements of shortest list 
	# to ``None`` and zip them
	# 
	return zip_longest(all_problems, problems_solved)

