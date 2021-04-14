
# Welcome to your CDK Python project!

This is a blank project for Python development with CDK.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```



### This smaple try use build L2 Construct lib.
```bash
cdk diff
---
Stack VPCSTACK
Resources
[+] AWS::EC2::VPC vpc vpc 
[+] AWS::EC2::Subnet subnet_az1 subnetaz1 
[+] AWS::EC2::SecurityGroup sg sg 

Outputs
[+] Output Exports/Output{"Ref":"sg"} ExportsOutputRefsgFF7C4770: {"Value":{"Ref":"sg"},"Export":{"Name":"VPCSTACK:ExportsOutputRefsgFF7C4770"}}
[+] Output Exports/Output{"Ref":"subnetaz1"} ExportsOutputRefsubnetaz14221E4A9: {"Value":{"Ref":"subnetaz1"},"Export":{"Name":"VPCSTACK:ExportsOutputRefsubnetaz14221E4A9"}}

Stack testCustomL2Constructs
Resources
[+] AWS::Elasticsearch::Domain testdomainfrom/testdomainfromtestdomain testdomainfromtestdomainfromtestdomainAD332E62 
```