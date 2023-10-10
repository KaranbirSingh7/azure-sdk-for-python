# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from gencore.serialization import CoreJSONEncoder, NULL

AzureJSONEncoder = CoreJSONEncoder

__all__ = ["NULL", "AzureJSONEncoder"]
