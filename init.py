from process_tools import *
import ujson as json
from time import sleep
import sys


try:
	with open(sys.argv[1:] or "./config.txt") as fd:
		config = json.load(fd)
		assert(isinstance(config, dict))
		assert("python_path" in config)
		assert("worker_path" in config)
		assert("quantity" in config)
except Exception as e:
	print(e)
	sys.exit(0)

processes = create_processes(config["python_path"], config["worker_path"],
	config["quantity"])

try:
	while True:
		sleep(1)
finally:
	kill_processes(processes)