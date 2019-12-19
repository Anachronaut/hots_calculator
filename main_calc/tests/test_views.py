from django.test import TransactionTestCase
import sqlite3
from main_calc.views import hero_update
from main_calc.models import Hero

class AjaxTest(TransactionTestCase):
    
    fixtures = ['db.json']

    def test_hero_update(self):

        
        self.connection = sqlite3.connect('db.sqlite3')
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            "select rowid from main_calc_hero order by rowid asc limit 1")
        result = self.cursor.fetchone()

        response = self.client.get(
            '/ajax/hero_update/?hero='+str(result[0])+'&formid=id_ally_select_form1-a_draft', follow=True)
        request = response.wsgi_request

        self.assertGreater(len(response.content), 10)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], "application/json")