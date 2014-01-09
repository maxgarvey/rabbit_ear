#process_tools.py
#just a little lib for setting up the processes

#1/8/14
#Max Garvey

from subprocess import Popen
import os

def spawn_process(python_route, worker_route):
	return Popen([python_route, worker_route], preexec_fn=os.setsid)

def kill_process(process):
	process.kill()

def respawn_process(process, python_route, worker_route):
	kill_process(process)
	return spawn_process(python_route, worker_route)

def create_processes(python_route, worker_route, quantity):
	processes = []
	for i in xrange(quantity):
		processes.append(spawn_process(python_route, worker_route))
	return processes

def kill_processes(processes):
	for process in processes:
		process.kill()