# aws-ec2-instances

This is a CLI program that takes AWS keys and finds all the running EC2 instances in any region associated with those keys. It then takes that information and puts it in a database. The specific information this program pulls is instance id, type, region, state (always "running", in this case), private IP address, public IP address, and the time the instance was launched. Run the program on the command line. You will be prompted for the AWS Access Key and AWS Secret Access Key of the account you want to run. Once you enter them, the program will run and populate the database table with data.

## Getting Started

To use this program, you will need access to AWS and a set of keys to enter. To learn more, visit [AWS](https://aws.amazon.com/). You will also need [boto3](https://boto3.readthedocs.io/en/latest/), which is AWS SDK for Python.

### Prerequisites

* [Python 2.7](https://www.python.org/downloads/)
* [PostgreSQL](https://www.postgresql.org/) - Open source relational database
* [Postico](https://eggerapps.at/postico/) - PostgreSQL client for Mac
* `pip install boto3`
* `pip install psycopg2`

### Installing

Clone or download the repo and run the program in the command line.
Create a database in Postico called 'aws_ec2_db' (or change the name in line 4 of ec2_instances.py).
In ec2_instances.py, change the user and host in line 4 to the appropriate inputs for your system.
