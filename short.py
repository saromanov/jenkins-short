import jenkins
import os

def create_job(server, path):
    server.get_job_config(path)
    server.build_job(path)
    server.delete_job(path)

if 'JENKINS_SHORT_USER' not in os.environ:
    raise Exception('user is not defined')
if 'JENKINS_SHORT_USER' not in os.environ:
    raise Exception('password is not defined')
user = os.environ['JENKINS_SHORT_USER']
password = os.environ['JENKINS_SHORT_PASSWORD']
server = jenkins.Jenkins('http://localhost:8080', user, password)
print (server.jobs_count())