from django.db import models

from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from problems.models import Problem
from datetime import datetime
# Create your models here.


class Solved(models.Model):
    
    user     = models.ForeignKey(User,   on_delete=models.CASCADE)
    problem  = models.ForeignKey(Problem,on_delete=models.CASCADE)

    cases_running   = models.BooleanField(default=False) # we tried to do hackerrank like live test cases status, but i guess we need websocket for that
    solved          = models.BooleanField(default=False)
    score           = models.IntegerField(default=0)
    date            = models.DateField(auto_now_add=True)



    def __str__(self) -> str:
        return "User:{} | Problem:{} | Solved:{}".format(self.user, self.problem, self.solved)