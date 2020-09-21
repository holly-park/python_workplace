"""구구단을 출력하는 함수
    mygugu(3,5)"""

def mygugu(start,end):
   for i in range(start, end+1):
      print("***", i, "단***")
      for j in range(1,10):
          print("%3d x %3d = %3d"%(i,j,i*j))
  

mygugu(3,5)