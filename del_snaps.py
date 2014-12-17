#!/usr/bin/python
import boto.ec2
import sys
import datetime
if len(sys.argv) < 3 :
  print "usage: del_snap.py <no of days> <volume id>"
  sys.exit() 

conn = boto.ec2.connect_to_region("us-east-1",
      aws_access_key_id='xxxxxxxxxxxxxxxxxxxxxxxxxx',
      aws_secret_access_key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

days = int(sys.argv[1])
ids = str(sys.argv[2])
vols = conn.get_all_volumes(volume_ids=ids)
for i in vols:
   if ( len(i.snapshots()) == 0) :
     continue
   else :
     snaps = i.snapshots()
     for snap in snaps:
       time1 = snap.start_time
       snp_date = datetime.datetime.strptime(time1, '%Y-%m-%dT%H:%M:%S.%fZ')
       start_date = datetime.datetime.today() + datetime.timedelta(-days)
       dt = datetime.datetime.strftime(start_date, '%Y-%m-%dT%H:%M:%S.%fZ')
       if snp_date < start_date :
		print ('{0} greater than 30 days old - {1}. Deleting them').format(snap, snp_date)
		snap.delete()
	     
       else :
		print ("{0} less than 30 days old {1}. So ignoring the snap").format(snap, snp_date)
		continue
