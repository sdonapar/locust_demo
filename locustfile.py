from locust import HttpLocust, TaskSet, task
import requests

class WebsiteTasks(TaskSet):
    # We can use the @task decorator as well as the  
    # tasks dict in the same TaskSet
    @task(10)
    def index_page(self):
        self.client.get("/index")

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 15000
