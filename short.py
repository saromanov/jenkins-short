import jenkins
import os

def get_builds(server, color):
    jobs = server.get_all_jobs()
    for j in jobs:
        if j['color'] == color:
            print(j['name'])

def get_job_info(server, job):
    return server.get_job_info(job)

def create_job(server, path):
    server.get_job_config(path)
    server.build_job(path)
    server.delete_job(path)

if 'JENKINS_SHORT_USER' not in os.environ:
    raise Exception('user is not defined')
if 'JENKINS_SHORT_PASSWORD' not in os.environ:
    raise Exception('password is not defined')
user = os.environ['JENKINS_SHORT_USER']
password = os.environ['JENKINS_SHORT_PASSWORD']
server = jenkins.Jenkins('http://localhost:8080', user, password)
get_builds(server, 'blue')