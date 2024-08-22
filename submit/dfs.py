queue=[]
def bfs(x,y):
    global flag,vis,queue;
    queue.append([0,0])
    while (queue!=[]):
        if(G[queue[0][0]][queue[0][1]] == 2):
            flag = True;
            return
        for i in range(4):
            nx = queue[0][0] + fx[i]
            ny = queue[0][1] + fy[i]
            if(nx >= 0 and nx < n and ny < m and ny >= 0 and vis[nx][ny] == 0 and G[nx][ny]!= 1):
                vis[nx][ny] = 1
                queue.append([nx,ny])
        queue.pop(0)
flag=False
G=[]
vis=[]
fx=[1,-1,0,0]
fy=[0,0,-1,1]
n=int(input())
m=int(input())
for i in range(n):
    G.append(list(eval(input())))
for i in range(n):
    temp=[]
    for j in range(m):
        temp.append(0)
    vis.append(temp)
vis[0][0]=1
bfs(0,0)
print(flag)
