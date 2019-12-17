from django.test import TestCase
from django.db.models import ImageField, DecimalField, IntegerField
from main_calc.models import Hero


def check_field(obj, fieldname):
        field = obj._meta.get_field(fieldname)
        return field

class HeroTest(TestCase):

    def create_hero(
        self, name="Bob", image="hero_images/Cho.jpg", 
        win_rate=30.5, popularity=3, ban_rate=80.5, 
        games_played=2000, win_total=5, loss_total=1995):

        return Hero.objects.create(name=name, image=image, win_rate=win_rate, 
        popularity=popularity, ban_rate=ban_rate, games_played=games_played, 
        win_total=win_total, loss_total=loss_total)


    def test_hero_creation(self):
        hero = self.create_hero()
        imgfield = check_field(hero, 'image')
        win_rfield = check_field(hero, 'win_rate')
        popfield = check_field(hero, 'popularity')
        banfield = check_field(hero, 'ban_rate')
        gpfield = check_field(hero, 'games_played')
        win_tfield = check_field(hero, 'win_total')
        loss_tfield = check_field(hero, 'loss_total')

        self.assertTrue(isinstance(hero, Hero))
        self.assertEqual(hero.__str__(), hero.name)
        self.assertTrue(isinstance(imgfield,ImageField))
        self.assertTrue(isinstance(win_rfield,DecimalField))
        self.assertTrue(isinstance(popfield,IntegerField))
        self.assertTrue(isinstance(banfield,DecimalField))
        self.assertTrue(isinstance(gpfield,IntegerField))
        self.assertTrue(isinstance(win_tfield,IntegerField))
        self.assertTrue(isinstance(loss_tfield,IntegerField))
    
