#Author: Faith Elledge
#Github username: Elledgef
#Date: 9/28/22
#Description: Code will return the mode, mean and median using the statistics module that is imported from pycharm

import statistics

class Student:
    def __init__(self,coursegrade,name):
        self._coursegrade = coursegrade
        self._name = name
#Both coursegrade and name are private

    def student_grade(self):
        return self._coursegrade
#This will get mean median and mode

    def  basic_stats(student_list):
        student_coursegrade_list = []
    for x in student_list:
                total.append(x.student_grade())
                mean=statistics.mean(student_coursegrade_list)
                median=statistics.median(student_coursegrade_list)
                mode=statistics.mode(student_coursegrade_list)
            #truple stats
                Truple = (Mean,Median,Mode)
                    return Truple


