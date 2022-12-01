#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import networkx as nx  
G = nx.Graph()
G.add_weighted_edges_from([(1, 2,6), (1, 3, 8), (1, 4, 1),
                            (2,4,2), (2, 5, 1),
                            (3,4, 5), (3, 5, 5), (3, 6, 1), (3, 7, 2),
                            (4, 7,6),(4,11,2),
                            (5, 6, 3), (5, 8, 2), (5, 9, 9),
                            (6, 7, 4), (6, 9, 6),
                            (7, 9, 3), (7, 10, 1),
                            (8, 9, 7), (8, 11, 9),
                            (9, 10, 1), (9, 11, 2),
                            (10, 11, 4)])# 批量加入赋权边，格式（点1，点2，权值）



G = nx.DiGraph(G) #构建有向图
layout = nx.shell_layout(G)  #排列节点,保证两次排列方式一样，使第二次绘制权值时在边上
nx.draw(G, layout,node_color = 'pink',with_labels = True,alpha = 0.7)

labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, layout, edge_labels=labels)
plt.savefig('graph.png',dpi = 800)
plt.show()

