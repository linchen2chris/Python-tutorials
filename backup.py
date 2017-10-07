# archive the __init__.py to a zip file

import os
import time

source = ['./__init__.py']

target_dir = './'

target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -qr %s %s" % (target, ''.join(source))

print(zip_command)

if os.system(zip_command) == 0:
    print('Successful backup to %s' % target)
else:
    print('backup fail')
