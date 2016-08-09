#!/usr/bin/python

from openstack import connection
import os

auth_args = {
    'auth_url': os.environ['OS_AUTH_URL'],
    'project_name': os.environ['OS_PROJECT_NAME'],
    'username': os.environ['OS_USERNAME'],
    'password': os.environ['OS_PASSWORD'],
    'user_domain_id': os.environ['OS_USER_DOMAIN_ID'],
    'project_domain_id': os.environ['OS_PROJECT_DOMAIN_ID'],
}
conn = connection.Connection(**auth_args)

print "Servery:"
print "--------"
for server in conn.compute.servers():
    print server.name

print
print "Image:"
print "------"
for image in conn.compute.images():
    print image.name

print
print "Flavor:"
print "-------"
for flavor in conn.compute.flavors():
    print flavor.name
