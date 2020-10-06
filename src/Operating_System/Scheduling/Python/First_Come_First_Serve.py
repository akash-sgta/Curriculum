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

def waiting_time_util(processes):

	n = len(processes)
	completed_jobs = 0
	clock_ticks = 0

	current_job = 0 # job at pos 0
	current_job_left = processes[current_job].burst_time

	while completed_jobs != n:

		check_for_job_finished = False
		if current_job_left > 0:
			current_job_left -= 1 # reduce time left
		else:
			check_for_job_finished = True
		
		if check_for_job_finished == True:
			completed_jobs += 1

			processes[current_job].completion_time = clock_ticks
			processes[current_job].waiting_time = (processes[current_job].completion_time
													- processes[current_job].burst_time
													- processes[current_job].arrival_time)

			if processes[current_job].waiting_time < 0:
				processes[current_job].waiting_time = 0

			current_job += 1
			if current_job < n:
				current_job_left = processes[current_job].burst_time
				if processes[current_job].arrival_time > clock_ticks:
					clock_ticks = processes[current_job].arrival_time # increment clock for the ticks when the cpu will be idle

			continue # shoud not increase clock as no work done in this iteration

		clock_ticks += 1

	return True

def turn_around_time_util(processes):

	n = len(processes)

	for i in range(n):
		processes[i].turn_around_time = processes[i].completion_time - processes[i].arrival_time
	
	return True
	
def print_process_chart(processes):

	n = len(processes)
	print("Process\t|\tAT\t|\tBT\t|\tCT\t|\tTAT\t|\tWT")
	for i in range(n):
		print(str(processes[i]))

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