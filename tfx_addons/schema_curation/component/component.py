# Copyright 2021 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""TFX Schema Curation Custom Component
"""

from typing import Optional, Text, Union

from tfx import types
from tfx.dsl.components.base import base_component, executor_spec
from tfx.orchestration import data_types
from tfx.types import standard_artifacts
from tfx.types.component_spec import ChannelParameter, ExecutionParameter

from tfx_addons.schema_curation.component import executor


class SchemaCurationSpec(types.ComponentSpec):
  """ComponentSpec for TFX Schema Curation Custom Component."""

  PARAMETERS = {
      'module_file': ExecutionParameter(type=str, optional=True),
      'module_path': ExecutionParameter(type=str, optional=True),
      'schema_fn': ExecutionParameter(type=str, optional=True)
  }
  INPUTS = {
      'schema':
      ChannelParameter(type=standard_artifacts.Schema
                       ),  # Dictionary obtained as output from SchemaGen
  }
  OUTPUTS = {
      'custom_schema':
      ChannelParameter(type=standard_artifacts.Schema
                       )  # Dictionary which containes new schema
  }


class SchemaCuration(base_component.BaseComponent):
  """Custom TFX Schema Curation Component.

    The SchemaCuration component is used to apply user code to a schema
    generated by SchemaGen in order to curate the schema based on
    domain knowledge.

    Component `outputs` contains:
     - `custom_schema`: Channel of type `standard_artifact.Schema`
    """

  SPEC_CLASS = SchemaCurationSpec
  EXECUTOR_SPEC = executor_spec.ExecutorClassSpec(executor.Executor)

  def __init__(
      self,
      schema: types.Channel,
      module_file: Optional[Union[Text, data_types.RuntimeParameter]] = None,
      module_path: Optional[Union[Text, data_types.RuntimeParameter]] = None,
      schema_fn: Optional[Union[Text, data_types.RuntimeParameter]] = None):
    """Construct a SchemaCurationComponent.

        Args:
          schema: A dictionary that containes the schema generated by
            SchemaGen component of tfx
          custom_schema: A dictionary that contains the schema after curation
            by the custom schema curation component
        """

    custom_schema = types.Channel(type=standard_artifacts.Schema)

    spec = SchemaCurationSpec(schema=schema,
                              custom_schema=custom_schema,
                              module_file=module_file,
                              module_path=module_path,
                              schema_fn=schema_fn)
    super().__init__(spec=spec)
