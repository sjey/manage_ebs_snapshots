#!/usr/bin/python
import boto.ec2
import sys
import datetime
import optparse

conn = boto.ec2.connect_to_region("us-east-1",
      aws_access_key_id='xxxxxxxxxxxxxxxxx',
      aws_secret_access_key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

def deletesnap():
	days = options.d 
	ids = options.v
	print ("Fetching snapshots for vol {0} to delete...").format(ids)
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
					print ("{0} greater than {2} days old - Created date: {1}. Deleting them").format(snap, snp_date, days)
					snap.delete()
	     
       				else :
					print ("{0} less than {2} days old - Created date: {1}. So ignoring the snap").format(snap, snp_date, days)
					continue

def createsnap():
	ids = options.v
	print ("creating snapshot for vol - {0}").format(ids)
	str = "Mysnap-"
	start_date = datetime.datetime.today()
        dt = datetime.datetime.strftime(start_date, '%Y-%m-%dT%H:%M:%S.%fZ')
	desc = str + dt
	snapshot = conn.create_snapshot(ids,desc)
	print ("{0} created").format(snapshot) 

parser = optparse.OptionParser()
parser.add_option('-c', type='choice', choices=['create', 'delete'])
parser.add_option('-v', type='string', action="store")
parser.add_option('-d', type='int', action="store")
options, args = parser.parse_args()
if ( options.c == 'create' ):
	createsnap()
elif ( options.c == 'delete' ):
	if ( not(options.d) ):
		print "Number of days option is left empty. So setting it toi default to 30 days"
		options.d = 30
 	deletesnap()


