from django.db import models

# Create your models here.


class Problem(models.Model):

    problem_id = models.IntegerField(primary_key=True, auto_created=True)
    title = models.CharField(null=False, max_length=255, default="No Title")
    description = models.TextField(null=False)


    def __str__(self) -> str:
        return "{} {}".format( self.problem_id, self.title)


class InputOutput(models.Model):

    id = models.IntegerField(primary_key=True, auto_created=True)
    
    input_data = models.TextField(null=False)
    output_data = models.TextField(null=False)

    problem_id = models.ForeignKey(Problem, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "{} -- {}".format(self.problem_id, self.id)