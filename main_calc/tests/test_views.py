from django.test import LiveServerTestCase
import sqlite3
from main_calc.views import hero_update
from main_calc.models import Hero

class AjaxTest(LiveServerTestCase):
    
    def test_hero_update(self):
        self.connection = sqlite3.connect('db.sqlite3')
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            "select rowid from main_calc_hero order by rowid asc limit 1")
        result = self.cursor.fetchone()
        #print(str(result[0]))


        response = self.client.get(
            '/ajax/hero_update/?hero='+str(result[0])+'&formid=id_ally_select_form1-a_draft', follow=True)
        print(response)
        request = response.wsgi_request

        hero_id = request.GET.get('hero', None)
        print(hero_id)