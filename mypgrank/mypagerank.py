sparse_matrix_x=[]#记录起始网页
sparse_matrix_y=[]#记录目标网页
all_pages=[]#记录所有出现的页面
M_matrix=[]#转移矩阵
NxN_matrix=[]#NxN均值矩阵
A_matrix=[]#迭代矩阵


#快速排序所用划分函数
def Quick_Sort_Split(list_x,list_y,low,high):
    i=low
    base=list_x[low]
    for j in range(low,high):
        if(list_x[j]<=base):
            i+=1
            list_x[i],list_x[j]=list_x[j],list_x[i]
            list_y[i],list_y[j]=list_y[j],list_y[i]
    list_x[low],list_x[i]=list_x[i],list_x[low]
    list_y[low],list_y[i]=list_y[i],list_y[low]
    return i

#根据x为xy两个list都进行排序，用于存储稀疏矩阵的每一项列、行
def Quick_Sort(list_x,list_y,low,high):
    i =Quick_Sort_Split(list_x,list_y,low,high)
    Quick_Sort(list_x,list_y,low,i-1)
    Quick_Sort(list_x,list_y,i+1,high)
    return list_x,list_y


f=open('WikiData.txt','r')#只读形式按行读取数据集
line=f.readline()
while line:
    page_x,page_y=line.strip('\n').split('\t')
    sparse_matrix_x.append(page_x)
    sparse_matrix_y.append(page_y)
    if page_x not in all_pages:
        all_pages.append(page_x)
    if page_y not in all_pages:
        all_pages.append(page_y)
    line=f.readline()
f.close()
#print(sparse_matrix_x)#打印所有起始网页
#print(sparse_matrix_y)#打印所有目标网页
#print(all_pages)#打印所有网页
print("step 1 completed!")

last_pagerank=[]#存储前一时刻的pagerank
now_pagerank=[]#新的pagerank
pagenum=len(all_pages)#总的网页数目
#print(pagenum)#共7115个网页
'''
for i in range(pagenum):
    last_pagerank.append(1/pagenum)#均值初始化
    now_pagerank.append(1/pagenum)#均值初始化

for i in range(0,pagenum):
    row_M_matrix=[]#转移矩阵的一行
    row_NxN_matrix=[]#NxN均值矩阵的一行
    row_A_matrix=[]#迭代用矩阵的一行
    for j in range(0,pagenum):
        #三者初始化
        row_M_matrix.append(0)
        row_NxN_matrix.append(1/pagenum)
        row_A_matrix.append(0)
    #用上面的每一行初始化三个矩阵
    M_matrix.append(row_M_matrix)
    NxN_matrix.append(row_NxN_matrix)
    A_matrix.append(row_A_matrix)

#记录每个起始网页的出度
out_count={}
for page in sparse_matrix_x:
    out_count[page]=out_count.get(page,0)+1
    print(out_count)
'''
x,y=Quick_Sort(sparse_matrix_x,sparse_matrix_y,0,len(sparse_matrix_x)-1)
print(x)