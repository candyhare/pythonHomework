#Даны значения двух моментов времени, принадлежащих одним и тем же суткам: часы, минуты и секунды для каждого из моментов времени.
#Известно, что второй момент времени наступил не раньше первого.
#Определите, сколько секунд прошло между двумя моментами времени.

#Первый отрезок
firstHours = int(input())
firstMinutes = int(input())
firstSeconds = int(input())

#Второй отрезок
secondHours = int(input())
secondMinutes = int(input())
secondSeconds = int(input())

firstSum = firstHours * 3600 + firstMinutes * 60 + firstSeconds
secondSum = secondHours * 3600 + secondMinutes * 60 + secondSeconds
print(secondSum - firstSum)