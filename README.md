manage_ebs_snapshots
====================
A simple script to manage snapshots and cycle the older ones.

This scirpt deletes snapshots that are older than the given days.

Usage:
------------------
del_snaps.py -c delete or create -d \<no of days\>  -v \<volume id\>

Eg to delete snapshot:
del_snaps.py -c delete -d 20 -v vol-xxxxxxxxx

The above command will delete snapshots that are older than 20 days for vol-xxxxxxxxx

Note: 
* If no. of days not passed to the script while deleting, it will take 30 days as default and deletes 30 days old snapshots.
* this script will not delete snapshots that are created by CreateImage action.
