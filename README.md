# Lephare Data

This repository contains all the auxillary data needed for [Lephare](https://github.com/lephare-photoz/lephare).

## Note the two actions included:
### Update registry file
  - [Action](https://github.com/lephare-photoz/lephare-data/actions/workflows/update-registry.yml) | [Yaml file](https://github.com/lephare-photoz/lephare-data/blob/main/.github/workflows/update-registry.yml) | [Python file](https://github.com/lephare-photoz/lephare-data/blob/main/scripts/add_to_registry.py)
  - Triggers on push (and manually).
  - Rebuilds the registry file, where each line contains a path to a data file and the file's hash.
  - Regenerates a hash of the registry file itself.
### Update zip on OSF
  - [Action](https://github.com/lephare-photoz/lephare-data/actions/workflows/update-zip-on-osf.yml) | [Yaml file](https://github.com/lephare-photoz/lephare-data/blob/main/.github/workflows/update-zip-on-osf.yml)
  - Triggers on push (and manually).
  - Zips all the data and uploads it to the [Lephare OSF project](https://osf.io/mvpks/files/osfstorage).
  - This includes versioning automatically.
