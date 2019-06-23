import numpy as np

#读取文件并存储
def Readfile():
    pageX=[]#存储转移矩阵的列号
    pageY=[]#存储转移矩阵的行号
    allpages=[]#存储所有的页面
    f=open('WikiData.txt','r')#只读形式按行读取数据集
    #f=open('1.txt','r')#测试用小数据集
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
def Kill_Deadend(pageX,pageY,allpages,value):
    deadend=[]#用一个元组来存储所有deadend
    deadendX=[]#用一个元组来存储所有deadend所有源节点
    deadendY=[]#用一个元组来存储所有deadend作为目的节点
    deadendV=[]#用一个元组来存储所有deadend被指向时的出度
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
                    deadendX.append(pageX[position])
                    deadendY.append(pageY[position])
                    deadendV.append(value[position])
                    del pageY[position]
                    del pageX[position]
                    del value[position]

    return pageX,pageY,now_live_pages,deadend,deadendX,deadendY,deadendV

def Value(pageX,pageY):
    value=[]
    previous=pageX[0]
    count=0
    #counts=0#根据我们的观察推测，本数据集的初始页面都是连续出现的并且不会在其他位置出现，本函数也是依托这一特征来设计的。为了验证猜想，我们用counts值来验证这一猜想，发现假设成立。
    for i in range(len(pageX)):
        if pageX[i]==previous:
            count+=1
            if i==len(pageX)-1:#对PageX记录的最后一点特别处理，当它前面有与它相同值的点时
                for j in range(count):
                    value.append(1/count)
        else:
            previous=pageX[i]
            #counts+=1
            for j in range(count):
                value.append(1/count)
            if i==len(pageX)-1:#对PageX记录的最后一点特别处理，当它前面点和它的值不同时
                value.append(1)
            count=1
    #print(counts)
    return value

#根据行列元组对转移矩阵的元素进行赋值
def Value_and_Index(pageX,pageY):
    value=[]#记录删去deadends之后的转移矩阵值
    previous=pageX[0]#是前一个PageX[i]的值，用来与现在的PageX做对比
    count=0#记数
    #counts=0#根据我们的观察推测，本数据集的初始页面都是连续出现的并且不会在其他位置出现，本函数也是依托这一特征来设计的。为了验证猜想，我们用counts值来验证这一猜想，发现假设成立。

    #提前预处理，增加对块的索引
    block_index1=[]
    block_index2=[]
    block_index3=[]
    block_index4=[]
    block_index5=[]
    block_index6=[]
    block_index7=[]
    block_index8=[]

    for i in range(len(pageX)):
        #提前预处理，增加对块的索引,8个block_index用来记录pageY(目标页面)属于该数据块的内容角标,注意列表是按str形式存储的，和整数比大小要转为int形式
        if int(pageY[i])>0 and int(pageY[i])<=1000:
            block_index1.append(i)
        if int(pageY[i])>1000 and int(pageY[i])<=2000:
            block_index2.append(i)
        if int(pageY[i])>2000 and int(pageY[i])<=3000:
            block_index3.append(i)
        if int(pageY[i])>3000 and int(pageY[i])<=4000:
            block_index4.append(i)
        if int(pageY[i])>4000 and int(pageY[i])<=5000:
            block_index5.append(i)
        if int(pageY[i])>5000 and int(pageY[i])<=6000:
            block_index6.append(i)        
        if int(pageY[i])>6000 and int(pageY[i])<=7000:
            block_index7.append(i)
        if int(pageY[i])>7000 and int(pageY[i])<=9000:
            block_index8.append(i)
        #计算值
        if pageX[i]==previous:
            count+=1
            if i==len(pageX)-1:#对PageX记录的最后一点特别处理，当它前面有与它相同值的点时
                for j in range(count):
                    value.append(1/count)
        else:
            previous=pageX[i]
            #counts+=1
            for j in range(count):
                value.append(1/count)
            if i==len(pageX)-1:#对PageX记录的最后一点特别处理，当它前面点和它的值不同时
                value.append(1)
            count=1
    #print(counts)

    blocklist=[block_index1,block_index2,block_index3,block_index4,block_index5,block_index6,block_index7,block_index8]
    return blocklist,value

def Pagerank(pageX,pageY,now_live_pages,value,blocklist):
    ranknew=np.zeros(9000)
    rankold=np.zeros(9000)
    avgrank=1/len(now_live_pages)
    for i in now_live_pages:#首先利用所有已存在节点给rankold赋上总页面倒数平均值
        rankold[int(i)]=avgrank
    while True:
        error=0
        for i in now_live_pages:#ranknew初始值为传递参数*平均页面rank
            ranknew[int(i)]=avgrank*0.15
        for block in blocklist:
            for i in block:
                ranknew[int(pageY[i])]+=0.85*rankold[int(pageX[i])]*value[i]
        for j in range(len(rankold)):
            error+=abs(rankold[j]-ranknew[j])
        if error >=0.0000000000001:
            rankold=ranknew.copy()
            print(ranknew)
            continue
        else:
            print(ranknew)
            print(sum(ranknew))#rank值之和为1,表明无错误
            break
    return ranknew

def Calc_Deadend(rank_alive,deadendX,deadendY,deadendV):
    rank_all=rank_alive.copy()
    deadendX.reverse()
    deadendY.reverse()
    deadendV.reverse()
    for i in range(len(deadendX)):
        rank_all[int(deadendY[i])]+=rank_all[int(deadendX[i])]*deadendV[i]
    print(sum(rank_all))
    return rank_all



if __name__ == "__main__":
    pageX,pageY,allpages=Readfile()
    value=Value(pageX,pageY)
    pageX,pageY,now_live_pages,deadend,deadendX,deadendY,deadendV=Kill_Deadend(pageX,pageY,allpages,value)
    blocklist,valueafterkill=Value_and_Index(pageX,pageY)
    rank_alive=Pagerank(pageX,pageY,now_live_pages,valueafterkill,blocklist)
    rank_all=Calc_Deadend(rank_alive,deadendX,deadendY,deadendV)
    
    record_top100=[]
    record_top100_index=[]
    for j in range(100):
        max=rank_all[0]
        max_i=0
        for i in range(len(rank_all)): 
            if(rank_all[i]>max) and rank_all[i] not in record_top100:
                max=rank_all[i]
                max_i=i
        record_top100.append(max) 
        record_top100_index.append(max_i)
    
    for i in range(100):
        print (str(record_top100_index[i])+"："+str(record_top100[i]))
        

    #print(rank_all)
    #print(sum(rank_all))
    #print(block_index1)
    #print(len(block_index1)+len(block_index2)+len(block_index3)+len(block_index4)+len(block_index5)+len(block_index6)+len(block_index7)+len(block_index8))#共70922角标，完美
    #print(deadend)
    #print(len(deadend))#共1957个deadend
    #print(len(deadendX))
    #print(len(deadendY))#共32767个deadend信息
    #print(value)#活节点转移矩阵的值
    #print(len(value))#活节点转移矩阵记录有70922个值，加上死节点记录32767共103689条记录
    #print(len(now_live_pages)+len(deadend))#存活节点+deadend共7115
