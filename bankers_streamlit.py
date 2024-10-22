# Banker's Algorithm

# Driver code:
if __name__=="__main__":
    
    # P0, P1, P2, P3, P4 are the Process names here
    n = 5 # Number of processes
    m = 3 # Number of resources
    
    # Allocation Matrix
    alloc = [[0, 1, 0 ],[ 2, 0, 0 ],
            [3, 0, 2 ],[2, 1, 1] ,[ 0, 0, 2]]
    
    # MAX Matrix 
    max = [[7, 5, 3 ],[3, 2, 2 ],
            [ 9, 0, 2 ],[2, 2, 2],[4, 3, 3]]
    
    avail = [3, 3, 2] 
    
    f = [0]*n
    ans = [0]*n
    ind = 0
    for k in range(n):
        f[k] = 0
        
    need = [[ 0 for i in range(m)]for i in range(n)]
    for i in range(n):
        for j in range(m):
            need[i][j] = max[i][j] - alloc[i][j]
    y = 0
    for k in range(5):
        for i in range(n):
            if (f[i] == 0):
                flag = 0
                for j in range(m):
                    if (need[i][j] > avail[j]):
                        flag = 1
                        break
                
                if (flag == 0):
                    ans[ind] = i
                    ind += 1
                    for y in range(m):
                        avail[y] += alloc[i][y]
                    f[i] = 1
                    
    print("Following is the SAFE Sequence")
    
    for i in range(n - 1):
        print(" P", ans[i], " ->", sep="", end="")
    print(" P", ans[n - 1], sep="")






























# import streamlit as st
# class BankersAlgorithm:
#     def __init__(self, num_processes, num_resources, max_resources, allocation, max_demand):
#         self.num_processes = num_processes
#         self.num_resources = num_resources
#         self.max_resources = max_resources
#         self.allocation = allocation
#         self.max_demand = max_demand
#         self.available = self.calculate_available()

#     def calculate_available(self):
#         total_resources = [sum(x) for x in zip(*self.allocation)]
#         available = [self.max_resources[i] - total_resources[i] for i in range(self.num_resources)]
#         return available

#     def is_safe_state(self):
#         work = self.available[:]
#         finish = [False] * self.num_processes
#         safe_sequence = []

#         while len(safe_sequence) < self.num_processes:
#             progress_made = False
#             for i in range(self.num_processes):
#                 if not finish[i] and self.can_allocate(i, work):
#                     work = [work[j] + self.allocation[i][j] for j in range(self.num_resources)]
#                     finish[i] = True
#                     safe_sequence.append(i)
#                     progress_made = True
#                     break
#             if not progress_made:
#                 return False, []

#         return True, safe_sequence

#     def can_allocate(self, process, work):
#         return all(self.max_demand[process][j] - self.allocation[process][j] <= work[j] for j in range(self.num_resources))

#     def request_resources(self, process, request):
#         if all(request[j] <= self.max_demand[process][j] - self.allocation[process][j] for j in range(self.num_resources)):
#             if all(request[j] <= self.available[j] for j in range(self.num_resources)):
#                 for j in range(self.num_resources):
#                     self.available[j] -= request[j]
#                     self.allocation[process][j] += request[j]

#                 safe, safe_sequence = self.is_safe_state()
#                 if safe:
#                     return True, safe_sequence
#                 else:
#                     for j in range(self.num_resources):
#                         self.available[j] += request[j]
#                         self.allocation[process][j] -= request[j]
#                     return False, []
#             else:
#                 return False, []
#         else:
#             return False, []

# # Streamlit app
# st.title("Banker's Algorithm")

# num_processes = 5
# num_resources = 3
# max_resources = [10, 5, 7]
# allocation = [[0, 1, 0],
#               [2, 0, 0],
#               [3, 0, 2],
#               [2, 1, 1],
#               [0, 0, 2]]
# max_demand = [[7, 5, 3],
#                [3, 2, 2],
#                [9, 0, 2],
#                [2, 2, 2],
#                [4, 3, 3]]

# banker = BankersAlgorithm(num_processes, num_resources, max_resources, allocation, max_demand)

# process_id = st.number_input("Process ID (0-4):", min_value=0, max_value=num_processes-1)
# request = st.text_input("Request (comma-separated):")

# if st.button("Request Resources"):
#     try:
#         request_list = list(map(int, request.split(',')))
#         if len(request_list) == num_resources:
#             safe, safe_sequence = banker.request_resources(process_id, request_list)
#             if safe:
#                 st.success(f"Resources allocated. Safe sequence: {safe_sequence}")
#             else:
#                 st.error("Request could not be granted safely.")
#         else:
#             st.error("Request must have the same number of elements as resources.")
#     except ValueError:
#         st.error("Please enter valid input.")
