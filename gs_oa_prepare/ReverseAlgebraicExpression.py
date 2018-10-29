class reverse():
    def process(self,input):
        result=[]
        num=[]
        sym=[]
        j=0
        for i,x in enumerate(input):
            if (x=='-' and i!=0 and self.is_sym(input,i-1))or(x=='-' and i==0):
                continue
            elif self.is_sym(input,i):
                result.insert(0,input[j:i])
                result.insert(0,x)
                j = i+1
        result.insert(0,input[j:len(input)])

        return ''.join(str(x) for x in result)



    def is_sym(self,input,i):
        x=input[i]
        if x == '*' or x=='+' or x=='-'or x=='/':
            return True
        else:
            return False

    def is_num(self,input,i):
        x=input[i]
        if x=='0'or x=='1'or x=='2' or x =='3' or x=='4' or x=='5'or x=='6' or x=='7' or x=='8' or x=='9':
            return True
        else:
            return False
a=reverse()
print(a.process("-11+-22-123+4*5/-66"))
