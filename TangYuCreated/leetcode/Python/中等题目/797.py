class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.graph = graph
        self.path = []
        self.target = len(graph) - 1
        self.findThePath(0,[])
        return self.path
    
    def findThePath(self,currentPoint,path):
        if currentPoint != self.target:
            for point in self.graph[currentPoint]:
                self.findThePath(point,path + [currentPoint])
        else:
            self.path.append(path + [self.target])
