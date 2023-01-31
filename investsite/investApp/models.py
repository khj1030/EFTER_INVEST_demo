from django.db import models

# Create your models here.
class userLogin(models.Model):
    user_id = models.CharField(primary_key=True, null=False, max_length=10)
    user_team = models.IntegerField(default=0)
    team1 = models.IntegerField(default=0)
    team2 = models.IntegerField(default=0)
    team4 = models.IntegerField(default=0)
    team3 = models.IntegerField(default=0)
    team5 = models.IntegerField(default=0)
    user_money = models.IntegerField(default=10000000)

    # title = models.CharField(max_length=100)

    class Meta:
        db_table = 'student_id'

class projectDB(models.Model):
    proj_id = models.CharField(primary_key=True, null=False, max_length=2)
    name = models.CharField(null=True, max_length=100)

    class Meta:
        db_table = 'project_id'