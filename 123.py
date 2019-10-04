# -*- coding: utf8 -*-

import jenkinsapi
from jenkinsapi.jenkins import Jenkins 
from jenkinsapi.utils.crumb_requester import CrumbRequester

def main():
    pass

crumb=CrumbRequester(username='srivalli', password='oguri@777', baseurl='http://localhost:8080')

jenkins = Jenkins('http://localhost:8080','srivalli','oguri@777',requester=crumb) 

job_name = 'test_job'

job = jenkins[job_name]
# job = jenkins[job_name,'blue','http://localhost:8080/job/test_job']

item = job.invoke()
print 'Building...'

config = job.get_config()

print(config)

item.block_until_complete()

#build = item.get_last_build()

job_name = 'Jenkins_01'
#curl http://192.168.200.133:8080/job/Jenkins_01/buildWithParameters?token=1234&Type=Device
#curl 'http://192.168.200.133:8080/job/Jenkins_01/buildByToken/buildWithParameters?\&token=1234&Type=Device'
#wget 'http://192.168.200.133:8080/job/Jenkins_01/buildByToken?\&token=1234'
#cmd = """curl 'http://192.168.200.133:8080/job/Jenkins_01/build?\&token=1234'"""

#print(Device)


#print 'Last build number was:', build.get.number()


