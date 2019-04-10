# 判断这些课程能否构成有向无环图（DAG）----拓扑排序
# 每次选择入度为0的节点，作为序列的下一个节点，然后移除该节点和以从节点出发的所有边。
# 如果N次操作结束还没判断出来，那么就不是DAG
# 这N次中，每次都找一个入度为0的点，并把它的入度变为-1，
# 作为已经取过的点不再使用，同时把从这个点指向的点的入度都-1.
# 如果找不到入度为0的点，那么说明存在环。
# 如果N次操作，每次都操作成功的去除了一个入度为0的点，那么说明这个图是DAG.
class Solution():
    def canFinish(self, N, prerequisites):
        """
        :type N,: int  N courses to take
        :type prerequisites: List[List[int]]a graph represented by a list of edges
        :rtype: bool
        """
        graph = collections.defaultdict(list)
        indegrees = collections.defaultdict(int)
        for u, v in prerequisites:
            graph[v].append(u)
            indegrees[u] += 1
        for i in range(N):
            zeroDegree = False
            for j in range(N):
                if indegrees[j] == 0:
                    zeroDegree = True
                    break
            if not zeroDegree: return False
            indegrees[j] = -1
            for node in graph[j]:
                indegrees[node] -= 1
        return True        
