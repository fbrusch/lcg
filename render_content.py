import pystache
import sys

template = open(sys.argv[1]).read()
context = {"content": open(sys.argv[2]).read()}

output = pystache.render(template, context)

sys.stdout.write(output)

