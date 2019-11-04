import sys
import requests



def CALLJENKINS ( Project, Parameter ):
	requests.get ( "http://localhost:8080/jenkins/job/{0}/build?token=slave&Item={1}".format ( Project, Parameter ) )

print "\n\n\n\n", sys.argv, "\n\n\n\n"

if len ( sys.argv ) == 3:
	print  sys.argv[1], sys.argv[2]
else:
	print "please provide atleast one argument"
	exit ( 1 )


Device = sys.argv[1]
Slaves = sys.argv[2].split ( "," )

if Device == 'Samsung':
	for Item in Slaves:
		if  Item == 'nandu':
			CALLJENKINS ( 'node-Nandu', Item )
		if Item == 'nikhil':
			CALLJENKINS ( 'node-Nikhil', Item )
		if Item == 'manikanta':
                        CALLJENKINS ( 'node-Manikanta', Item )
                if Item == 'windows-slave':
                        CALLJENKINS ( 'node-Ravichandra', Item )
                if Item == 'sravya':
                        CALLJENKINS ( 'node-Sravya', Item )

elif Device == 'Oppo':
        for Item in Slaves:
                if  Item == 'nandu':
                        CALLJENKINS ( 'node-Nandu', Item )
                if Item == 'nikhil':
                        CALLJENKINS ( 'node-Nikhil', Item )
                if Item == 'manikanta':
                        CALLJENKINS ( 'node-Manikanta', Item )
                if Item == 'windows-slave':
                        CALLJENKINS ( 'node-Ravichandra', Item )
                if Item == 'sravya':
                        CALLJENKINS ( 'node-Sravya', Item )

elif Device == 'HTC':
        for Item in Slaves:
                if  Item == 'nandu':
                        CALLJENKINS ( 'node-Nandu', Item )
                if Item == 'nikhil':
                        CALLJENKINS ( 'node-Nikhil', Item )
                if Item == 'manikanta':
                        CALLJENKINS ( 'node-Manikanta', Item )
                if Item == 'windows-slave':
                        CALLJENKINS ( 'node-Ravichandra', Item )
                if Item == 'sravya':
                        CALLJENKINS ( 'node-Sravya', Item )
else:
	print "NOTHING"


