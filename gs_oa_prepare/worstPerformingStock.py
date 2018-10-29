class worstperformingstock():
    def find(self,input):
        result={}
        for i in input:
            result[i[0]]=result.get(i[0],(i[2]-i[1])/float(i[1]))
        return sorted(result,key=result.get)[0]
a=worstperformingstock()
test=[[1200,100,105],[1400,50,55]]
print(a.find(test))
