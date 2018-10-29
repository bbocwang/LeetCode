class csv_formatter():
    def format(self,input):
        sto=[]
        result=[]
        width = len(input[0].split(','))
        maxColLen=0
        for line in input:
            row = line.split(',')
            for i in row:
                maxColLen=max(maxColLen,len(i))

        for idx,line in enumerate(input):
            sto.append(line.split(','))
            for n,j in enumerate(sto[idx]):
                k=list(j)
                k.append(',')
                if n == len(sto[idx])-1:
                    k.append('\n')
                j=''.join(str(x) for x in k)
                while len(j)<maxColLen+2:
                    k = list(j)
                    k.insert(0,' ')
                    j=''.join(str(x) for x in k)
                result.append(j)
        return ''.join(str(x) for x in result)




input=[]
s1 = "Name,Course,Percent Grade,Letter Grade"
s2 = "Mark Johnson,Biology,75,B"
s3 = "Susan Smith,Mathematics,84,B+"
s4 = "Bob Doe,English,80,B+"
s5 = "Emma Knight,Physics,91,A"
s6 = "Jenny Lee,English,95,A+"
s7 = "Mark Johnson,Mathematics,100,A+"
input.append(s1)
input.append(s2)
input.append(s3)
input.append(s4)
input.append(s5)
input.append(s6)
input.append(s7)
#print(input)
a=input[1]
a=csv_formatter()
print(a.format(input))
