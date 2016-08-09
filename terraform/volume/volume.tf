# OpenStack Provider (udaje vezmeme z env)
provider "openstack" {

}

# Chceme volume
resource "openstack_blockstorage_volume_v1" "volume_1" {
  name = "tf-volume"
  size = 1
}
