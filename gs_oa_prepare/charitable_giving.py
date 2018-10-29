class CharitableGiving():
    def cal(self,n):
        order=[]
        rec={"A":0,"B":0,"C":0}
        for i in range(len(n)):

                a_money = rec.get("A")
                b_money = rec.get("B")
                c_money = rec.get("C")
                min_money = min(a_money,b_money,c_money)
                print("min_money:",min_money)
                if rec.get("A")==min_money:
                    min_key="A"
                elif rec.get("B")==min_money and b_money!=a_money:
                    min_key="B"
                else:
                    min_key="C"
                rec[min_key]=rec.get(min_key)+n[i]
                order.append(min_key)
                #print(" a:",a_money," b:",b_money," c:",c_money," min_key:",min_key)
        return order

a=CharitableGiving()
test=[1,2,3,4,1,3,1]
print(a.cal(test))
