import subprocess
import vagrant
from vagrant import compat
import yaml

TD = None

print("++++++++++++++++++++++++++++++++ Creating Instances ++++++++++++++++++++++++++++++++++")
v = vagrant.Vagrant()
v.up()

with open('nodes.yaml', 'r') as f:
    nodes = yaml.load(f)

nodeList = nodes["nodes"]

hosts = {'nodes': ''}

hostinfos = {}

print("++++++++++++++++++++++++++ Preparing Configurations Files +++++++++++++++++++++++++++++")

for key, value in nodeList.iteritems():

 command = "vagrant ssh-config " + value.get(":node_name")

 ssh_config = compat.decode(subprocess.check_output(command, cwd=TD, shell=True))

 hostinfo = ssh_config.splitlines(True)[1]

 hostinfos[key] = hostinfo.strip().split(" ")[1]

hosts['nodes'] = hostinfos

with open('hosts.yml', 'w') as outfile:
    outfile.write( yaml.dump(hosts, default_flow_style=False))

print("++++++++++++++++++++++++++++++++++++++ Finished +++++++++++++++++++++++++++++++++++++++")

