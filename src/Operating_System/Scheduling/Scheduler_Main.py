from First_Come_First_Server import fcfs

class Jobs(object):

	def __init__(self, pid, at, bt):
		self.p_id__ = pid
		self.arrival_t = at
		self.burst_t = bt
		self.priority = None
		self.turna_t = None
		self.wait_T = None
	
	def get_pid(self):
		return self.p_id__

	def get_arrivalT(self):
		return self.arrival_t

	def __str__(self):
		string =  f"|\t{self.p_id__}\t|\t{self.arrival_t}\t|\t{self.burst_t}\t|\t{self.turna_t}\t|\t{self.wait_T}\t|"
		if self.priority != None:
			string = f"|\t{self.priority}\t" + string
		return string

def sort_jobs(j_array, size):

	for i in range(0, size-1):
		flag = False
		for j in range(0, size-1-i):
			if j_array[j].get_arrivalT() > j_array[j+1].get_arrivalT():
				j_array[j], j_array[j+1] = j_array[j+1], j_array[j]
				flag = True
		if flag == False:
			break
	return j_array

def main():
	number_of_jobs = int(input())
	job_array = list()
	for i in range(number_of_jobs):
		pid, at, bt = tuple(map(int, input().split()))
		job = Jobs(pid, at, bt)
		job_array.append(job)


	job_array = sort_jobs(job_array, len(job_array))
	
	print("|\tP_id\t|\tArrival_T\t|\tBurst_T\t|\tTurnaround_T\t|\tWaiting_T\t|")
	for i in range(len(job_array)):
		print(f"{str(job_array[i])}")

	job_array, gnatt= fcfs(job_array, len(job_array))
	
	print("|\tP_id\t|\tArrival_T\t|\tBurst_T\t|\tTurnaround_T\t|\tWaiting_T\t|")
	for i in range(len(job_array)):
		print(f"{str(job_array[i])}")

if __name__ == '__main__':
	main()

'''
5
	
'''