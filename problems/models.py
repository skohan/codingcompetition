from django.db import models
from codingcompetition.settings import INPUT_UPLOAD, OUTPUT_UPLOAD

# Create your models here.


class Problem(models.Model):

    problem_id = models.IntegerField(primary_key=True, auto_created=True)
    title = models.CharField(null=False, max_length=255, default="No Title")
    description = models.TextField(null=False)


    def __str__(self) -> str:
        return "{} {}".format( self.problem_id, self.title)


class InputOutput(models.Model):

    id = models.IntegerField(primary_key=True, auto_created=True)
    
    input_data = models.FileField(null=False, upload_to=INPUT_UPLOAD)
    output_data = models.FileField(null=False, upload_to=OUTPUT_UPLOAD)

    problem_id = models.ForeignKey(Problem, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "{} -- {}".format(self.problem_id, self.id)