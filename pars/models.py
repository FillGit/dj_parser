from django.db import models

# Create your models here.


class Rezult(models.Model):

    value1 = models.PositiveIntegerField()
    value2 = models.PositiveIntegerField()
    team1 = models.CharField(max_length=50, help_text="Team1")
    team2 = models.CharField(max_length=50, help_text="Team2")
    score = models.CharField(max_length=50, help_text="Score")
    

    def save_instance(self, **kwargs):
        instance = kwargs.pop('instance')
        self.id = instance['id']
        self.value1 = instance['value1']
        self.value2 = instance['value1']
        self.save()

    def save(self, *args, **kwargs):
        super(Rezult, self).save(*args, **kwargs)

    def __str__(self):
        return self.id
