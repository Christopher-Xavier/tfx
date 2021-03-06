#### SIG TFX-Addons
# Project Proposal

**Your name:** Gerard Casas Saez

**Your email:** gerard@twitter.com

**Your company/organization:** Twitter

**Project name:** TFX MLMD Client Library

## Project Description

Client library to inspect content in ML Metadata populated by TFX pipelines. Library will be written in Python and distributed through PyPi.
Given metadata connection information, it should provide easy to use methods to introspect the Metadata DB.

Idea from [#12](https://github.com/tensorflow/tfx-addons/issues/12)

## Project Category

Client Library

## Project Use-Case(s)


ML Metadata contains all the metadata for TFX pipelines (pipeline state, component execution, artifact lineage...). 
However currently to query pipeline information you need to write custom code every time, as there is no common library that provides an abstraction layer on top
of the raw ML Metadata library. 

Several libraries have implemented their own implementation of this library as seen in [ModelCards](https://github.com/tensorflow/model-card-toolkit/blob/master/model_card_toolkit/utils/tfx_util.py), [NitroML](https://github.com/google/nitroml/tree/master/nitroml/analytics) 
or [Airflow example](https://github.com/tensorflow/tfx/blob/master/tfx/examples/airflow_workshop/notebooks/tfx_utils.py) in TFX repository.

Twitter already has a small implementation of this library used to track pipeline state from interactive environments.

Project will need close collaboration with TFX team to stabilize the context types ids used by TFX to track its jobs in ML Metadata.

## Project Implementation

_Distribution:_
- Python library `tfx-addons-metadata-client` released to PyPi. (potentially `tfx-addons` if we want to include more projects in the future).
- Automatic release and packaging using GitHub Actions. Versioning will depend on TFX stability for MLMD types.
- Folder: `tfx/addons/metadata-client` (we will likely also need to create some .github files for automatic testing and automatic release).

_Project implementation:_

- Python client library for ML Metadata, using ML Metadata Python SDK to query the database. 
- Main skeleton will be 3 model classes for Pipeline, PipelineRun and ComponentRun to introspect their status.
- Artifact class methods to obtain artifacts generated by each ComponentRun, PipelineRun and ComponentRun (with optional filter by ArtifactType).
- Lineage tracking for Artifact class: Obtain all artifacts that helped generate this Artifact, and check all downstream Artifacts generated by current artifact.

To be heavily based on the existing libraries by NitroML, ModelCard (see above) and [tensorflow/tfx#2415](https://github.com/tensorflow/tfx/pull/2415).


## Project Dependencies
`ml-metadata>=0.26` - Used to query the database.
`ml-pipelines-sdk>=0.26` - This will be needed to pull the type names used by TFX on ML Metadata.

## Project Team
Suzen Fylke, sue@twitter.com
Vincent Nguyen, [[To be filled]]
Paul Selden, paul.selden@openx.com
[[TFX team member TBD]]
