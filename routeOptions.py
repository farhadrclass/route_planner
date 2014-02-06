from shared import *

class RouteOptions(object):
	"""RouteN is a class that calculates all different route options given N nodes"""

	def __init__(self,N):
		"initiates the route"

		self.N = N
		self.route = [[]]
		self.routeCount = 0
		self.maxRouteCount = factorial(N)

		print("there will be {} route combinations".format(self.maxRouteCount))
	
	def setRoute(self,nodes):
		"function to itterate through the nodes"

		for i in nodes:
			nodesLeft = nodes.copy()
			nodesLeft.remove(i)
			self.route[self.routeCount].append(i)
			if (len(nodesLeft) > 0):
				self.setRoute(nodesLeft)
			else:
				self.routeCount += 1

				if (self.routeCount < self.maxRouteCount):
					self.route.append([])

	def cleanRoute(self):
		"function to clean the route"

		finalRoute = []

		for nodes in self.route:
			if (len(nodes) == self.N):
				defaultRoute = nodes
				finalRoute.append(nodes)
			else:
				defaultRoute = defaultRoute[0:-len(nodes)]+nodes
				finalRoute.append(defaultRoute)

		self.route = finalRoute

	def getRoute(self):
		"function to return the route"

		nodes = list(range(0,self.N))
		self.setRoute(nodes)
		self.cleanRoute()

		return self.route

if __name__ == "__main__":
	route5 = RouteOptions(5).getRoute()