from prometheus_client import start_http_server, Gauge
import random
import time

curr_req = Gauge('a_myapp_current_req_count', "Current Request")
curr_req_4xx = Gauge('a_myapp_current_req_count_4xx', "4xx Request")
curr_req_5xx = Gauge('a_myapp_current_req_count_5xx', "5xx Request")

def fetch_metric():
    curr_req.set(random.randint(1, 100))
    curr_req_4xx.set(random.randint(0, 10))
    curr_req_5xx.set(random.randint(0, 5))

def run_loop_metrics(time_interval):
    while True:
        fetch_metric()
        time.sleep(time_interval)

def main():
    start_http_server(9130)
    run_loop_metrics(5)


if __name__ == "__main__":
    main()

