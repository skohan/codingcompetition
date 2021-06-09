from django.db import models

from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from problems.models import Problem, InputOutput
# Create your models here.


class Solved(models.Model):
    
    user     = models.ForeignKey(User,   on_delete=models.CASCADE)
    problem  = models.ForeignKey(Problem,on_delete=models.CASCADE)

    cases_running = models.BooleanField(default=False)
    solved   = models.BooleanField(default=False)



    def __str__(self) -> str:
        return "User:{} | Problem:{} | Solved:{}".format(self.user, self.problem, self.solved)