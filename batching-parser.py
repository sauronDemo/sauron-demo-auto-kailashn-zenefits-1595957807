#!/usr/bin/env python
import json
import os
import sys

try:
    payload = json.loads(os.environ.get('PAYLOAD'))
except Exception:
    print 'Could not parse "PAYLOAD" env var so trying "extras" env var.'
    try:
        payload = json.loads(os.environ.get('extras'))
    except Exception:
        print "Could not figure out what to merge."
        print "Assuming this is not a batch build and"
        print "not writing down batch file for merge script."
        sys.exit(0)

sha_sequence = payload.get('sha_sequence', None)
if sha_sequence is None:
    print "Parsed JSON payload but did not see 'sha_sequence' key."
    print "Assuming this is not a batch build."
else:
    with open('batch', 'w') as f:
        for sha in sha_sequence:
            f.write("{}\n".format(sha))
