import shutil

diskLabel = 'C:/Users/park0/opencvDojang/data'
# total, used, free = shutil.disk_usage(diskLabel)

# print(total)
# print(used)
# print(free)

import os

print(os.path.getsize(diskLabel))
