std1 = []
std2 = []
std3 = []
std4 = []
std5 = []

students = [std1, std2, std3, std4, std5]

for i in range(0, 5):
    students[i][0].append(input("이름을 입력하세요: "))
    students[i][1].append(int(input("수학 성적을 입력하세요:")))
    students[i][2].addend(int(input("영어 성적을 입력하세요")))

math = 0
eng = 0

for i in range(0, 5):
    math += students[i][1]
    eng += students[i][2]

math /= 5
eng /= 5

