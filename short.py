import jenkins


def create_job(server, path):
    server.get_job_config(path)
    server.build_job(path)
    server.delete_job(path)

server = jenkins.Jenkins('http://localhost:8080')
print (server.jobs_count())