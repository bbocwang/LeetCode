class latestStudent():
    def find(self,input):
        date=set()
        date_student={}
        m=0
        n=0
        for i in input:
            late = int(i[3])-int(i[2])
            if late < 0 : late = 0
            if i[0] not in date_student:
                date_student[i[0]]=date_student.get(i[0],{})
            date_student[i[0]].update({i[1]:str(late)})
        lateness={}
        for key,val in date_student.items():
            if key not in date:
                date.add(key)
                mean_val = 0
                for student,late_val in val.items():
                    mean_val+=int(late_val)
                mean_val/=len(val)
                for student,late_val in val.items():
                    relative_lateness=int(late_val)-mean_val
                    if relative_lateness<0: relative_lateness=0
                    if student not in lateness:
                        lateness[student]=lateness.get(student,relative_lateness)
                    else:
                        lateness[student]=lateness.get(student)+relative_lateness
        sorted_students=sorted(lateness.keys(),key = lambda x:x.lower())
        max_lateness=max(lateness.values())
        for i in sorted_students:
            if lateness[i] == max_lateness:
                return i

a=latestStudent()
test=[
["09-01","Arlene","540","570"],
["09-01","Bobby","540","543"],
["09-01","Caroline","540","530"],
["09-02","Arlene","540","580"],
["09-02","Bobby","540","580"],
["09-02","Caroline","540","595"]
]
print(a.find(test))
