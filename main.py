from CSVLoader import DataLoader
import DataGraph
data_loader = DataLoader()


def loadDistanceGraph():
    distances_data = data_loader.load_distances_csv('/Users/zacharymollenhour/Desktop/WGUChainRouting/distance_table.csv')
    graph = DataGraph.CompleteGraph(len(distances_data))
    for i in range(0, len(distances_data)):
        for j in range(0, len(distances_data[i])):
            graph.add_edge(i, j, distances_data[i][j])
    return graph

loadDistanceGraph()