import flask_testing
import unittest
import requests
import multiprocessing
import time

from app import app

REST_ROOT = 'http://localhost:8943/'


class CustomLiveServer(flask_testing.LiveServerTestCase):
    def _spawn_live_server(self):
        self._process = None
        self.port = self.app.config.get('LIVESERVER_PORT', 8943)

        worker = lambda app, port: app.run(port=port, use_reloader=False, debug=True)

        self._process = multiprocessing.Process(
            target=worker, args=(self.app, self.port)
        )

        self._process.start()
        time.sleep(1)

class AppTestCase(CustomLiveServer):
    render_templates = False

    def create_app(self):
        return app

    def setUp(self):
        #db.create_all()
        pass

    def tearDown(self):
        #db.drop_all()
        pass

class RootRoutesTest(AppTestCase):
    def test_methods(self):
        result = requests.get(REST_ROOT)
        self.assertEqual(result.status_code, 200)
        self.assertTrue('hello' in result.text)

        result = requests.post(REST_ROOT)
        self.assertEqual(result.status_code, 200)

        result = requests.put(REST_ROOT)
        self.assertEqual(result.status_code, 200)

        result = requests.delete(REST_ROOT)
        self.assertEqual(result.status_code, 403)


if __name__ == '__main__':
    unittest.main()

