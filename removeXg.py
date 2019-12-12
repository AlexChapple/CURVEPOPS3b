import os

dir_name = "/nesi/nobackup/uoa00094/CURVEPOPS3b/2017ein/output"
test = os.listdir(dir_name)

for item in test:
    if item.endswith(".xg"):
        os.remove(os.path.join(dir_name, item))