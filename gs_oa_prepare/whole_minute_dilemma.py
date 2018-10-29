class WMD:
    def WholeMinuteDilamma(self,n):
        record={}
        for item in n:
            if 60-item != 0:
                if 60-item in record:

                    record[60-item]=record.get(60-item)+1
                else:
                    record[item]=record.get(item,1)

        ct=0
        for key,val in record.items():
            if val==2:
                ct += 1
            elif val>2:
                ct += val//2
        return ct



test=[10,20,60,50,40,30,30,30,30]
a=WMD()
print(a.WholeMinuteDilamma(test))
