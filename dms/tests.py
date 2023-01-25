import os



base = os.path.abspath('..')+"\\static\\DOKUMENTE\\123990708"
print(base)

for dirpath, dirnames, filenames in os.walk(base):
    #list = dirpath.split("\\")
    for filename in filenames:
        if len(filename) > 100:
            print(os.path.join(dirpath, filename))



