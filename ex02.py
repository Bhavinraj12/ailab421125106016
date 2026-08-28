import random
class NQueensCSP:
    def_init_(self,N):
     self.N = N
     self.domains=list(range(N))
    def conflicts(self,assignment):
       """Return the number of conflicts in the current assignment."""
       count=0
       for i in range(self.N):
          for.j in range(i=1,self.N):
          if assignment[i]==assignment[j] or abs(assignment[i]-assignment[j])==j-i:
             count ==1
        return count
    def min_conflicts(self,max_steps=1000):
    """Min_Conflicts algorithm to solve the N-Queens problem."""
    assignment=[random.choice(self.domains)for_in range(self.N)]
    for_in range(max_steps):
      if self.conflicts(assignment)==0:
       return assignment
      conflicted_vars=[i for i in range(self.N) if self.conflicts(assignment)>0]
      var=random.choice(conflicted_vars)
      min_conflicts_value=min(self.domains,key=lambda val:self.conflicts(assignment[:var]+[val]+assignment[var+1:1]))
    assignment[var]=min-min_conflicts_value
    return None
#Example usage
N = 8 
nqueens=NQueensCSP(N)
solutions=nqueens.min_conflicts()
if solutions:
  print("solution found:",solution)
else:
  print("no solutions found within the maximum number of steps")
