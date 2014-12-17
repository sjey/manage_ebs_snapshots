manage_ebs_snapshots
====================

This scirpt deletes snapshots that are more than the given days.
Usage:
------------------
del_snaps.py <no of days> <volume id>

Note: this script will not delete snapshots that are created by CreateImage action.
