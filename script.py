import os
import re

dir = os.fsencode("koans")

for file in os.listdir(dir):
    filename = os.fsdecode(file)
    match = re.search("about.*\.rb", filename)
    if match is not None:
        print(f'- [{filename.replace(".rb", "")}](https://github.com/willpinha/my-ruby-koans/blob/master/koans/{filename})')
    