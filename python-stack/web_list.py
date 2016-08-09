#!/usr/bin/python

from openstack import connection
import os
from bottle import route, run

auth_args = {
    'auth_url': os.environ['OS_AUTH_URL'],
    'project_name': os.environ['OS_PROJECT_NAME'],
    'username': os.environ['OS_USERNAME'],
    'password': os.environ['OS_PASSWORD'],
    'user_domain_id': os.environ['OS_USER_DOMAIN_ID'],
    'project_domain_id': os.environ['OS_PROJECT_DOMAIN_ID'],
}
conn = connection.Connection(**auth_args)

@route('/')
def app():
    vystup = "<table><TR><TD>Flavors</TD></TR>"
    for flavor in conn.compute.flavors():
        vystup = vystup + "<TR><TD>" + flavor.name + "</TD></TR>"
    vystup = vystup + "</table>"
    return vystup

run(host='0.0.0.0', port=7123)
