from django.test import TestCase
from django.db.models import ImageField, DecimalField, IntegerField, CharField
from main_calc.models import Hero


def check_field(obj, fieldname):
        field = obj._meta.get_field(fieldname)
        return field

class HeroTest(TestCase):

    def create_hero(self, 
        name, image, win_rate, popularity, ban_rate, 
        games_played, win_total, loss_total, ally_1, ally_1_win, 
        enemy_1, enemy_1_win):

        return Hero.objects.create(name=name, image=image, win_rate=win_rate, 
        popularity=popularity, ban_rate=ban_rate, games_played=games_played, 
        win_total=win_total, loss_total=loss_total, ally_1=ally_1, 
        ally_1_win=ally_1_win, enemy_1=enemy_1, enemy_1_win=enemy_1_win)


    def test_hero_creation_correct(self):
        hero = self.create_hero("Bob","hero_images/Cho.jpg", 30.5, 3, 80.5, 
        2000, 5, 1995, 'Steve', 50.05, 'Tom', 25.50)
        imgfield = check_field(hero, 'image')
        win_rfield = check_field(hero, 'win_rate')
        popfield = check_field(hero, 'popularity')
        banfield = check_field(hero, 'ban_rate')
        gpfield = check_field(hero, 'games_played')
        win_tfield = check_field(hero, 'win_total')
        loss_tfield = check_field(hero, 'loss_total')
        a1field = check_field(hero, 'ally_1')
        a1_wfield = check_field(hero, 'ally_1_win')
        e1field = check_field(hero, 'enemy_1')
        e1_wfield = check_field(hero, 'enemy_1_win')

        self.assertTrue(isinstance(hero, Hero))
        self.assertEqual(hero.__str__(), hero.name)
        self.assertTrue(isinstance(imgfield, ImageField))
        self.assertTrue(isinstance(win_rfield, DecimalField))
        self.assertTrue(isinstance(popfield, IntegerField))
        self.assertTrue(isinstance(banfield, DecimalField))
        self.assertTrue(isinstance(gpfield, IntegerField))
        self.assertTrue(isinstance(win_tfield, IntegerField))
        self.assertTrue(isinstance(loss_tfield, IntegerField))
        self.assertTrue(isinstance(a1field, CharField))
        self.assertTrue(isinstance(a1_wfield, DecimalField))
        self.assertTrue(isinstance(e1field, CharField))
        self.assertTrue(isinstance(e1_wfield, DecimalField))


    def test_hero_content_length(self):
        hero = self.create_hero("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "hero_images/Cho.jpg", 3320.50456, 3, 8224.34456, 
        2000, 5, 1995, 'Steve', 50.05, 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ', 
        2533.502334)
        name = check_field(hero, 'name')
        win_rfield = check_field(hero, 'win_rate')
        banfield = check_field(hero, 'ban_rate')
        a1field = check_field(hero, 'ally_1')
        a1_wfield = check_field(hero, 'ally_1_win')
        e1field = check_field(hero, 'enemy_1')
        e1_wfield = check_field(hero, 'enemy_1_win')

        self.assertFalse(len(hero.name) <= name.max_length)
        self.assertFalse(len(str(hero.win_rate).replace('.', '')) <= win_rfield.max_digits)
        self.assertFalse(len(str(hero.ban_rate).replace('.', '')) <= banfield.max_digits)
        self.assertTrue(len(hero.ally_1) <= a1field.max_length)
        self.assertTrue(len(str(hero.ally_1_win).replace('.', '')) <= a1_wfield.max_digits)
        self.assertFalse(len(hero.enemy_1) <= e1field.max_length)
        self.assertFalse(len(str(hero.enemy_1_win).replace('.', '')) <= e1_wfield.max_digits)
    
    
    def test_hero_image_format(self):
        hero1 = self.create_hero("Bob","hero_imgs/Cho.png", 30.5, 3, 80.5, 
        2000, 5, 1995, 'Steve', 50.05, 'Tom', 25.50)

        self.assertNotEqual(str(hero1.image).split('/')[0], 'hero_images')
        self.assertNotEqual(str(hero1.image)[-4:], '.jpg')

        hero2 = self.create_hero("Bob","hero_images/Cho.jpg", 30.5, 3, 80.5, 
        2000, 5, 1995, 'Steve', 50.05, 'Tom', 25.50)

        self.assertEqual(str(hero2.image).split('/')[0], 'hero_images')
        self.assertEqual(str(hero2.image)[-4:], '.jpg')