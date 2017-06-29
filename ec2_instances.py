import boto3
import psycopg2

conn = psycopg2.connect('dbname=aws_ec2_db user=nadiamounzih host=/tmp/')

cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS ec2_instances(id serial PRIMARY KEY, instance_id varchar, type varchar, region varchar, state varchar, private_ip_address varchar, public_ip_address varchar, launch_time varchar);')

access_key = raw_input('AWS Access Key ID: ')
secret_key = raw_input('AWS Secret Access Key: ')

client = boto3.client('ec2', aws_access_key_id=access_key,
                      aws_secret_access_key=secret_key)

regions = []
for region in client.describe_regions()['Regions']:
    regions.append(region['RegionName'])


instance_list = []
for region in regions:
    ec2 = boto3.resource('ec2', aws_access_key_id=access_key,
                          aws_secret_access_key=secret_key,
                          region_name=region)
    instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name',
                                               'Values': ['running']}])
    for instance in instances:
        if instance.state["Name"] == "running":
            instance_list.append((instance.id, instance.instance_type, region, instance.state['Name'], instance.private_ip_address, instance.public_ip_address, instance.launch_time))

for instance in instance_list:
    cur.execute('INSERT INTO ec2_instances(instance_id, type, region, state, private_ip_address, public_ip_address, launch_time) VALUES (%s, %s, %s, %s, %s, %s, %s)', (instance[0], instance[1], instance[2], instance[3], instance[4], instance[5], instance[6]))

cur.execute('SELECT * from ec2_instances;')
cur.fetchone()

conn.commit()

cur.close()

conn.close()
