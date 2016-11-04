import pystache
import sys

template = open(sys.argv[1]).read()
context = {"content": sys.stdin.read()}

output = pystache.render(template, context)

sys.stdout.write(output)

