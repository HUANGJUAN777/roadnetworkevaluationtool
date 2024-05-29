import json
import networkx as nx

# 读取 JSON 文件  点
file_path = 'D:/路网开发软件/路网样例地图/oushang_demo/1.geojsonl.json'
#线
file_path2 = 'D:/路网开发软件/路网样例地图/oushang_demo/2.geojsonl.json'

nodeset=set()#存点的合集
with open(file_path, 'r') as file:
    for line in file:
        try:
            json_data = json.loads(line)
            nodeset.add(json_data['properties']['HLNodeID'])
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
#假设所有的点都有线id 所有的线也有对应的点id
#把线的点放进一个集合

laneset=[]#每条线对应的两个点的id
lanenodeset=set()
with open(file_path2, 'r') as file2:
    for line in file2:
        try:
            json_data = json.loads(line)
            tmp=[0,0]
            tmp[0]=json_data['properties']['SLNodeID']
            lanenodeset.add(tmp[0])
            tmp[1]=json_data['properties']['ELNodeID']
            lanenodeset.add(tmp[1])
            laneset.append(tmp)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

# 创建一个空图
G = nx.Graph()

# 添加线
G.add_edges_from(laneset)

# 判断是否图是连通的
is_connected = nx.is_connected(G)
if is_connected:
    print("给定的线是相互连通的")
else:
    print("给定的线不是相互连通的")

#检查一下点是不是都在线上
for ele in nodeset:
    if ele in lanenodeset:
        pass
    else:
        print(f"路径集合中不包含节点 {ele}，请检查点的属性")