#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 메뉴 
# 1. 학생 정보 등록 ( 이름, 성적)
# 2. 전체 학생 자료 출력
# 3. 학생의 정보 검색
# 4. 학생의 총점, 평균 출력


# In[ ]:


# ############################
#      학사 관리
# #############################
#  1. 학생 정보 등록
#  2. 전체 자료 조회
#  3. 특정 학생 정보 검색
#  4. 총점, 평균 출력
#  5. 종료
# ############################


# In[10]:


def print_menu():
    prt = '''############################
     학사 관리
#############################
 1. 학생 정보 등록
 2. 전체 자료 조회
 3. 특정 학생 정보 검색
 4. 총점, 평균 출력
 5. 종료
############################'''
    print(prt)

def insert():
    students = {}
    while True:
        student = input("이름과 성적 입력 ( 예: 홍기동 90 형식, 종료는 q 입력 ) > ")
        if student == 'q':
            break
        student = student.split()
        if len(student) != 2 or not student[1].isdigit():
            print("다시 입력 ")
            continue
        students[student[0]] = int(student[1])
    return students
    
def list_student(students):
    for name, score in students.items():
        print(f'{name} : {score}')
        
def search(students):
    s_name = input("검색할 학생명 입력 > ")
    if s_name in students:
        print(f'{s_name}의 성적은 {students[s_name]}')
    else:
        print(f"{s_name}의 자료는 없음")
        
def print_total(students):
    tot = 0
    for key in students:
        tot += students[key]

    print('총 인원수 : {},   총점 : {}, 평균 : {}'.format(                    len(students), tot, tot/len(students)))


# In[ ]:


import os
import time

while True:
    os.system('cls')
    print_menu()
    menu = input(" 메뉴 입력 > ")
    if menu == '5':
        break
    if menu == '1':
        students = insert()
    elif menu == '2':
        list_student(students)
    elif menu == '3':
        search(students)
    elif menu == '4':
        print_total(students)
    time.sleep(1)
    
print('\n프로그램 종료')        

