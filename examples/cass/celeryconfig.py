# -*- coding: utf-8 -*-
from cassandra.policies import RoundRobinPolicy

broker_url = 'amqp://guest:guest@localhost:5672//'
result_backend = 'cassandra'

cassandra_servers = ['127.0.0.1']
cassandra_keyspace = 'demo'
cassandra_table = 'celery_jobs_result'
cassandra_auth_provider = 'PlainTextAuthProvider'
cassandra_auth_kwargs = {
    'username': 'cassandra',
    'password': 'cassandra'
}
cassandra_options = {
    'load_balancing_policy': RoundRobinPolicy()
}
cassandra_entry_ttl = 86400

ignore_result = False

worker_concurrency = 4
