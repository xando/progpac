import os
import sys
import re
import time
from django.core.management import setup_environ
import settings

setup_environ(settings)

from progpac.core.models import Level

def sorted_nicely( l ): 
    """ Sort the given iterable in the way that humans expect.""" 
    convert = lambda text: int(text) if text.isdigit() else text 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)

if len(sys.argv) > 1:
    directory = sys.argv[1]
    Level.objects.all().delete()
    for f in sorted_nicely(os.listdir(sys.argv[1])):
        file_content = open(os.path.join(directory, f)).readlines()
        level_lines = file_content[:25]
        content = [line.rstrip() for line in level_lines]
        name = f.rstrip(".txt")
        content = "\n".join(content)

        points = file_content[26].strip().split(" ")[1]
        maxsize = file_content[27].strip().split(" ")[1]
        
        Level.objects.create(
            name=name,
            content=content,
            points=points,
            maxsize=maxsize
        )

        time.sleep(0.01)