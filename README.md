manage_ebs_snapshots
====================
A simple script to manage snapshots and cycle the older ones.

This scirpt deletes snapshots that are older than the given days.

Usage:
------------------
del_snaps.py \<no of days\> \<volume id\>

Eg:
del_snaps.py 20 vol-xxxxxxxxx

The above command will delete snapshots that are older than 20 days for vol-xxxxxxxxx

Note: 
* If no. of days not passed to the script while deleting, it will take 30 days as default and deletes 30 days old snapshots.
* this script will not delete snapshots that are created by CreateImage action.
