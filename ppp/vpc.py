from aws_cdk import core as cdk
from aws_cdk import (
    core,
    aws_elasticsearch as es,
    aws_ec2 as ec2
)


class VPCStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.vpc = ec2.CfnVPC(self, 'vpc', cidr_block="10.0.0.0/16")
        self.subnet_az1 = ec2.CfnSubnet(self, 'subnet_az1', vpc_id=self.vpc.ref, cidr_block="10.0.0.0/24")
        self.sg = ec2.CfnSecurityGroup(self, 'sg', vpc_id=self.vpc.ref, group_description="sg for vpc")