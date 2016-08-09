# OpenStack Provider (udaje vezmeme z env)
provider "openstack" {

}

# Necht existuje Security Group
resource "openstack_compute_secgroup_v2" "secgroup_1" {
  name = "tf-pravidla"
  description = "Moje TF Security Group"
  rule {
    from_port = 22
    to_port = 22
    ip_protocol = "tcp"
    cidr = "0.0.0.0/0"
  }
  rule {
    from_port = 80
    to_port = 80
    ip_protocol = "tcp"
    cidr = "0.0.0.0/0"
  }
  rule {
    from_port = 443
    to_port = 443
    ip_protocol = "tcp"
    cidr = "0.0.0.0/0"
  }
}

# Necht existuje sit
resource "openstack_networking_network_v2" "network_1" {
  name = "tf-net"
  admin_state_up = "true"
}

# Necht existuje subnet
resource "openstack_networking_subnet_v2" "subnet_1" {
  name = "tf-sub"
  network_id = "${openstack_networking_network_v2.network_1.id}"
  cidr = "192.168.79.0/24"
  ip_version = 4
}

# Necht existuje router
resource "openstack_networking_router_v2" "router_1" {
  name = "tf-router"
  external_gateway = "d4712d32-e929-4c20-9b9c-fe9fe66b85f6"
}

# Necht existuje interface routeru pripojujici sit
resource "openstack_networking_router_interface_v2" "router_interface_1" {
  router_id = "${openstack_networking_router_v2.router_1.id}"
  subnet_id = "${openstack_networking_subnet_v2.subnet_1.id}"
}

# Necht existuje prvni server
resource "openstack_compute_instance_v2" "server1" {
  name = "tf-server1"
  image_name = "Cirros"
  flavor_name = "m1.tiny"
  security_groups = ["${openstack_compute_secgroup_v2.secgroup_1.name}"]

  network {
    uuid = "${openstack_networking_network_v2.network_1.id}"
  }
}

# Necht existuje druhy server
resource "openstack_compute_instance_v2" "server2" {
  name = "tf-server2"
  image_name = "Cirros"
  flavor_name = "m1.tiny"
  security_groups = ["${openstack_compute_secgroup_v2.secgroup_1.name}"]
  network {
    uuid = "${openstack_networking_network_v2.network_1.id}"
  }
}
