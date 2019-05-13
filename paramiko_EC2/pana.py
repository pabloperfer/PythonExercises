###connecting to EC2 instances using paramiko
###use case: deploy a config change in 100 servers
##arguments:
    ###I expect to receive a list with many servers, being this the output of the command 'aws ec2 describe-instances --region eu-west-1' From the file i'll get the public dns name and the key to use.

   ### I expect to receive also the user and the path for the new httpd.conf file


### as poc, I will copy a new version of httpd.conf and restart apache
##needed : pip install cryptography==2.4.2 paramiko

#ejemplo ejecucion python3 pana.py instances.json ec2-user /tmp/httpd.conf


import paramiko,sys,json

if len(sys.argv) < 3:
    print ("args missing")
    sys.exit(1)

Ec2_describe = sys.argv[1]
user = sys.argv[2]
path_httpd = sys.argv[3]
remote_httpd_path = '/tmp/httpd.conf'

try:
    with open(Ec2_describe, "r") as nodes:  ##we parse the file to get the values we need for the ssh connection
        data = json.load(nodes)

        for x in data['Reservations'][0]['Instances']:

            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #Policy for automatically adding the hostname and new host key to the local HostKeys object, and saving it
            ssh_client.connect(hostname=(x['PublicDnsName']),username='ec2-user',key_filename=(x['KeyName']) + ".pem" )

            sftp_client=ssh_client.open_sftp()
            sftp_client.put(path_httpd,remote_httpd_path)
            sftp_client.close()

            stdin, stdout, stderr = ssh_client.exec_command('sudo cp /etc/httpd/conf/httpd.conf /tmp/httpdBAK.conf')
            stdin, stdout, stderr = ssh_client.exec_command('sudo mv /tmp/httpd.conf /etc/httpd/conf/httpd.conf')

            stdin, stdout, stderr = ssh_client.exec_command('sudo systemctl restart httpd')

except paramiko.AuthenticationException:
    print ("Authentication failed when connecting to "  + host)
