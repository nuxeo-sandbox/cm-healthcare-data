# Medical Claim Data

## Installation

Data preparation steps include uploading the templates and importing the CSV data.

### Templates

Upload all from 'templates' to 'Domain/Templates' as a 'File Template' object.  Use the Import tab to upload all documents as once.  Click 'Add Properties', choose 'File Template' then 'Apply to All'.  Finally, 'Create' the documents.

### CSV Data

Import CSV files into the respective directories.

* Use CSV Import tab to import 'data/users.csv' to 'Domain/Workspaces/CSRs', no CSV switches required.
* Use CSV Import tab to import 'data/providers.csv' to 'Domain/Workspaces/Providers', no CSV switches required.
* Use CSV Import tab to import 'data/members.csv' to 'Domain/Workspaces/Members', no CSV switches required.
* Use CSV Import tab to import 'data/claims.csv' to 'Domain/Workspaces/CLaims', enable the 'Apply Date, Author and Dublin Core properties.' switch.

> The data preparation and installation is complete.

## New Data Generation

You can generate new fake data if you wish.

Relies on Python 3 and the 'faker' library.

### Install dependencies

`$ pip3 install -r requirements.txt`

### Generate new data

`$ python3 src/new_claims.py > data/output.csv`
