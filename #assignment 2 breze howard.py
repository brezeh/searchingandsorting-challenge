#assignment 2 breze howard

#importing os and csv file 
import os
import csv

#define the function
def main():
    data = getdata()
    firstrecords(data)

    #sort and print the records by Reading Score (ascending) and Math Score (descending)
    sortedcombined = sortbyreadingandmath(data)
    print("Records sorted by Reading Score (ascending) and Math Score (descending):")
    for student in sortedcombined[:5]:
        print(f"ID: {student['Student ID']}, Name: {student['Student Name']}, "
              f"Reading Score: {student['Reading Score']}, Math Score: {student['Math Score']}")

    #linear search for student scores
    studentid = int(input("Enter Student ID to search for scores: "))
    studentscores = linsearchid(data, studentid)
    if studentscores is not None:
        print(f"Scores for Student ID {studentid}: Reading Score: {studentscores['Reading Score']}, Math Score: {studentscores['Math Score']}")
    else:
        print(f"Student ID {studentid} not found.")
    
    #calculate average grade and pass percentage for each grade
    stats = calcpercentandave(data)
    print("\nAverage scores and pass percentages per grade:")
    for grade, stat in stats.items():
        print(f"Grade {grade}: Average Reading Score: {stat['average reading score']:.2f}, "
              f"Average Math Score: {stat['average math score']:.2f}, "
              f"Passing Percentage Reading: {stat['passing percentage reading']:.2f}%, "
              f"Passing Percentage Math: {stat['passing percentage math']:.2f}%")

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
    sorted_data = sorted(data, key=lambda x: x['Student ID'])
    print("First few records:")
    for student in sorted_data[:5]:
        print(f"ID: {student['Student ID']}, Name: {student['Student Name']}, Gender: {student['Gender']}, "
              f"Grade: {student['Grade']}, School: {student['School Name']}, "
              f"Reading Score: {student['Reading Score']}, Math Score: {student['Math Score']}")


#sorting reading score by insertion sort
def insertsortreading(data):
    size = len(data)
    for i in range(1, size):
        key = data[i]
        j = i-1
        while j >= 0 and key['Reading Score'] < data[j]['Reading Score']:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key
    return data

#sorting math score by selection sort
def selsortmath(data):
    size = len(data)
    for ind in range(size):
        max_index = ind
        for j in range(ind + 1, size):
            if data[j]['Math Score'] > data[max_index]['Math Score']:
               max_index = j
        data[ind], data[max_index] = data[max_index], data[ind]
    return data

#sort data by Reading Score (ascending) and Math Score (descending)
def sortbyreadingandmath(data):
    sortedbyreading = insertsortreading(data)
    sortedcombined = selsortmath(sortedbyreading)
    return sortedcombined

#linear search by student id
def linsearchid(data, studentid):
    for student in data:
        if student['Student ID'] == studentid:
            return student
    return None

#binary search by reading score
def binarysort(data, readingscore):
    low, high = 0, len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid]['Reading Score'] == readingscore:
            return data[mid]
        elif data[mid]['Reading Score'] < readingscore:
            low = mid + 1
        else:
            high = mid - 1
    return None

#calculate average grade and pass percentage for each grade
def calcpercentandave(data):
    gradestats = {}
    grades = set(student['Grade'] for student in data)
    for grade in grades:
        gradedata = [student for student in data if student['Grade'] == grade]
        averagereading = sum(student['Reading Score'] for student in gradedata) / len(gradedata)
        averagemath = sum(student['Math Score'] for student in gradedata) / len(gradedata)
        passingreading = (sum(1 for student in gradedata if student['Reading Score'] >= 70) / len(gradedata)) * 100
        passingmath = (sum(1 for student in gradedata if student['Math Score'] >= 70) / len(gradedata)) * 100
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