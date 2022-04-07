from locust import HttpUser, between, task

class AppUser(HttpUser):
    # The time waiting between 2 task launched
    wait_time = between(1, 5)

    @task(2)
    def index(self):
        self.client.get("/")
    
    # 4 est la ratio, 
    # cette fonction a 2x plus de chance d'être choisi que @task(2)
    @task(4)
    def other(self):
        self.client.get("/other?page=1")