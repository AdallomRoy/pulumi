# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .get_ami_ids import *
from .list_storage_account_keys import *
from .provider import *
from ._inputs import *
from . import outputs
_utilities.register(
    resource_modules="""
[]
""",
    resource_packages="""
[
 {
  "pkg": "mypkg",
  "token": "pulumi:providers:mypkg",
  "fqn": "pulumi_mypkg",
  "class": "Provider"
 }
]
"""
)