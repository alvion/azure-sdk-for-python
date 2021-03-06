# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ExitCodeRangeMapping(Model):
    """A range of exit codes and how the Batch service should respond to exit
    codes within that range.

    All required parameters must be populated in order to send to Azure.

    :param start: Required. The first exit code in the range.
    :type start: int
    :param end: Required. The last exit code in the range.
    :type end: int
    :param exit_options: Required. How the Batch service should respond if the
     task exits with an exit code in the range start to end (inclusive).
    :type exit_options: ~azure.batch.models.ExitOptions
    """

    _validation = {
        'start': {'required': True},
        'end': {'required': True},
        'exit_options': {'required': True},
    }

    _attribute_map = {
        'start': {'key': 'start', 'type': 'int'},
        'end': {'key': 'end', 'type': 'int'},
        'exit_options': {'key': 'exitOptions', 'type': 'ExitOptions'},
    }

    def __init__(self, **kwargs):
        super(ExitCodeRangeMapping, self).__init__(**kwargs)
        self.start = kwargs.get('start', None)
        self.end = kwargs.get('end', None)
        self.exit_options = kwargs.get('exit_options', None)
