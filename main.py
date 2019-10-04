import sys
import requests



def CALLJENKINS ( Project, Parameter ):
	requests.get ( "http://localhost:8080/job/{0}/buildWithParameters?token=srivalli_project&Item={1}".format ( Project, Parameter ) )

print "\n\n\n\n", sys.argv, "\n\n\n\n"

if len ( sys.argv ) == 3:
	print  sys.argv[1], sys.argv[2]
else:
	print "please provide atleast one argument"
	exit ( 1 )


BakeryType = sys.argv[1]
Items = sys.argv[2].split ( "," )

if BakeryType == 'Samsung':
	for Item in Items:
		if  Item == 'nandu':
			CALLJENKINS ( 'project_nandu', Item )
		if Item == 'nikhil':
			CALLJENKINS ( 'project_nikhil', Item )
		if Item == 'manikanta':
                        CALLJENKINS ( 'project_a', Item )

elif BakeryType == 'Oppo':
        for Item in Items:
                if  Item == 'nandu':
                        CALLJENKINS ( 'project_nandu', Item )
                if Item == 'nikhil':
                        CALLJENKINS ( 'project_nikhil', Item )
		if Item == 'manikanta':
                        CALLJENKINS ( 'project_b', Item )
elif BakeryType == 'HTC':
        for Item in Items:
                if  Item == 'nandu':
                        CALLJENKINS ( 'project_nandu', Item )
                if Item == 'nikhil':
                        CALLJENKINS ( 'project_nikhil', Item )
		if Item == 'manikanta':
                        CALLJENKINS ( 'project_a', Item )


else:
	print "NOTHING"


