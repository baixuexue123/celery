#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import time
from random import choice, randint

from faker import Faker

from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.policies import RoundRobinPolicy
from cassandra.query import SimpleStatement

fake = Faker()


def make_row_data(id):
    return id, randint(10, 20), choice(['A', 'B', 'C', 'D']), fake.name()


auth_provider = PlainTextAuthProvider(
    username='cassandra',
    password='cassandra'
)
cluster = Cluster(
    auth_provider=auth_provider,
    load_balancing_policy=RoundRobinPolicy(),
    cql_version='3.4.4',
)
session = cluster.connect('demo')

query = "INSERT INTO test (id, age, class, name) VALUES(%s, %s, %s, %s)"
stmt = SimpleStatement(query, consistency_level=ConsistencyLevel.ONE)


def insert(n):
    for i in range(n):
        row = make_row_data(i)
        print(row)
        session.execute(stmt, row)
        time.sleep(1.0)


pool = []


for i in range(10, 18):
    t = threading.Thread(target=insert, args=(i,))
    t.start()
    pool.append(t)
