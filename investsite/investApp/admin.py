from django.contrib import admin

# Register your models here.
from .models import userLogin, projectDB

class Lay_userLogin(admin.ModelAdmin):
    list_display = ('user_id','user_team','team1','team2','team3','team4','team5','user_money')
admin.site.register(userLogin,Lay_userLogin)

class Lay_projName(admin.ModelAdmin):
    list_display = ('proj_id','name')
admin.site.register(projectDB,Lay_projName)
