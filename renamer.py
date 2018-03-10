import os;
import sys;

path = sys.argv[1]
oldWord = sys.argv[2]
newWord = sys.argv[3]

counter = 0

for file in os.listdir(path):
    if oldWord in os.path.splitext(file)[0]:
        counter = counter + 1
        os.rename(path + "\\"+file, path + "\\"+file.replace(oldWord, newWord))

print(str(counter)+ " files have been found")