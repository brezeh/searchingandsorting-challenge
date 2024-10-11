#assignment 2 breze howard

#importing os and csv file 
import os
import csv

#define the function
def main():
    data = getdata()
    firstrecords(data)
    selsortmath(data)
    insertsortreading(data)
    linsearchid(data, studentid)
    binarysort(data, readingscore)
    calcpercentandave(data)

    #sort by math score (descending)
    sortedmath = selsortmath(data.copy())
    print("Top records sorted by Math Score (descending):")
    print(sortedmath.head())

    #sort by reading score (ascending)
    sortedreading = insertsortreading(data.copy())
    print("Top records sorted by Reading Score (ascending):")
    print(sortedreading.head())

    #linear search for student scores
    studentid = int(input("Enter Student ID to search for scores: "))
    studentscores = linsearchid(data, studentid)
    if studentscores is not None:
        print(f"Scores for Student ID {studentid}: {studentscores[['Reading Score', 'Math Score']]}")
    else:
        print(f"Student ID {studentid} not found.")

    #Performing binary search
    sortedreading = sortedreading.sort_values(by='Reading Score')
    readingscore = float(input("Enter Reading Score to search for student: "))
    student = binarysort(sortedreading, readingscore)
    if student is not None:
        print(f"Student with Reading Score {readingscore}: {student[['Student ID', 'Student Name']]}")
    else:
        print(f"No student found with Reading Score {readingscore}.")
    
    ##calculate average grade and pass percentage for each grade
    stats = calcpercentandave(data)
    print("Average scores and pass percentages per grade:")
    for grade, stat in stats.items():
        print(f"Grade {grade}: {stat}")

#variable
keep_going = 'y'

#getting student data
def getdata():
    with open("students_complete.csv", "r") as students: 
        get = csv.reader(students)
        next(get)
        data = []
        for info in get:
            data.append({
                'Student ID': int(info[0]),
                'Student Name': info[1],
                'Gender': info[2],
                'Grade': info[3],
                'School Name': info[4],
                'Reading Score': float(info[5]),
                'Math Score': float(info[6])
            })
    return data

#displaying first few records
def firstrecords(data):
    print(data.head())

#sorting math score by selection sort
def selsortmath(data):
    size = len(data)
    for ind in range(size):
        max_index = ind
        for j in range(ind + 1, size):
            if data.iloc[j]['Math Score'] > data.iloc[max_index]['Math Score']:
               max_index = j
            data.iloc[ind], data.iloc[max_index] = data.iloc[max_index], data.iloc[ind]
    return data

#sorting reading score by insertion sort
def insertsortreading(data):
    size = len(data)
    for i in range(1, size):
        key = data.iloc[i]
        j = i-1
        while j >= 0 and key['Reading Score'] < data.iloc[j]['Reading Score']:
            data.iloc[j+1] = data.iloc[j]
            j -= 1
            data.iloc[j+1] = key
    return data

#linear search by student id
def linsearchid(data, studentid):
    for index, row in data.iterrows():
        if row['Student ID'] == studentid:
            return row
    return None

#binary search by reading score
def binarysort(data, readingscore):
    low, high = 0, len(data) - 1
    while low <= high:
        mid = (low + high) // 2
    if data.iloc[mid]['Reading Score'] == readingscore:
        return data.iloc[mid]
    elif data.iloc[mid]['Reading Score'] < readingscore:
        low = mid + 1
    else:
        high = mid - 1
    return None

#calculate average grade and pass percentage for each grade
def calcpercentandave(data):
    gradestats = {}
    grades = data['Grade'].unique()
    for grade in grades:
        gradedata = data[data['grade'] == grade]
        averagereading = gradedata['Reading Score'].mean()
        averagemath = gradedata['Math Score'].mean()
        passingreading = (gradedata['Reading Score'] >= 70).mean() * 100
        passingmath = (gradedata['Math Score'] >= 70).mean() * 100
        gradestats[grade] = {
            'average reading score': averagereading,
            'average math score': averagemath,
            'passing percentage reading': passingreading,
            'passing percentage math': passingmath
        }
    return gradestats

#call the function and restart
while keep_going == 'y':
    main()
    keep_going = input ('would you like to run again? ')