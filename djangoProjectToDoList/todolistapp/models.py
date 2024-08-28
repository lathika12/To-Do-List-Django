from django.db import models

# Create your models here.
class TodoList(models.Model):
    taskname = models.CharField(max_length=500)
    done = models.BooleanField(default=False)

    def __str__(self):
        if self.done:
            donev = "COMPLETE"
        else:
            donev = "INCOMPLETE"
        return self.taskname + " || " + donev
