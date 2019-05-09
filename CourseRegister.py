'''
Created on Oct 30, 2018

Estimate number of students eligible for a course

@author: lufei Guan
'''


def processProgramFile(ProgramFilePath):    # Create a function to return program name and a dictionary for program details.
    import os
    File = open(ProgramFilePath)
    ProgramName = File.readline().strip()
    Text = File.read().split('\n')

    DictProgram = {}    
    for i in range(len(Text)):
        Tuple = Text[i]
        DictProgram[Tuple[0:4]] = Tuple[5:].strip()
        i += 1
        
    return ProgramName, DictProgram



def processPrereqsFile(PrereqsFilePath):    # Return a dictionary of pre-requests for each course
    import os
    File = open(PrereqsFilePath)
    Text = File.read().split('\n')
    
    DictPrereqs = {}
    for i in range(len(Text)):
        Tuple = Text[i]
        DictPrereqs[Tuple[0:4]] = Tuple[5:].strip()
            
    return DictPrereqs




def processClassFiles(ClassListSubfolderPath):  # Return a dictionary of course to see who has taken the course.
    import os
    FileNameList = os.listdir(ClassListSubfolderPath)
    CourseList = set()
    for FileName in FileNameList:
        if FileName.startswith("c") and FileName[1].isdigit():
            CourseNum = FileName[1:5]
            CourseList.add(CourseNum)
    CourseList = list(CourseList)
    
    DictCourseTaken = {}
    for i in range(len(CourseList)):
        StudentList = []
        for j in range(len(FileNameList)):
            
            if CourseList[i] == FileNameList[j][1:5]:
                ClassFile = open(ClassListSubfolderPath+"\\"+FileNameList[j])
                ClassFileText = ClassFile.readlines()
                StudentList = StudentList + ClassFileText
                DictCourseTaken[CourseList[i]] = StudentList
                j += 1
            else:
                j += 1       
        i += 1
    
    for key in DictCourseTaken:
        value = DictCourseTaken.get(key)
        for i in range(len(value)):
            value[i] = value[i].split()[0]
            
    for key in DictCourseTaken:
        DictCourseTaken[key] = set(DictCourseTaken.get(key))

    
    return DictCourseTaken




def initFromFiles(SubfolderPath):   # Call the three functions above.
    CourseInfoTuple = processProgramFile(SubfolderPath+"\\program1.txt"), processPrereqsFile(SubfolderPath+"\\prereqs.txt"), processClassFiles(SubfolderPath)    
    return CourseInfoTuple




def studentList(SubfolderPath): # Return a set of all the students' names.
    import os
    FileNameList = os.listdir(SubfolderPath)
    NameList = []
    for i in range(len(FileNameList)):
        if FileNameList[i].startswith("c") and FileNameList[i][1].isdigit():
            ClassFile = open(SubfolderPath+"\\"+FileNameList[i])
            ClassFileText = ClassFile.readlines()
            NameList = NameList + ClassFileText
    
    for i in range(len(NameList)):
        NameList[i] = NameList[i].split()[0]
    
    NameSet = set(NameList)    
    
    return NameSet



def courseList(SubfolderPath):  # Return a list of all the courses.
    import os
    FileNameList = os.listdir(SubfolderPath)
    CourseList = set()
    for FileName in FileNameList:
        if FileName.startswith("c") and FileName[1].isdigit():
            CourseNum = FileName[1:5]
            CourseList.add(CourseNum)
    CourseList = list(CourseList)
    return CourseList



def estimateClass(CourseNum, SubfolderPath):    # Return a set of eligible students for a course.
    CourseNum = str(CourseNum)
    CourseInfoTuple = initFromFiles(SubfolderPath)
    Prereqs = CourseInfoTuple[1]
    DictCourseTaken = CourseInfoTuple[2]
    AllStudents = studentList(SubfolderPath)
    
      
    if CourseNum in courseList(SubfolderPath):
        if CourseNum in Prereqs.keys():
            PrereqsList = Prereqs.get(CourseNum).split()
            StudentsTake = []
            StudentDonePrereqs = []
            for i in range(len(PrereqsList)):
                StudentsTake = list(DictCourseTaken.get(PrereqsList[i])) + StudentsTake
            
            for student in StudentsTake:
                if StudentsTake.count(student) == len(PrereqsList):
                    StudentDonePrereqs.append(student)
                
            StudentNotTake =  AllStudents.difference(DictCourseTaken.get(CourseNum))
            EligibleStudents = StudentNotTake.intersection(set(StudentDonePrereqs))    
              
        else:    
            EligibleStudents =  AllStudents.difference(DictCourseTaken.get(CourseNum))
            
    else:
        EligibleStudents = set()
          
    return EligibleStudents



def courseName(Subfolder):  # Return a dictionary of course numbers with course titles.
    import os
    Tuple1 = processProgramFile(Subfolder+'\\program1.txt')
    Tuple2 = processProgramFile(Subfolder+'\\program2.txt')
    
    CourseNameList = Tuple1[1].copy()
    CourseNameList.update(Tuple2[1])

    return CourseNameList


def main():
    import os
    import os.path
    
    Subfolder = input('Please enter the name of the subfolder with files:') 
    SubfolderPath = os.getcwd()+"\\"+Subfolder

    CourseNum = input('Enter course number or press enter to stop:')
    while CourseNum is not "":
        NumberOfStudents = len(estimateClass(CourseNum, SubfolderPath))
        CourseNameList = courseName(SubfolderPath)
        CourseName = CourseNameList.get(CourseNum)
        print('There are',NumberOfStudents, 'students who could take course', CourseNum, CourseName)
        CourseNum = input('Enter course number or press enter to stop:')
    else:
        print('Bye!')
    
    return

main()
    
