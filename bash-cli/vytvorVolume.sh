for vol in "$@"
do
      openstack volume create $vol --size 1
done
