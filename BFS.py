graph={
    "A":["B","C"],
    "B":["A","C","D"],
    "C":["A","B","D","E"],
    "D":["B","C","E","F"],
    "E":["C","D"],
    "F":["D"]
    }
def BFS(graph,s):
    queue=[]
    queue.append(s)
    seen=set()
    seen.add(s)
    parent={s:None}
    while queue!=[]:
        vertex=queue.pop(0)
        for node in graph[vertex]:
            if node not in seen:
                queue.append(node)
                seen.add(node)
                parent[node]=vertex
        print("BFS",vertex)
    return parent
parent=BFS(graph,"E")
for key in parent:
    print(key,parent[key])



def DFS(graph,s):
    stack=[]
    stack.append(s)
    seen=set()
    seen.add(s)
    while stack!=[]:
        vertex=stack.pop(-1)
        for node in graph[vertex]:
            if node not in seen:
                stack.append(node)
                seen.add(node)
        print("DFS",vertex)
DFS(graph,"A")
