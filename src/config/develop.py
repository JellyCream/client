import os
import logging

from production import defaults as production_defaults

# These directories are in Appdata (e.g. C:\ProgramData on some Win7 versions)
if 'ALLUSERSPROFILE' in os.environ:
    APPDATA_DIR = os.path.join(os.environ['ALLUSERSPROFILE'], "FAForeverDevelop")
else:
    APPDATA_DIR = os.path.join(os.environ['HOME'], "FAForeverDevelop")

defaults = production_defaults.copy()
defaults['host'] = 'test.faforever.com'
defaults['client/data_path'] = APPDATA_DIR

# FIXME: Temporary fix for broken https config on test server
# Turns off certificate verification entirely
import ssl
ssl._https_verify_certificates(False)
