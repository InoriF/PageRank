def Readfile():
    pageX=[]#存储转移矩阵的列号
    pageY=[]#存储转移矩阵的行号
    valueXY=[]#存储对应行列的值
    f=open('WikiData.txt','r')#只读形式按行读取数据集
    line=f.readline()
    while line:
        tempX,tempY=line.strip().split()
        pageX.append(tempX)
        pageY.append(tempY)
        line=f.readline()
    return pageX,pageY,valueXY

def deadend(pagex,pagey):
    deadend=[]
    n=len(pagex)
    for i in range(n):
        if pagey[i] not in pagex:
            if pagey[i] not in deadend:
                deadend.append(pagey[i])
            del pagex[i]
            del pagey[i]
    print ("deadend is ")
    print (deadend)

    original=0
    while original != n:
        n=len(pagex)
        for i in range(n):
            if pagey[i] not in pagex:
                if pagey[i] not in deadend:
                    deadend.append(pagey[i])
                del pagex[i]
                del pagey[i]
            else:
                original+=1
        print ("deadend is ")
        print (len(deadend))

    print ("deadend is ")
    print (len(deadend))
    return deadend

if __name__ == "__main__":
    pageX,pageY,valueXY=Readfile()
    deadend=deadend(pageX,pageY)
