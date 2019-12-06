from locust import TaskSequence, HttpLocust, seq_task
import json


class UserBehaviour(TaskSequence):

    def __init__(self, parent):
        self.access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxIiwiZXhwIjoxNTc1NzMxODI5fQ.PlHW2j0P-Nmh4TXkMYq6RGHl_NrNZq3PpeVYIjEnTG8'
        self.url_id = 0
        self.short_url = ''

        super().__init__(parent)

    def on_start(self):
        pass

    @seq_task(5)
    def create_url(self):
        response = self.client.post('/clients/me/urls/', {'longUrl': 'https://example.com/my-very-long-url-3XL6su64dD4Of9OwZS9lg5jOSVxIhgb1JF1JyBlE'},
                                    headers={'Authorization': 'Bearer {}'.format(self.access_token)})
        data = json.loads(response.text)
        print(data['url']['shortUrl'])
        self.short_url = data['url']['shortUrl']
        self.url_id = data['url']['id']

    @seq_task(85)
    def redirect(self):
        print(self.short_url)
        response = self.client.get(self.short_url.replace('localhost:8000', ''))

    @seq_task(10)
    def get_analytics(self):
        response = self.client.get('/analytics/today-reports/?urlId={0}'.format(self.url_id),
                                   headers={'Authorization': 'Bearer {}'.format(self.access_token)})


class WebsiteUser(HttpLocust):
    task_set = UserBehaviour
    min_wait = 5000
    max_wait = 9000
