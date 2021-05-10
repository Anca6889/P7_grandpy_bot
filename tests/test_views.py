from flask_testing import TestCase
from app import views

class TestViews(TestCase):

    render_templates = False

    def create_app(self):

        from app.views import app
        app.config['TESTING'] = True
        return app

    def test_return_index_template(self): # REQUIRE BLINKER LIBRARY TO WORK

        response = self.client.get("/")
        assert response.status_code == 200
        self.assert_template_used('index.html')


    def test_assert_not_process_the_template(self):
        response = self.client.get("/")
        assert b"" == response.data

    def test_answer(self, monkeypatch):

        def mock_request_form(*args, **kwargs):
            pass

        def mock_class_Parser__init__(*args, **kwargs):
            pass
        
        def mock_class_Request__init__(self):
            self.wiki_result = "a fake text"
            self.lat = "666"
            self.lng = "999"
        
        monkeypatch.setattr("app.views.flask.request", mock_request_form)
        monkeypatch.setattr("app.parser.Parser.__init__",
                            mock_class_Parser__init__)
        monkeypatch.setattr("app.requester.Request.__init__",
                            mock_class_Request__init__)

        result = views.send_answer()
        assert result == "?"
