from django.db import models


class Talent(models.Model):
    name = models.CharField(default="talent_name",max_length=75)
    level = models.IntegerField(default=1)
    image = models.ImageField(upload_to="talent_images", blank=True, null=True)
    win_rate = models.DecimalField(default=0.00, max_digits=8, decimal_places=2)
    popularity = models.IntegerField(default=0)
    games_played = models.IntegerField(default=0)
    win_total = models.IntegerField(default=0)
    loss_total = models.IntegerField(default=0)
    '''
    ***User's personal stats?***
    user_win_rate = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    user_games_played = models.IntegerField(default=0)
    user_win_total = models.IntegerField(default=0)
    user_loss_total = models.IntegerField(default=0)
    '''

class Hero(models.Model):
    name = models.CharField(default="hero_name",max_length=25)
    image = models.ImageField(upload_to="hero_images", blank=True, null=True)
    win_rate = models.DecimalField(default=0.00, max_digits=8, decimal_places=2)
    popularity = models.IntegerField(default=0)
    ban_rate = models.DecimalField(default=0.00, max_digits=8, decimal_places=2)
    games_played = models.IntegerField(default=0)
    win_total = models.IntegerField(default=0)
    loss_total = models.IntegerField(default=0)

    #talents[#] are One-to-Many lists of talent choices by hero level
    talents_one = models.ForeignKey(Talent, on_delete=models.CASCADE, related_name="level_one_talents")
    talents_four = models.ForeignKey(Talent, on_delete=models.CASCADE, related_name="level_four_talents")
    talents_seven = models.ForeignKey(Talent, on_delete=models.CASCADE, related_name="level_seven_talents")
    talents_ten = models.ForeignKey(Talent, on_delete=models.CASCADE, related_name="level_ten_talents")
    talents_thirteen = models.ForeignKey(Talent, on_delete=models.CASCADE, related_name="level_thirteen_talents")
    talents_sixteen = models.ForeignKey(Talent, on_delete=models.CASCADE, related_name="level_sixteen_talents")
    talents_twenty = models.ForeignKey(Talent, on_delete=models.CASCADE, related_name="level_twenty_talents")
    '''
    ***User's personal stats?***
    user_win_rate = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    user_games_played = models.IntegerField(default=0)
    user_win_total = models.IntegerField(default=0)
    user_loss_total = models.IntegerField(default=0)
    tkdown_max = models.IntegerField(default=0)
    tkdown_min = models.IntegerField(default=0)
    tkdown_avg = models.IntegerField(default=0)
    death_max = models.IntegerField(default=0)
    death_min = models.IntegerField(default=0)
    death_avg = models.IntegerField(default=0)
    kill_max = models.IntegerField(default=0)
    kill_min = models.IntegerField(default=0)
    kill_avg = models.IntegerField(default=0)
    assists_max = models.IntegerField(default=0)
    assists_min = models.IntegerField(default=0)
    assists_avg = models.IntegerField(default=0)
    '''

class Build(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)

    talent_one = models.ForeignKey(Talent, on_delete=models.CASCADE, related_name="level_one_talent")
    talent_four = models.ForeignKey(Talent, on_delete=models.CASCADE, related_name="level_four_talent")
    talent_seven = models.ForeignKey(Talent, on_delete=models.CASCADE, related_name="level_seven_talent")
    talent_ten = models.ForeignKey(Talent, on_delete=models.CASCADE, related_name="level_ten_talent")
    talent_thirteen = models.ForeignKey(Talent, on_delete=models.CASCADE, related_name="level_thirteen_talent")
    talent_sixteen = models.ForeignKey(Talent, on_delete=models.CASCADE, related_name="level_sixteen_talent")
    talent_twenty = models.ForeignKey(Talent, on_delete=models.CASCADE, related_name="level_twenty_talent")

    games_played = models.IntegerField(default=0)
    win_total = models.IntegerField(default=0)
    loss_total = models.IntegerField(default=0)
    win_chance = models.DecimalField(default=0.00, max_digits=8, decimal_places=2)
    '''
    ***User's personal stats?***
    user_win_rate = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    user_games_played = models.IntegerField(default=0)
    user_win_total = models.IntegerField(default=0)
    user_loss_total = models.IntegerField(default=0)
    '''