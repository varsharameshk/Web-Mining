import networkx
import matplotlib.pyplot as plt
import warnings

N= networkx.read_edgelist(r"C:\Users\Varsha's PC\Desktop\web-google.csv", delimiter=',', create_using=networkx.Graph())
print(networkx.info(N))
print(networkx.is_directed(N))
N=networkx.fast_gnp_random_graph(20,0.5,directed=True)
networkx.draw(N,with_labels=True)
plt.show()
print(networkx.is_directed(N))
print(networkx.pagerank(N,alpha = 0.5))
