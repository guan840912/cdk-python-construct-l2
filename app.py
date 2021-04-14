#!/usr/bin/env python3
import os

from aws_cdk import core as cdk
from aws_cdk import core

from ppp.ppp_stack import PppStack
from ppp.ppp_stack import L2construct
from ppp.vpc import VPCStack


devenv = {
    "account": os.environ.get('CDK_DEFAULT_ACCOUNT'),
    "region": os.environ.get('CDK_DEFAULT_REGION'),
}
app = core.App()
vpcstack = VPCStack(app, "VPCSTACK", env=devenv)

newstak = core.Stack(app, 'testCustomL2Constructs', env=devenv)
L2construct(newstak, 'testdomainfrom', subnet=[vpcstack.subnet_az1.ref], SG=[vpcstack.sg.ref])
app.synth()