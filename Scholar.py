class Scholar:
    def __init__(self,ScholarId,ScholarName,State,Marks):
        self.ScholarId=ScholarId
        self.ScholarName=ScholarName
        self.State=State
        self.Marks=Marks

class ScholarResult:
    def __init__(self):
        self.Scholargrade=[]
    
    @classmethod
    def calculate_grade(self,ScholarGrade,grade):
        gradelist=['A','B','C','D']
        result_list=[]
        if len(ScholarGrade)>0:
            for i in ScholarGrade:
                assign_grade=''
                TotalMarks=sum(i.Marks)
                percentage=round(TotalMarks/3)
                if percentage>=80:
                    assign_grade+=gradelist[0]
                elif percentage>=60:
                    assign_grade+=gradelist[1]
                elif percentage>=50:
                    assign_grade+=gradelist[2]
                else:
                    assign_grade+=gradelist[3]
                d={}
                d['ScholarId']=i.ScholarId
                d['ScholarName']=i.ScholarName
                d['TotalMarks']=TotalMarks
                d['Grade']=assign_grade
                d['State']=i.state
                self.Scholargrade.append(d)
            result_list=[j for j in self.Scholargrade if i['Grade']==grade]
            result_list=sorted(result_list,key=lambda x:(x['TotalMarks']),reverse=True)
            return result_list
        else:
            return None

    @classmethod
    def Statewise_result(self):
        if len(self.Scholargrade)==0:
            return None
        else:
            state_ratio=[]
            states=list(set(i['State'] for i in self.Scholargrade))
            states.sort()
            for j in states:
                count_scholars=0
                count_fail=0
                for k in self.Scholargrade:
                    if k['State']==j:
                        count_scholars+=1
                        if i['Grade']=='D':
                            count_fail+=1
            fail_per=round((count_fail/count_scholars)*100)
            pass_per=round(((count_scholars-count_fail)/count_scholars)*100)
            state_ratio.append([i,f'{pass_per}:{fail_per}'])
        return state_ratio

if __name__='__main__':
    scholar_count = int(input())
    ScholarGrade = []
    for i in range(scholar_count):
        ScholarId = int(input())
        ScholarName = input()
        State = input()
        marks1 = int(input())
        marks2 = int(input())
        marks3 = int(input())
        Marks = [marks1,marks2,marks3]
        scholar_obj = Scholar(ScholarId, ScholarName, State, Marks)
        ScholarGrade.append(scholar_obj)

    grade = input().upper()
    ScholarGradeObj = ScholarResult()
    StudentListWithGrade = ScholarGradeObj.calculate_grade(ScholarGrade, grade)
    if StudentListWithGrade is None or len(StudentListWithGrade) == 0:
        print("No Record Found")
    else:
        for record in StudentListWithGrade:
            for i,j in record.items():
                print(j, end=" ")
            print()
    PassFailRatioStatewise = ScholarGradeObj.Statewise_result()
    if PassFailRatioStatewise is None:
            print("No Record Found")
    else:
        for record in PassFailRatioStatewise:
            for s in record:
                print(s, end=" ")
            print()





            




