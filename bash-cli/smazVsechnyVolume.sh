for vol in $(openstack volume list -f value -c ID)
do
   openstack volume delete $vol
done

echo Smazano!
