sparse_matrix_x=[]#记录起始网页
sparse_matrix_y=[]#记录目标网页
all_pages=[]#记录所有出现的页面

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
print(all_pages)#打印所有网页
print("step 1 completed!")

last_pagerank=[]#存储前一时刻的pagerank
now_pagerank=[]#新的pagerank
pagenum=len(all_pages)#总的网页数目
#print(pagenum)#共7115个网页

for i in range(pagenum):
    last_pagerank.append(1/pagenum)#均值初始化
    now_pagerank.append(1/pagenum)#均值初始化
