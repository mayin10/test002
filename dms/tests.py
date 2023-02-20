import os



base = os.path.abspath('..')+"\\media\\zip"
print(base)

for dirpath, dirnames, filenames in os.walk(base):
    #list = dirpath.split("\\")
    for filename in filenames:
        if len(filename) > 100:
            print(os.path.join(dirpath, filename))



