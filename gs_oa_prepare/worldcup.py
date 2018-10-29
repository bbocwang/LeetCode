class wordcup():
    def cal(self,input):
        result = sorted(input)
        result.reverse()
        first=result[0]
        second=0
        t1=1
        for i in range(1,len(input)+1):
            t1=t1*i
        t2=1
        for i in range(1,len(input)-1):
            t2=t2*i
        total=t1/t2
        for i,n in enumerate(input):
            if n != first or i == len(input)-1:
                second=n
                break
        if first != second:
            return format(result.count(first)*result.count(second)/float(total),'.2f')




a=wordcup()
print(a.cal([1,3,4,2]))
