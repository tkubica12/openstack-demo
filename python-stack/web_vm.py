#!/usr/bin/python

from openstack import connection
import os
from bottle import route, run, request

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
    vystup = """<!DOCTYPE html>
             <html>
             <body>
             <form action="vytvor">
             Nazev VM:<br>
             <input type="text" name="nazev" value="nejakejmeno">
             <br><br>
             Flavor:<br>
             <select name="flavor">"""

    for flavor in conn.compute.flavors():
        vystup = vystup + '<option value="{}">{}</option>'.format(flavor.name, flavor.name)
    vystup = vystup + """
             </select>
             <br><br>
             Image:<br>
             <select name="image">"""

    for image in conn.compute.images():
        vystup = vystup + '<option value="{}">{}</option>'.format(image.name, image.name)
    vystup = vystup + """
             </select>
             <br><br>

    Sit:<br>
    <select name="sit">"""

    for sit in conn.network.networks():
        vystup = vystup + '<option value="{}">{}</option>'.format(sit.name, sit.name)
    vystup = vystup + """
             </select>
             <br><br>

             <input type="submit" value="Vytvor">
             </form>

             </body>
             </html>"""
    return vystup

@route('/vytvor')
def vytvor():
    nazev = request.query.nazev
    image = conn.compute.find_image(request.query.image)
    flavor = conn.compute.find_flavor(request.query.flavor)
    network = conn.network.find_network(request.query.sit)
    server = conn.compute.create_server(
        name=nazev, image_id=image.id, flavor_id=flavor.id,
        networks=[{"uuid": network.id}])

    return "<h1>Pozadavek zadan</h1>"

run(host='0.0.0.0', port=7123)
