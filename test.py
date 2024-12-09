import psutil
import sys
import flask
print(sys.base_prefix)
print(sys.prefix)

psutil.net_if_stats()