from django.test import TestCase

class ApiSmokeTests(TestCase):
    def test_health(self):
        r = self.client.get('/api/')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json().get('status'), 'ok')

    def test_ping(self):
        r = self.client.get('/api/ping/')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json().get('pong'), 'OK')

    def test_hello(self):
        r = self.client.get('/api/hello/?name=teste')
        self.assertEqual(r.status_code, 200)
        self.assertIn('Olá, teste', r.json().get('hello'))
