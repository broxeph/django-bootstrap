import os, sys

from django.test.runner import DiscoverRunner


sys.path.append(os.path.normpath(os.path.join(os.getcwd(), '..')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'testing.settings'

tr = DiscoverRunner(verbosity=1)
failures = tr.run_tests(['bootstrap'])
if failures:
    sys.exit(failures)
