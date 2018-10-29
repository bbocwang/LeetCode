class AllocateSchool():
    def allocate(self,school_seat,student_score,student_pref):
        student={}
        no_school_student=0
        no_student_seat=0
        for i,x in enumerate(student_score):
            student[i]=x
        order = sorted(student,key=student.get)
        order.reverse()
        for i in order:
            pref = student_pref[i]
            for idx,j in enumerate(pref):
                if school_seat[j] > 0:
                    school_seat[j]-=1
                    break
                elif idx == len(pref) - 1:
                    no_school_student += 1
            no_student_seat = sum(school_seat)
        return [no_student_seat,no_school_student]

a=AllocateSchool()
a1=[1,3,1,2]
a2=[990,780,830,860,920]
a3=[[3,2,1],[3,0,0],[2,0,1],[0,1,3],[0,2,3]]
print(a.allocate(a1,a2,a3))
