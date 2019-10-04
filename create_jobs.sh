jenkins-jobs test --config-xml configure_auto_test.yaml -o . 
jenkins-jobs --conf /etc/jenkins_jobs/jenkins_jobs.ini update configure_auto_test.yaml 
jenkins-jobs test --config-xml configure_connected_nodes.yaml -o .
jenkins-jobs --conf /etc/jenkins_jobs/jenkins_jobs.ini update configure_connected_nodes.yaml

