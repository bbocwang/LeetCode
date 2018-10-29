class CodeFriends():
    def findwinner(self,erica,bob):
        score_e=0
        score_b=0
        e={"S":0,"E":0,"M":0,"H":0}
        b={"S":0,"E":0,"M":0,"H":0}
        for i in erica:
            e[i]+=1
        for i in bob:
            b[i]+=1
        score_e=1*e.get("E")+3*e.get("M")+5*e.get("H")
        score_b=1*b.get("E")+3*b.get("M")+5*b.get("H")
        if score_b > score_e:
            return "Bob"
        elif score_e > score_b:
            return "Erica"
        else:
            if e.get("H")>b.get("H"):
                return "Erica"
            elif e.get("H")<b.get("H"):
                return "Bob"
            else:
                if e.get("M")>b.get("M"):
                    return "Erica"
                elif e.get("M")<b.get("M"):
                    return "Bob"
                else:
                    if e.get("E")>b.get("E"):
                        return "Erica"
                    elif e.get("E")<b.get("E"):
                        return "Bob"
                    else:
                        return "Tie"

a=CodeFriends()
print(a.findwinner("EHH","EHH"))
