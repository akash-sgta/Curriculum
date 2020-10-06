import sys
MAXINT = sys.maxsize

class Process(object):

	def __init__(self, p_id=None, burst_time=None, arrival_time=None):
		self._p_id = p_id
		self._burst_time = burst_time
		self._arrival_time = arrival_time
		self._completion_time = 0
		self._turn_around_time = 0
		self._waiting_time = 0
	
	@property
	def p_id(self):
		return self._p_id
	@p_id.setter
	def p_id(self, val):
		self._p_id = val

	@property
	def burst_time(self):
		return self._burst_time
	@burst_time.setter
	def burst_time(self, val):
		self._burst_time = val
	
	@property
	def arrival_time(self):
		return self._arrival_time
	@arrival_time.setter
	def arrival_time(self, val):
		self._arrival_time = val
	
	@property
	def turn_around_time(self):
		return self._turn_around_time
	@turn_around_time.setter
	def turn_around_time(self, val):
		self._turn_around_time = val
	
	@property
	def waiting_time(self):
		return self._waiting_time
	@waiting_time.setter
	def waiting_time(self, val):
		self._waiting_time = val
	
	@property
	def completion_time(self):
		return self._completion_time
	@completion_time.setter
	def completion_time(self, val):
		self._completion_time = val
	
	def __str__(self):
		return f'{self.p_id}\t|\t{self.arrival_time}\t|\t{self.burst_time}\t|\t{self._completion_time}\t|\t{self.turn_around_time}\t|\t{self.waiting_time}'

def sort_processes(processes):
	n = len(processes)
	for i in range(0, n):
		pos = i
		for j in range(i+1, n):
			if processes[pos].arrival_time > processes[j].arrival_time:
				pos = j
		if pos != i:
			processes[pos],processes[i] = processes[i],processes[pos]
	return processes

def print_process_chart(processes):

	n = len(processes)
	print("Process\t|\tAT\t|\tBT\t|\tCT\t|\tTAT\t|\tWT")
	for i in range(n):
		print(str(processes[i]))

def waiting_time_util(processes):

	n = len(processes)
	
	completed_jobs = 0
	remaining_time = [processes[_].burst_time for _ in range(n)]
	shortest = 0
	minimum = MAXINT
	check = False
	
	clock_ticks = 0
	while completed_jobs != n:

		for i in range(n):
			if (processes[i].arrival_time <= clock_ticks
			and remaining_time[i] < minimum
			and remaining_time[i] > 0):
				minimum = remaining_time[i]
				shortest = i
				check = True
		
		if check == False:
			clock_ticks += 1
			continue
		
		remaining_time[shortest] -= 1
		minimum = remaining_time[shortest]
		if minimum <= 0:
			minimum = MAXINT
		
		if remaining_time[shortest] == 0:
			completed_jobs += 1
			check = False

			processes[shortest].completion_time = clock_ticks + 1
			processes[shortest].waiting_time = (processes[shortest].completion_time
												- processes[shortest].arrival_time
												- processes[shortest].burst_time)
			
			if processes[shortest].waiting_time < 0:
				processes[shortest].waiting_time = 0

		clock_ticks += 1

	return True

def turn_around_time_util(processes):

	n = len(processes)

	for i in range(n):
		processes[i].turn_around_time = processes[i].completion_time - processes[i].arrival_time
	
	return True

def compute(processes):
    
	n = len(processes)
	processes = sort_processes(processes)
	
	waiting_time_util(processes)
	turn_around_time_util(processes)
	
	print_process_chart(processes)
	
	wt_sum,tat_sum = 0,0
	for i in range(n):
		wt_sum += processes[i].waiting_time
		tat_sum += processes[i].turn_around_time

	return tat_sum/n, wt_sum/n


def main():

	array_of_process = list()
	array_of_process.append(Process('P1', 4, 3))
	array_of_process.append(Process('P2', 3, 5))
	array_of_process.append(Process('P3', 2, 0))
	array_of_process.append(Process('P4', 1, 5))
	array_of_process.append(Process('P5', 2, 4))

	a_tat, a_wt = compute(array_of_process)
	print(f"Average Turnaround Time : {a_tat}")
	print(f"Average Waiting Time : {a_wt}")

main()