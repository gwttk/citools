import sys
import os
import base64

env_var_name = sys.argv[1]
output_file_path = sys.argv[2]

# get env var value
base64str =os.environ[env_var_name]

# decode and write to file
with open(output_file_path, "wb") as fh:
	fh.write(base64.b64decode(base64str, validate=True))
