# <argv1> string for hashing
# <argv2> number of hashes to generate
#
# uploads plot of individual hashes and blob hashes to plotly

import hashlib
import time, sys
import plotly, plotly.plotly as py, plotly.graph_objs as go
plotly.tools.set_credentials_file(username="nseidl", api_key="FEPhHlSVEO6rVHXy3YEK")

# s : string to hash
# n : number of hashes to generate
# return : time it took
def hash_n(s, n):
	print "Starting %s individual hashes." % n
	start = time.time()

	for i in range(n):
		hashlib.sha256(s).hexdigest()

	end = time.time()
	print "Ending invidiual hashes. Took %ss to hash %s individually." % (str(end - start), n)

	return (end - start)

# s : string to append to itself
# n : number of times to append string to itself
# return : time it took
def hash_blob(s, n):
	print "Starting blob hash of %s." % n
	start = time.time()

	to_hash = ""

	for i in range(n):
		to_hash += s

	hashlib.sha256(s).hexdigest()

	end = time.time()
	print "Ending blob hash. Took %ss to hash %s in a blob." % (str(end - start), n)

	return (end - start)

def calc_indv(sizes):
	results = []
	for i in range(len(sizes)):
		results.append(hash_n(STR, sizes[i]))

	return results

def calc_blob(sizes):
	results = []
	for i in range(len(sizes)):
		results.append(hash_blob(STR, sizes[i]))

	return results

def plot_results(x, indv, blob):
	indv_trace = go.Scatter(
		x = x,
		y = indv,
		mode = "lines+markers",
		name = "individual"
	)

	blob_trace = go.Scatter(
		x = x,
		y = blob,
		mode = "lines+markers",
		name = "blob"
	)

	to_plot = [indv_trace, blob_trace]

	py.iplot(to_plot, filename="test")

if __name__ == "__main__":
	STR = str(sys.argv[1])
	sizes = [i*100000 for i in range(51)]

	invidiual_results = calc_indv(sizes)
	blob_results = calc_blob(sizes)

	plot_results(sizes, invidiual_results, blob_results)










