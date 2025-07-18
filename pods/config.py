#
# This loads the configuration
#
import sys
import os

if sys.version_info >= (3, 0):
    import configparser
else:
    import ConfigParser as configparser

config = configparser.ConfigParser()

# This is the default configuration file that always needs to be present.
default_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "defaults.cfg"))

# These files are optional
# This specifies configurations that are typically specific to the machine (it is found alongside the GPy installation).
local_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "machine.cfg"))

# This specifies configurations specific to the user (it is found in the user home directory)
home = os.getenv("HOME") or os.getenv("USERPROFILE")
user_file = os.path.join(home, ".ods_user.cfg")

# Read in the given files.
config.read_file(open(default_file))
config.read([local_file, user_file])
if not config:
    raise ValueError(
        "No configuration file found at either "
        + user_file
        + " or "
        + local_file
        + " or "
        + default_file
        + "."
    )
