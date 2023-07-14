import random

def ms_to_adj(ms, v):
    adj = [[] for i in range(v)]
    for i in range(v):
        for j in range(v):
            if ms[i][j] != 0:
                adj[i].append(j)
    return adj

def rand_g():
    # level = random.randint(3, 6)
    level = 4
    cnt_each_level = [0] * level
    cnt_each_level[0] = cnt_each_level[-1] = 1
    for i in range(1, level-1):
        cnt_each_level[i] = random.randint(2, 2 + 2 * (level - 1 - i))
    g = [[] for k in range(level)]
    num = 0
    for i in range(level):
        for j in range(cnt_each_level[i]):
            g[i].append(num)
            num += 1
    v = num
    ms = [[0 for i in range(v)] for j in range(v)]
    for i in range(level-1):
        for j in range(0, len(g[i])):
            if len(g[i+1]) >= 2:
                for k in range(0, len(g[i+1])):
                    ms[g[i][j]][g[i + 1][k]] = random.randint(10, 50)
            else:
                    ms[g[i][j]][g[i + 1][0]] = random.randint(10, 50)
    return ms, v

def dijkstra(start, finish, ms, adj, v):
    '''
    не работает для графиках с тупиками
    '''
    tmp_ms = [[ms[j][i] for i in range(v)] for j in range(v)]
    dist = [99999999] * v
    completed = [False] * v
    completed[start] = True
    dist[start] = 0
    queue = [start]
    last = [-1] * v
    last[0] = 0
    while not all(completed):
        v0 = queue.pop(0)  # убираем из очереди вершину, тк мы ее либо продолжим, либо нет
        flag = True
        # этот фор нужен для того, чтобы проверить, что все входящие ребра учтены, иначе мы просто скипаем эту вершину
        for j in range(v):
            if tmp_ms[j][v0] != 0:  # если есть хоть одно входящее в эту вершину ребро, то дальше по нему не идем
                flag = False
        if flag:
            completed[v0] = flag
            for i in adj[v0]:  # перебираем все исходящие вершины
                # print(i)
                new_dist = dist[v0] + ms[v0][i]
                tmp_ms[v0][i] = 0  # исключаем ребро и списка ребер, типо оно уже пройдено
                if dist[i] > new_dist:
                    dist[i] = new_dist
                    last[i] = v0
                queue.append(i)

    x = -1
    way = [v-1]
    while x != 0:
        x = last[x]
        way.append(x)
    return dist[finish], dist, way[::-1]

ms, v = rand_g()
adj = ms_to_adj(ms, v)
for i in ms:
    print(i)
res, dist, way = dijkstra(0, v-1, ms, adj, v)
print(way, res)
