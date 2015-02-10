import boto.ec2
import dateutil.relativedelta
import sys
from boto.exception import EC2ResponseError
from datetime import timedelta, datetime
from dateutil import parser

conn = boto.ec2.connect_to_region("us-east-1",
     aws_access_key_id='xxxxxxxxxxxxxxxxxxxxxxx',
     aws_secret_access_key='xxxxxxxxxxxxxxxxxxxxxxxxxxx'
 )
 
 #list all the snapshots in us-east-1 reion
snaps = conn.get_all_snapshots(owner="self")

#delete the snapshots that are older than 14 days. Handle delete errors if delete fails due to snap being used by amicreation
for snap in snaps:
	limit = datetime.now() - timedelta(days=14)
	if parser.parse(snap.start_time).date() <= limit.date():
		print "deleting" , snap.id
                try:
			conn.delete_snapshot(snap.id)
		except EC2ResponseError as error:
			print ("Could not remove snapshot:",snap.id)
