class  perfectTeam():
    def differendTeams(self,skills):
        buffer = {"p":0,"c":0,"m":0,"b":0,"z":0}
        for i in skills:
            buffer[i]=buffer.get(i)+1
        result = 1
        for key,val in buffer.items():
            result*=val
        return result

a=perfectTeam()
print(a.differendTeams("pcmbzz"))
