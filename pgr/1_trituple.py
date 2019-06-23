#读取文件并存储
def Readfile():
    pageX=[]#存储转移矩阵的列号
    pageY=[]#存储转移矩阵的行号
    allpages=[]#存储所有的页面
    f=open('WikiData.txt','r')#只读形式按行读取数据集
    line=f.readline()
    while line:
        tempX,tempY=line.strip().split()#读取文件进两个元组
        pageX.append(tempX)
        pageY.append(tempY)
        if tempX not in allpages:
            allpages.append(tempX)
        if tempY not in allpages:
            allpages.append(tempY)
        line=f.readline()
    return pageX,pageY,allpages


#去除所有deadend以及因此而产生的新deadend直到所有pages变为强连通
def Kill_Deadend(pageX,pageY,allpages):
    deadend=[]#用一个元组来存储所有deadend
    now_live_pages=allpages#假定最初所有页面都是活页面
    last_live_pages=[]
    while True:
        if len(now_live_pages) == len(last_live_pages):#当上一次的存活页面和本次存活页面个数相同时，说明图已强连通
            print("number of final_live_pages:")
            print(len(now_live_pages))#计算出最终一共5158个强连通页面
            break
        print("number of last_live_pages:")
        print(len(last_live_pages))
        print("number of now_live_pages:")
        print(len(now_live_pages))
        last_live_pages=now_live_pages#开始操作，将本次存活页面存入last_live_pages并且把now_live_pages置空
        now_live_pages=[]
        for i in last_live_pages:
            if i in pageX:
                now_live_pages.append(i)#当页面还能在pageX中找到时，将页面存入now_live_pages
            else:
                deadend.append(i)
                while i in pageY:#当页面不在pageX中却在pageY中，查找出y中所有该页面记录的下标，并且删除pageX、pageY中所有对应下标的项
                    position=pageY.index(i)
                    #print(position)
                    del pageY[position]
                    del pageX[position]
    return pageX,pageY,now_live_pages,deadend

#根据行列元组对转移矩阵的元素进行赋值
def Value(pageX,pageY):
    
    return


'''
def deadend(pageX,pageY):
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
'''

if __name__ == "__main__":
    pageX,pageY,allpages=Readfile()
    pageX,pageY,now_live_pages,deadend=Kill_Deadend(pageX,pageY,allpages)
    #print(deadend)
    #print(len(deadend))#共1957个deadend
    #print(len(now_live_pages)+len(deadend))#存活节点+deadend共7115个
    