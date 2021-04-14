from aws_cdk import core as cdk
from aws_cdk import (
    core,
    aws_elasticsearch as es,
    aws_ec2 as ec2
)


class PppStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, vpcstack: core.Stack,  **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #esClusterfn(self, 'hello', subnet=[vpcstack.subnet_az1.ref], SG=[vpcstack.sg.ref])


# def esClusterfn(self, id: str, subnet: [ec2.CfnSubnet], SG: [ec2.CfnSecurityGroup]):
#             es.CfnDomain(self, id+'testdomain',
#             elasticsearch_version='7.9',
#             vpc_options=es.CfnDomain.VPCOptionsProperty(
#                 security_group_ids=SG,
#                 subnet_ids=subnet))
        L2construct(self, 'hello', subnet=[vpcstack.subnet_az1.ref], SG=[vpcstack.sg.ref])


# Try use L2 Constructs.
class L2construct(cdk.Construct):
    def __init__(self, scope: cdk.Construct, construct_id: str, subnet: [ec2.CfnSubnet], SG: [ec2.CfnSecurityGroup], **kwargs) -> None:
        super().__init__(scope, construct_id)
        es.CfnDomain(self, construct_id+'testdomain',
            elasticsearch_version='7.9',
            vpc_options=es.CfnDomain.VPCOptionsProperty(
                security_group_ids=SG,
                subnet_ids=subnet))