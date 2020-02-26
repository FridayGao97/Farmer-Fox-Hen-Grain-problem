"""
Solution stub for the River Problem.

Fill in the implementation of the `River_problem` class to match the
representation that you specified in problem XYZ.
"""
from searchProblem import Search_problem, Arc

# for this assignment, I use tuple to store node; 
# and the node only view from left side(element in tuple are currently located in left side)
#

class River_problem(Search_problem):
    def start_node(self):
        """returns start node"""
        #TODO
        return ("Farmer","hen","fox","grain")
    
    def is_goal(self,node):
        """is True if node is a goal"""
        #TODO
        
        #
        #return len(node) % 2 == 0 # dummy goal, state has two items in it
        return node in {("nothing on LS")}

    def neighbors(self,node):
        """returns a list of the arcs for the neighbors of node"""
        
        #TODO
        if (node == ("Farmer","hen","fox","grain")):
        	return [Arc(("Farmer","hen","fox","grain"),("fox","grain"),1,'Farmer takes hen to right side')]
        	#return ("fox","grain")
        elif (node == ("fox","grain")):
        	return [Arc(("fox","grain"),("Farmer","fox","grain"),1,'Farmer back to left side')]
        	#return ("Farmer","fox","grain")
        elif (node == ("Farmer","fox","grain")):
        	return [Arc(("Farmer","fox","grain"),("fox"),1,'Farmer takes grain to RS'),Arc(("Farmer","fox","grain"),("grain"),6,'Farmer takes fox to RS')]
        	#return {("fox"),("grain")}
        	#Arc(("Farmer","fox","grain"),("grain"),8)
        	#Arc(("Farmer","fox","grain"),("fox"),8)
        elif (node == ("fox")):
        	return [Arc(("fox"),("Farmer","hen","fox"),1,'Farmer takes hen back to LS')]
        	#return ("Farmer","hen","fox")
        elif (node == ("grain")):
        	return [Arc(("grain"),("Farmer","hen","grain"),1,'Farmer takes hen back to LS')]
        	#return ("Farmer","hen","grain")
        elif (node == ("Farmer","hen","fox")):
        	return [Arc(("Farmer","hen","fox"),("hen"),1,'Farmer take fox to RS')]
        	#return ("hen")
        elif (node == ("Farmer","hen","grain")):
        	return  [Arc(("Farmer","hen","grain"),("hen"),1,'Farmer take grain to RS')]
        	#return ("hen")
        elif (node == ("hen")):
        	return [Arc(("hen"),("Farmer","hen"),2,'Farmer back to LS')]
        	#return ("Farmer","hen")
        elif (node == ("Farmer","hen")):
        	return [Arc(("Farmer","hen"),("nothing on LS"),2,'Farmer take hen to RS')]
        	#return ("")
        
        
        #return [Arc(node, node+(None,), 1, 'ADD-NONE')]
        # return self.neighs[node]

    def heuristic(self,n):
        """Gives the heuristic value of node n."""
        if "Framer" in n:
        	return 2*(len(n) -1) - 1
        else:
        	return 2*len(n)
        
        #TODO
        #return 0
    

