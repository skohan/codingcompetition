from problems.models import Problem
from home.models import Solved


def update_user_score(user, problem_id, verdict):

    solved = True
    for v in verdict:
        solved = solved and v[1]

    if not solved:
        return False

    p = Problem.objects.filter(problem_id=problem_id).first()
    sol_entry = Solved.objects.filter(user=user, problem=p).first()

    if not sol_entry: # there is no entry in db, so create one!
        sol_entry = Solved(user = user, problem_id = problem_id, solved = solved, score = p.points)
        sol_entry.save()
        return True

    if sol_entry.solved:
        return True

    sol_entry.solved = solved
    sol_entry.score = p.points
    sol_entry.save()
    
    return True
