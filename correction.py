# nouns 체언 품사 분리 함수
# cho, jung, jong 각각 한획씩 변경하여 사전 검색
# 갯수 다른 경우 정확한 탐색 필요
# 튜플로 중복 제거하여 최종 출력하기
#최적화 필요, 불필요 코드 삭제, 주석 필요
# cho, jung, jong 합칠 필요있음
# 함수 매개변수 지정하여 호환 잘 되도록 수정

from konlpy.tag import *
# -*- coding: utf-8 -*-
hannanum = Hannanum()

import re
#print("test")
# 유니코드 한글 시작 : 44032, 끝 : 55199
BASE_CODE, CHOSUNG, JUNGSUNG = 44032, 588, 28

CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
                #0     1     2     3     4     5     6     7     8     9     10    11    12    13    14    15    16    17    18
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
            #      0    1     2     3     4     5     6     7     8      9    10    11    12    13    14    15    16    17    18     19     20  
JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
              #   0    1     2     3     4     5     6     7     8     9     10    11    12    13    14    15    16    17    18    19    20    21    22    23     24    25  26    27
word_upgrade = []

primary = ""

def nouns (text) :
    global primary
    test = hannanum.pos(text)
    n = []
    #print(test)
    for i in range(0, len(test)) :
        test1 = str(test[i])
        app1 = ""
    
        if test1[-3] == "N" :
            for k in range(2, len(test1)-7) :
                app1 += test1[k]
            n.append(app1)

    f = open('체언_상세.txt', 'rt', encoding='UTF8')
    n_data = f.read()
    n_err = []
    count = 0
    
    for i in n :
        if i not in n_data:
            #print("%d번째 체언 오류의심 " %(count+1))
            count += 1
            n_err.append(i)
            #print(i)
            #print("\n")
    f.close()
    
    return n_err
    
#n_err = nouns("가귀 고쇠 남배 선퓽기 여러가지 구구마 낙공 오글 ")

def nouns_case (text) :
    global primary
    lst = []
    
    test = hannanum.pos(text)
    n = []
    
    for i in range(0, len(test)) :
        test1 = str(test[i])
        app1 = ""
    
        if test1[-3] == "N" :
            for k in range(2, len(test1)-7) :
                app1 += test1[k]
            n.append(app1)

    f = open('체언_상세.txt', 'rt', encoding='UTF8')
    n_data = f.read()
    count = 0
    
    for i in n :
        if i not in n_data:
            #print("%d번째 체언 오류의심 " %count)
            #print(i)
            lst.append(count)
            count += 1        
    f.close()
    #print(lst)
    
    return lst

def cho(text, lst) :
    global primary
    #n_err = nouns("구구마 가귀 고쇠 남배 선퓽기 여러가지 낙공 오글")
    err_lst = []

    for e in range(0, len(text)): # 에러 단어 개수만큼 반복
        
        word = ""
        
        err = str(text[e]) # 다음 반복문을 위함
        fix = ""
        
        for w in range (0, len(err)): # 공백 제거 한글자씩 접근
            check = 0
            ch11 = 0
            cnt = 0
            for q in range(0, 31) :
                ## 영어인 경우 구분해서 작성함. 
                check = 0
                if '가'<=err[w]<='힣':
                    ## 588개 마다 초성이 바뀜. 
                    ch1 = (ord(err[w]) - ord('가'))//588
                    #print(ch1)
                    #print(check)
                    #check = 0
                    if ch1 == 0 and check == 0 and q == 0 : #ㄱ  ㄴ
                        #print("엥?")
                        ch11 = 2
                        check = 1
                    if ch1 == 0 and check == 0 and q == 1 : #ㄱ  ㄹ
                        ch11 = 5
                        check = 1
                    
                    
                    if ch1 == 2 and check == 0 and q == 2 : # ㄴ ㄷ
                        ch11 = 3
                        check = 1
                    if ch1 == 2 and check == 0 and q == 3 : # ㄴ ㅁ
                        ch11 = 6
                        check = 1
                    if ch1 == 2 and check == 0 and q == 4 : # ㄴ ㅂ
                        ch11 = 7
                        check = 1
                    
                        
                    
                    if ch1 == 3 and check == 0 and q == 5 : # ㄷ ㄴ
                        ch11 = 2
                        check = 1
                    if ch1 == 3 and check == 0 and q == 6 : # ㄷ ㅂ
                        ch11 = 7
                        check = 1
                    
                    if ch1 == 5 and check == 0 and q == 7 : # ㄹ ㄱ
                        ch11 = 0
                        check = 1
                    if ch1 == 5 and check == 0 and q == 8 : # ㄹ ㅅ
                        ch11 = 9
                        check = 1
                        
                    if ch1 == 6 and check == 0 and q == 9 : #ㅁ ㄴ
                        ch11 = 2
                        check = 1
                    if ch1 == 6 and check == 0 and q == 10 : # ㅁ ㅂ
                        ch11 = 7
                        check = 1
                    
                    if ch1 == 7 and check == 0 and q == 11 : # ㅂ ㄷ
                        ch11 = 3
                        check = 1
                    if ch1 == 7 and check == 0 and q == 12 : # ㅂ ㅁ
                        ch11 = 6
                        check = 1
                    if ch1 == 7 and check == 0 and q == 13 : # ㅂ ㅈ
                        ch11 = 12
                        check = 1
                    if ch1 == 7 and check == 0 and q == 13 : # ㅂ ㅊ
                        ch11 = 14
                        check = 1
                        
                    if ch1 == 9 and check == 0 and q == 14 : # ㅅ ㄹ
                        ch11 = 5
                        check = 1
                        
                    if ch1 == 12 and check == 0 and q == 15 : # ㅈ ㅂ
                        ch11 = 7
                        check = 1
                    if ch1 == 12 and check == 0 and q == 16 : # ㅈ ㅊ
                        ch11 = 14
                        check = 1
                        
                    if ch1 == 14 and check == 0 and q == 17 : # ㅊ ㅂ
                        ch11 = 7
                        check = 1
                    if ch1 == 14 and check == 0 and q == 18 : # ㅊ ㅈ
                        ch11 = 12
                        check = 1
                        
                    if ch1 == 15 and check == 0 and q == 19 : # ㅋ ㅌ
                        ch11 = 16
                        check = 1
                    if ch1 == 15 and check == 0 and q == 20 : # ㅋ ㅍ
                        ch11 = 17
                        check = 1    
                    if ch1 == 15 and check == 0 and q == 21 : # ㅋ ㅎ
                        ch11 = 18
                        check = 1
                    
                    if ch1 == 16 and check == 0 and q == 22 : # ㅌ ㅋ
                        ch11 = 15
                        check = 1
                    if ch1 == 16 and check == 0 and q == 23 : # ㅌ ㅍ
                        ch11 = 17
                        check = 1
                    if ch1 == 16 and check == 0 and q == 24 : # ㅌ ㅎ
                        ch11 = 18
                        check = 1
                    
                    if ch1 == 17 and check == 0 and q == 25 : # ㅍ ㅋ
                        ch11 = 15
                        check = 1
                    if ch1 == 17 and check == 0 and q == 26 : # ㅍ ㅌ
                        ch11 = 16
                        check = 1
                    if ch1 == 17 and check == 0 and q == 27 : # ㅍ ㅎ
                        ch11 = 18
                        check = 1
                    
                    if ch1 == 18 and check == 0 and q == 28 : # ㅎ ㅋ
                        ch11 = 15
                        check = 1
                    if ch1 == 18 and check == 0 and q == 29 : # ㅎ ㅍ
                        ch11 = 17
                        check = 1
                    if ch1 == 18 and check == 0 and q == 30 : # ㅎ ㅌ
                        ch11 = 16
                        check = 1
                    
                    #print(word)
                    #print(ch1, "ch1")
                    ch2 = ((ord(err[w]) - ord('가')) - (588*ch1)) // 28
                    #print(ch2, "ch2")
                    #print(ch2)
                    ch3 = (ord(err[w]) - ord('가')) - (588*ch1) - 28*ch2
                    #print(ch3, "ch3")
                    #print(ch3)
                    
                    if check == 1 :
                        cnt += 1
                        if cnt == 5:
                            break
                        ch = chr(44032 + ch11*588 + ch2*28 + ch3)
                        check = 2
                        ch11 = 0
                        #word += ch
                        
                        word = []
                        for p in range (0, len(text[e])) :
                            word.append(text[e][p])
                        
                        word[w] = ch
                        
                        fix = ""
                        for p in range(0, len(text[e])) :
                            fix += word[p]
                    
                        if len(fix) == len(err) :
                            f = open('체언_상세.txt', 'rt', encoding='UTF8')
                            n_data = f.read()
                            if fix in n_data :
                                    #print("%d번째 체언 오류 의심단어 수정 %s -> %s" %(e+1, err, fix))
                                    err_lst.append(fix)
                                    if e in lst :
                                        lst.remove(e)
                                    f.close()
                                    
                                    #break  # 여기서 break 하면 하나만 추출 함
                            #print(fix) # 바꿔보며 출력
                          
                            #n_data = f.read()
                            
                            #if fix in n_data :
                            #    print("체언 오류 수정 %s -> %s" %(err, fix))
                            #    f.close()
                            #    
                            #    break    
                            #else :
                                
                             #   a+=1
    
                #print(fix)
    return err_lst

def cho_upgrade(text, lst) :
    global primary
    #n_err = nouns("구구마 가귀 고쇠 남배 선퓽기 여러가지 낙공 오글")
    #print(lst)
    err_lst = []

    for e in range(0, len(lst)): # 에러 단어 개수만큼 반복
        
        word = ""
        
        
        #print(text)
        err = str(text[lst[e]]) # 다음 반복문을 위함
        err_upgrade = err[:-1]
        
        if len(err_upgrade) >= 2 :
            f = open('체언_상세.txt', 'rt', encoding='UTF8')
            n_data = f.read()
            if err_upgrade in n_data :
                print("%d번째 의심단어 조사 혹은 용언 오류!\n%s" %(e, err_upgrade))
                word_upgrade.append(err_upgrade)
                f.close()
                return 1
                                    
        
        if len(err_upgrade) >= 2 and len(err_upgrade) <= 4 :
            for w in range (0, len(err_upgrade)): # 공백 제거 한글자씩 접근
                check = 0
                ch11 = 0
                cnt = 0
                for q in range(0, 31) :
                    ## 영어인 경우 구분해서 작성함. 
                    check = 0
                    if '가'<=err_upgrade[w]<='힣':
                        ## 588개 마다 초성이 바뀜. 
                        ch1 = (ord(err_upgrade[w]) - ord('가'))//588
                        #print(ch1)
                        #print(check)
                        #check = 0
                        if ch1 == 0 and check == 0 and q == 0 : #ㄱ  ㄴ
                            #print("엥?")
                            ch11 = 2
                            check = 1
                        if ch1 == 0 and check == 0 and q == 1 : #ㄱ  ㄹ
                            ch11 = 5
                            check = 1
                        
                        
                        if ch1 == 2 and check == 0 and q == 2 : # ㄴ ㄷ
                            ch11 = 3
                            check = 1
                        if ch1 == 2 and check == 0 and q == 3 : # ㄴ ㅁ
                            ch11 = 6
                            check = 1
                        if ch1 == 2 and check == 0 and q == 4 : # ㄴ ㅂ
                            ch11 = 7
                            check = 1
                        
                            
                        
                        if ch1 == 3 and check == 0 and q == 5 : # ㄷ ㄴ
                            ch11 = 2
                            check = 1
                        if ch1 == 3 and check == 0 and q == 6 : # ㄷ ㅂ
                            ch11 = 7
                            check = 1
                        
                        if ch1 == 5 and check == 0 and q == 7 : # ㄹ ㄱ
                            ch11 = 0
                            check = 1
                        if ch1 == 5 and check == 0 and q == 8 : # ㄹ ㅅ
                            ch11 = 9
                            check = 1
                            
                        if ch1 == 6 and check == 0 and q == 9 : #ㅁ ㄴ
                            ch11 = 2
                            check = 1
                        if ch1 == 6 and check == 0 and q == 10 : # ㅁ ㅂ
                            ch11 = 7
                            check = 1
                        
                        if ch1 == 7 and check == 0 and q == 11 : # ㅂ ㄷ
                            ch11 = 3
                            check = 1
                        if ch1 == 7 and check == 0 and q == 12 : # ㅂ ㅁ
                            ch11 = 6
                            check = 1
                        if ch1 == 7 and check == 0 and q == 13 : # ㅂ ㅈ
                            ch11 = 12
                            check = 1
                        if ch1 == 7 and check == 0 and q == 13 : # ㅂ ㅊ
                            ch11 = 14
                            check = 1
                            
                        if ch1 == 9 and check == 0 and q == 14 : # ㅅ ㄹ
                            ch11 = 5
                            check = 1
                            
                        if ch1 == 12 and check == 0 and q == 15 : # ㅈ ㅂ
                            ch11 = 7
                            check = 1
                        if ch1 == 12 and check == 0 and q == 16 : # ㅈ ㅊ
                            ch11 = 14
                            check = 1
                            
                        if ch1 == 14 and check == 0 and q == 17 : # ㅊ ㅂ
                            ch11 = 7
                            check = 1
                        if ch1 == 14 and check == 0 and q == 18 : # ㅊ ㅈ
                            ch11 = 12
                            check = 1
                            
                        if ch1 == 15 and check == 0 and q == 19 : # ㅋ ㅌ
                            ch11 = 16
                            check = 1
                        if ch1 == 15 and check == 0 and q == 20 : # ㅋ ㅍ
                            ch11 = 17
                            check = 1    
                        if ch1 == 15 and check == 0 and q == 21 : # ㅋ ㅎ
                            ch11 = 18
                            check = 1
                        
                        if ch1 == 16 and check == 0 and q == 22 : # ㅌ ㅋ
                            ch11 = 15
                            check = 1
                        if ch1 == 16 and check == 0 and q == 23 : # ㅌ ㅍ
                            ch11 = 17
                            check = 1
                        if ch1 == 16 and check == 0 and q == 24 : # ㅌ ㅎ
                            ch11 = 18
                            check = 1
                        
                        if ch1 == 17 and check == 0 and q == 25 : # ㅍ ㅋ
                            ch11 = 15
                            check = 1
                        if ch1 == 17 and check == 0 and q == 26 : # ㅍ ㅌ
                            ch11 = 16
                            check = 1
                        if ch1 == 17 and check == 0 and q == 27 : # ㅍ ㅎ
                            ch11 = 18
                            check = 1
                        
                        if ch1 == 18 and check == 0 and q == 28 : # ㅎ ㅋ
                            ch11 = 15
                            check = 1
                        if ch1 == 18 and check == 0 and q == 29 : # ㅎ ㅍ
                            ch11 = 17
                            check = 1
                        if ch1 == 18 and check == 0 and q == 30 : # ㅎ ㅌ
                            ch11 = 16
                            check = 1
                        
                        #print(word)
                        #print(ch1, "ch1")
                        ch2 = ((ord(err_upgrade[w]) - ord('가')) - (588*ch1)) // 28
                        #print(ch2, "ch2")
                        #print(ch2)
                        ch3 = (ord(err_upgrade[w]) - ord('가')) - (588*ch1) - 28*ch2
                        #print(ch3, "ch3")
                        #print(ch3)
                        
                        if check == 1 :
                            cnt += 1
                            if cnt == 5:
                                break
                            ch = chr(44032 + ch11*588 + ch2*28 + ch3)
                            check = 2
                            ch11 = 0
                            #word += ch
                            
                            word = []
                            for p in range (0, len(text[lst[e]])-1) :
                                word.append(text[lst[e]][p])
                            
                            word[w] = ch
                            
                            fix = ""
                            for p in range(0, len(text[lst[e]])-1) :
                                fix += word[p]
                        
                            if len(fix) == len(err_upgrade) :
                                f = open('체언_상세.txt', 'rt', encoding='UTF8')
                                n_data = f.read()
                                if fix in n_data :
                                        #print("%d번째 체언 오류 의심단어 수정 %s -> %s" %(e, err_upgrade, fix))
                                        primary = primary.replace(err_upgrade, fix, 1)                                       
                                        f.close()
                                    
                                    #break  # 여기서 break 하면 하나만 추출 함
                            #print(fix) # 바꿔보며 출력
                          
                            #n_data = f.read()
                            
                            #if fix in n_data :
                            #    print("체언 오류 수정 %s -> %s" %(err, fix))
                            #    f.close()
                            #    
                            #    break    
                            #else :
                                
                             #   a+=1
    
                #print(fix)

def jung(text, lst) :
    err_lst = []
    #n_err = nouns("구구마 가귀 고쇠 남배 선퓽기 여러가지 낙공 오글")
    global primary
    for e in range(0, len(text)): # 에러 단어 개수만큼 반복
        
        word = ""
        
        err = str(text[e]) # 다음 반복문을 위함
        fix = ""
        
        for w in range (0, len(err)): # 공백 제거 한글자씩 접근
            check = 0
            ch11 = 0
            cnt = 0
            for q in range(0, 57) :
                ## 영어인 경우 구분해서 작성함. 
                check = 0
                if '가'<=err[w]<='힣':
                    ## 588개 마다 초성이 바뀜. 
                    ch1 = (ord(err[w]) - ord('가'))//588

                    ch2 = ((ord(err[w]) - ord('가')) - (588*ch1)) // 28
                    #print(ch2, "ch2")
                    if ch2 == 0 and check == 0 and q == 0 : #ㅏ ㅗ
                        ch22 = 8
                        check = 1
                    if ch2 == 0 and check == 0 and q == 1 : #ㅏ ㅠ
                        ch22 = 17
                        check = 1
                    if ch2 == 0 and check == 0 and q == 2 : #ㅏ ㅡ
                        ch22 = 18
                        check = 1
                    if ch2 == 0 and check == 0 and q == 3 : #ㅏ ㅕ
                        ch22 = 6
                        check = 1
                        
                        
                    if ch2 == 2 and check == 0 and q == 4 : #ㅑ ㅓ
                        ch22 = 4
                        check = 1
                    if ch2 == 2 and check == 0 and q == 5 : #ㅑ ㅛ
                        ch22 = 12
                        check = 1
                    if ch2 == 2 and check == 0 and q == 6 : #ㅑ ㅜ
                        ch22 = 13
                        check = 1
                    if ch2 == 2 and check == 0 and q == 7 : #ㅑ ㅣ
                        ch22 = 20
                        check = 1
                        
                        
                    if ch2 == 4 and check == 0 and q == 8 : #ㅓ ㅑ
                        ch22 = 2
                        check = 1
                    if ch2 == 4 and check == 0 and q == 9 : #ㅓ ㅛ
                        ch22 = 12
                        check = 1
                    if ch2 == 4 and check == 0 and q == 10 : # ㅓ ㅜ
                        ch22 = 13
                        check = 1
                    if ch2 == 4 and check == 0 and q == 11 : # ㅓ ㅣ
                        ch22 = 20
                        check = 1
                        
                        
                    if ch2 == 6 and check == 0 and q == 12 : #ㅕ ㅏ
                        ch22 = 0
                        check = 1
                    if ch2 == 6 and check == 0 and q == 13 : #ㅕ ㅗ
                        ch22 = 8
                        check = 1
                    if ch2 == 6 and check == 0 and q == 13 : #ㅕ ㅠ
                        ch22 = 17
                        check = 1
                    if ch2 == 6 and check == 0 and q == 14 : #ㅕ ㅣ
                        ch22 = 20
                        check = 1
                        
                        
                    if ch2 == 8 and check == 0 and q == 15 : #ㅗ ㅏ
                        ch22 = 0
                        check = 1
                    if ch2 == 8 and check == 0 and q == 16 : #ㅗ ㅕ
                        ch22 = 6
                        check = 1
                    if ch2 == 8 and check == 0 and q == 17 : #ㅗ ㅛ
                        ch22 = 12
                        check = 1
                       ########################################################################################### 
                    if ch2 == 8 and check == 0 and q == 19 : #ㅗ ㅜ
                        ch22 = 13
                        check = 1
                    if ch2 == 8 and check == 0 and q == 20 : #ㅗ ㅠ
                        ch22 = 17
                        check = 1    
                    if ch2 == 8 and check == 0 and q == 21 : #ㅗ ㅣ
                        ch22 = 20
                        check = 1
                        
                        
                    if ch2 == 12 and check == 0 and q == 22 : #ㅛ ㅑ
                        ch22 = 2
                        check = 1
                    if ch2 == 12 and check == 0 and q == 23 : #ㅛ ㅜ
                        ch22 = 13
                        check = 1
                    if ch2 == 12 and check == 0 and q == 24 : #ㅛ ㅠ
                        ch22 = 17
                        check = 1
                    if ch2 == 12 and check == 0 and q == 25 : #ㅛ ㅡ
                        ch22 = 18
                        check = 1
                        
                        
                    if ch2 == 13 and check == 0 and q == 26 : #ㅜ ㅏ
                        ch22 = 0
                        check = 1
                    if ch2 == 13 and check == 0 and q == 27 : #ㅜ ㅓ
                        ch22 = 4
                        check = 1
                    if ch2 == 13 and check == 0 and q == 28 : #ㅜ ㅗ
                        ch22 = 8
                        check = 1
                    if ch2 == 13 and check == 0 and q == 29 : #ㅜ ㅛ
                        ch22 = 12
                        check = 1
                    if ch2 == 13 and check == 0 and q == 30 : #ㅜ ㅠ
                        ch22 = 17
                        check = 1
                    if ch2 == 13 and check == 0 and q == 31: #ㅜ ㅣ
                        ch22 = 20
                        check = 1
                        
                        
                    if ch2 == 17 and check == 0 and q == 32: #ㅠ ㅏ
                        ch22 = 0
                        check = 1
                    if ch2 == 17 and check == 0 and q == 33 : #ㅠ ㅕ
                        ch22 = 6
                        check = 1
                    if ch2 == 17 and check == 0 and q == 34 : #ㅠ ㅗ
                        ch22 = 8
                        check = 1
                    if ch2 == 17 and check == 0 and q == 35 : #ㅠ ㅛ
                        ch22 = 12
                        check = 1
                    if ch2 == 17 and check == 0 and q == 36 : #ㅠ ㅜ
                        ch22 = 13
                        check = 1
                    if ch2 == 17 and check == 0 and q == 37 : #ㅠ ㅡ
                        ch22 = 18
                        check = 1
                        
                        
                    if ch2 == 1 and check == 0 and q == 38 : #ㅐ ㅔ
                        ch22 = 5
                        check = 1
                    if ch2 == 1 and check == 0 and q == 39 : #ㅐ ㅘ
                        ch22 = 9
                        check = 1
                    if ch2 == 1 and check == 0 and q == 40 : #ㅐ ㅝ
                        ch22 = 14
                        check = 1
                        
                        
                    if ch2 == 5 and check == 0 and q == 41 : #ㅔ ㅐ
                        ch22 = 1
                        check = 1
                    if ch2 == 5 and check == 0 and q == 42 : #ㅔ ㅝ
                        ch22 = 14
                        check = 1
                        
                        
                    if ch2 == 9 and check == 0 and q == 43 : #ㅘ ㅐ
                        ch22 = 1
                        check = 1
                        
                        
                    if ch2 == 14 and check == 0 and q == 44 : #ㅝ ㅐ
                        ch22 = 1
                        check = 1
                        
                        
                    if ch2 == 14 and check == 0 and q == 45 : #ㅝ ㅔ
                        ch22 = 5
                        check = 1
                        
                        
                    if ch2 == 10 and check == 0 and q == 46 : #ㅙ ㅞ
                        ch22 = 15
                        check = 1
                    
                    if ch2 == 15 and check == 0 and q == 47 : #ㅞ ㅙ
                        ch22 = 10
                        check = 1
                    
                    if ch2 == 18 and check == 0 and q == 48 : #ㅡ ㅓ
                        ch22 = 15
                        check = 4
                    if ch2 == 18 and check == 0 and q == 49 : #ㅡ ㅏ
                        ch22 = 15
                        check = 0
                    if ch2 == 18 and check == 0 and q == 50 : #ㅡ ㅛ
                        ch22 = 15
                        check = 12
                    if ch2 == 18 and check == 0 and q == 51 : #ㅡ ㅠ
                        ch22 = 15
                        check = 17
                    
                    if ch2 == 20 and check == 0 and q == 52 : #ㅣ ㅑ
                        ch22 = 2
                        check = 1
                    if ch2 == 20 and check == 0 and q == 53 : #ㅣ ㅕ
                        ch22 = 6
                        check = 1
                    if ch2 == 20 and check == 0 and q == 54 : #ㅣ ㅗ
                        ch22 = 8
                        check = 1
                    if ch2 == 20 and check == 0 and q == 55 : #ㅣ ㅜ
                        ch22 = 13
                        check = 1
                    if ch2 == 20 and check == 0 and q == 56 : #ㅣ ㅠ
                        ch22 = 17
                        check = 1
                        
                    ch3 = (ord(err[w]) - ord('가')) - (588*ch1) - 28*ch2
                    #print(ch3, "ch3")
                    
                    
                    if check == 1 :
                        cnt += 1
                        if cnt == 7:
                            break
                        ch = chr(44032 + ch1*588 + ch22*28 + ch3)
                        check = 2
                        ch22 = 0
                        #word += ch
                        
                        word = []
                        for p in range (0, len(text[e])) :
                            word.append(text[e][p])
                        
                        word[w] = ch
                        
                        fix = ""
                        for p in range(0, len(text[e])) :
                            fix += word[p]
                    
                        if len(fix) == len(err) :
                            f = open('체언_상세.txt', 'rt', encoding='UTF8')


                            n_data = f.read()
                            if fix in n_data :
                                    #print("%d번째 체언 오류 의심단어 수정 %s -> %s" %(e, err, fix))
                                    err_lst.append(fix)
                                    if e in lst :
                                        lst.remove(e)
                                    f.close()
                                    
                                
                                    #break  # 여기서 break 하면 하나만 추출 함
                            #print(fix) # 바꿔보며 출력
    return err_lst

def jung_upgrade(text, lst) :
    err_lst = []
    global primary
    #n_err = nouns("구구마 가귀 고쇠 남배 선퓽기 여러가지 낙공 오글")
    for e in range(0, len(lst)): # 에러 단어 개수만큼 반복
        
        word = ""
        
        err = str(text[lst[e]]) # 다음 반복문을 위함
        err_upgrade = err[:-1]
        fix = ""
        
        if len(err_upgrade) >= 2 :
            f = open('체언_상세.txt', 'rt', encoding='UTF8')
            n_data = f.read()
            if err_upgrade in n_data :
                print("%d번째 의심단어 조사 혹은 용언 오류!\n%s" %(e, err_upgrade))
                word_upgrade.append(err_upgrade)
                f.close()
                return 1
        
        
        if len(err_upgrade) >= 2 and len(err_upgrade) <= 4 :
            for w in range (0, len(err_upgrade)): # 공백 제거 한글자씩 접근
                check = 0
                ch11 = 0
                cnt = 0
                for q in range(0, 57) :
                    ## 영어인 경우 구분해서 작성함. 
                    check = 0
                    if '가'<=err_upgrade[w]<='힣':
                            ## 588개 마다 초성이 바뀜. 
                        ch1 = (ord(err_upgrade[w]) - ord('가'))//588
    
                        ch2 = ((ord(err_upgrade[w]) - ord('가')) - (588*ch1)) // 28
                        #print(ch2, "ch2")
                        if ch2 == 0 and check == 0 and q == 0 : #ㅏ ㅗ
                            ch22 = 8
                            check = 1
                        if ch2 == 0 and check == 0 and q == 1 : #ㅏ ㅠ
                            ch22 = 17
                            check = 1
                        if ch2 == 0 and check == 0 and q == 2 : #ㅏ ㅡ
                            ch22 = 18
                            check = 1
                        if ch2 == 0 and check == 0 and q == 3 : #ㅏ ㅕ
                            ch22 = 6
                            check = 1
                            
                            
                        if ch2 == 2 and check == 0 and q == 4 : #ㅑ ㅓ
                            ch22 = 4
                            check = 1
                        if ch2 == 2 and check == 0 and q == 5 : #ㅑ ㅛ
                            ch22 = 12
                            check = 1
                        if ch2 == 2 and check == 0 and q == 6 : #ㅑ ㅜ
                            ch22 = 13
                            check = 1
                        if ch2 == 2 and check == 0 and q == 7 : #ㅑ ㅣ
                            ch22 = 20
                            check = 1
                            
                            
                        if ch2 == 4 and check == 0 and q == 8 : #ㅓ ㅑ
                            ch22 = 2
                            check = 1
                        if ch2 == 4 and check == 0 and q == 9 : #ㅓ ㅛ
                            ch22 = 12
                            check = 1
                        if ch2 == 4 and check == 0 and q == 10 : # ㅓ ㅜ
                            ch22 = 13
                            check = 1
                        if ch2 == 4 and check == 0 and q == 11 : # ㅓ ㅣ
                            ch22 = 20
                            check = 1
                            
                            
                        if ch2 == 6 and check == 0 and q == 12 : #ㅕ ㅏ
                            ch22 = 0
                            check = 1
                        if ch2 == 6 and check == 0 and q == 13 : #ㅕ ㅗ
                            ch22 = 8
                            check = 1
                        if ch2 == 6 and check == 0 and q == 13 : #ㅕ ㅠ
                            ch22 = 17
                            check = 1
                        if ch2 == 6 and check == 0 and q == 14 : #ㅕ ㅣ
                            ch22 = 20
                            check = 1
                            
                            
                        if ch2 == 8 and check == 0 and q == 15 : #ㅗ ㅏ
                            ch22 = 0
                            check = 1
                        if ch2 == 8 and check == 0 and q == 16 : #ㅗ ㅕ
                            ch22 = 6
                            check = 1
                        if ch2 == 8 and check == 0 and q == 17 : #ㅗ ㅛ
                            ch22 = 12
                            check = 1
                           ########################################################################################### 
                        if ch2 == 8 and check == 0 and q == 19 : #ㅗ ㅜ
                            ch22 = 13
                            check = 1
                        if ch2 == 8 and check == 0 and q == 20 : #ㅗ ㅠ
                            ch22 = 17
                            check = 1    
                        if ch2 == 8 and check == 0 and q == 21 : #ㅗ ㅣ
                            ch22 = 20
                            check = 1
                            
                            
                        if ch2 == 12 and check == 0 and q == 22 : #ㅛ ㅑ
                            ch22 = 2
                            check = 1
                        if ch2 == 12 and check == 0 and q == 23 : #ㅛ ㅜ
                            ch22 = 13
                            check = 1
                        if ch2 == 12 and check == 0 and q == 24 : #ㅛ ㅠ
                            ch22 = 17
                            check = 1
                        if ch2 == 12 and check == 0 and q == 25 : #ㅛ ㅡ
                            ch22 = 18
                            check = 1
                            
                            
                        if ch2 == 13 and check == 0 and q == 26 : #ㅜ ㅏ
                            ch22 = 0
                            check = 1
                        if ch2 == 13 and check == 0 and q == 27 : #ㅜ ㅓ
                            ch22 = 4
                            check = 1
                        if ch2 == 13 and check == 0 and q == 28 : #ㅜ ㅗ
                            ch22 = 8
                            check = 1
                        if ch2 == 13 and check == 0 and q == 29 : #ㅜ ㅛ
                            ch22 = 12
                            check = 1
                        if ch2 == 13 and check == 0 and q == 30 : #ㅜ ㅠ
                            ch22 = 17
                            check = 1
                        if ch2 == 13 and check == 0 and q == 31: #ㅜ ㅣ
                            ch22 = 20
                            check = 1
                            
                            
                        if ch2 == 17 and check == 0 and q == 32: #ㅠ ㅏ
                            ch22 = 0
                            check = 1
                        if ch2 == 17 and check == 0 and q == 33 : #ㅠ ㅕ
                            ch22 = 6
                            check = 1
                        if ch2 == 17 and check == 0 and q == 34 : #ㅠ ㅗ
                            ch22 = 8
                            check = 1
                        if ch2 == 17 and check == 0 and q == 35 : #ㅠ ㅛ
                            ch22 = 12
                            check = 1
                        if ch2 == 17 and check == 0 and q == 36 : #ㅠ ㅜ
                            ch22 = 13
                            check = 1
                        if ch2 == 17 and check == 0 and q == 37 : #ㅠ ㅡ
                            ch22 = 18
                            check = 1
                            
                            
                        if ch2 == 1 and check == 0 and q == 38 : #ㅐ ㅔ
                            ch22 = 5
                            check = 1
                        if ch2 == 1 and check == 0 and q == 39 : #ㅐ ㅘ
                            ch22 = 9
                            check = 1
                        if ch2 == 1 and check == 0 and q == 40 : #ㅐ ㅝ
                            ch22 = 14
                            check = 1
                            
                            
                        if ch2 == 5 and check == 0 and q == 41 : #ㅔ ㅐ
                            ch22 = 1
                            check = 1
                        if ch2 == 5 and check == 0 and q == 42 : #ㅔ ㅝ
                            ch22 = 14
                            check = 1
                            
                            
                        if ch2 == 9 and check == 0 and q == 43 : #ㅘ ㅐ
                            ch22 = 1
                            check = 1
                            
                            
                        if ch2 == 14 and check == 0 and q == 44 : #ㅝ ㅐ
                            ch22 = 1
                            check = 1
                            
                            
                        if ch2 == 14 and check == 0 and q == 45 : #ㅝ ㅔ
                            ch22 = 5
                            check = 1
                            
                            
                        if ch2 == 10 and check == 0 and q == 46 : #ㅙ ㅞ
                            ch22 = 15
                            check = 1
                        
                        if ch2 == 15 and check == 0 and q == 47 : #ㅞ ㅙ
                            ch22 = 10
                            check = 1
                        
                        if ch2 == 18 and check == 0 and q == 48 : #ㅡ ㅓ
                            ch22 = 15
                            check = 4
                        if ch2 == 18 and check == 0 and q == 49 : #ㅡ ㅏ
                            ch22 = 15
                            check = 0
                        if ch2 == 18 and check == 0 and q == 50 : #ㅡ ㅛ
                            ch22 = 15
                            check = 12
                        if ch2 == 18 and check == 0 and q == 51 : #ㅡ ㅠ
                            ch22 = 15
                            check = 17
                        
                        if ch2 == 20 and check == 0 and q == 52 : #ㅣ ㅑ
                            ch22 = 2
                            check = 1
                        if ch2 == 20 and check == 0 and q == 53 : #ㅣ ㅕ
                            ch22 = 6
                            check = 1
                        if ch2 == 20 and check == 0 and q == 54 : #ㅣ ㅗ
                            ch22 = 8
                            check = 1
                        if ch2 == 20 and check == 0 and q == 55 : #ㅣ ㅜ
                            ch22 = 13
                            check = 1
                        if ch2 == 20 and check == 0 and q == 56 : #ㅣ ㅠ
                            ch22 = 17
                            check = 1
                            
                        ch3 = (ord(err_upgrade[w]) - ord('가')) - (588*ch1) - 28*ch2
                        #print(ch3, "ch3")
                        
                        
                        if check == 1 :
                            cnt += 1
                            if cnt == 7:
                                break
                            ch = chr(44032 + ch1*588 + ch22*28 + ch3)
                            check = 2
                            ch22 = 0
                            #word += ch
                            
                            word = []
                            for p in range (0, len(text[lst[e]])-1) :
                                word.append(text[lst[e]][p])
                            
                            word[w] = ch
                            
                            fix = ""
                            for p in range(0, len(text[lst[e]])-1) :
                                fix += word[p]
                        
                            if len(fix) == len(err_upgrade) :
                                f = open('체언_상세.txt', 'rt', encoding='UTF8')
                                n_data = f.read()
                                if fix in n_data :
                                        print("%d번째 체언 오류 의심단어 수정 %s -> %s" %(e, err_upgrade, fix))
                                        err_lst.append(fix)
                                        primary = primary.replace(err_upgrade, fix, 1)
                                        f.close()
                                    
                                    #break  # 여기서 break 하면 하나만 추출 함
                            #print(fix) # 바꿔보며 출력

def jong(text, lst) :
    err_lst = []
    global primary
    #n_err = nouns("구구마 가귀 고쇠 남배 선퓽기 여러가지 낙공 오글")
    for e in range(0, len(text)): # 에러 단어 개수만큼 반복
        
        word = ""
        
        err = str(text[e]) # 다음 반복문을 위함
        fix = ""
        
        for w in range (0, len(err)): # 공백 제거 한글자씩 접근
            check = 0
            ch11 = 0
            cnt = 0
            for q in range(0, 30) :
                ## 영어인 경우 구분해서 작성함. 
                check = 0
                if '가'<=err[w]<='힣':
                    ## 588개 마다 초성이 바뀜. 
                    ch1 = (ord(err[w]) - ord('가'))//588

                    ch2 = ((ord(err[w]) - ord('가')) - (588*ch1)) // 28
                    #print(ch2, "ch2")
                  
                    ch3 = (ord(err[w]) - ord('가')) - (588*ch1) - 28*ch2
                    #print(ch3, "ch3")
                    
                    if ch3 == 1 and check == 0 and q == 0 : #ㄱ ㄹ
                        ch33 = 8
                        check = 1
                        
                    if ch3 == 4 and check == 0 and q == 1 : #ㄴ ㄷ
                        ch33 = 8
                        check = 7
                    if ch3 == 4 and check == 0 and q == 2 : #ㄴ ㅁ
                        ch33 = 8
                        check = 16
                    if ch3 == 4 and check == 0 and q == 3 : #ㄴ ㅂ
                        ch33 = 8
                        check = 17
                    if ch3 == 4 and check == 0 and q == 4 : #ㄴ ㅊ
                        ch33 = 8
                        check = 23
                        
                    if ch3 == 7 and check == 0 and q == 5 : #ㄷ ㄴ
                        ch33 = 4
                        check = 1
                        
                    if ch3 == 8 and check == 0 and q == 6 : #ㄹ ㄱ
                        ch33 = 1
                        check = 1
                    if ch3 == 8 and check == 0 and q == 7 : #ㄹ ㅅ
                        ch33 = 19
                        check = 1
                        
                    if ch3 == 16 and check == 0 and q == 8 : #ㅁ ㄴ
                        ch33 = 4
                        check = 1
                        
                    if ch3 == 17 and check == 0 and q == 9 : #ㅂ ㄴ
                        ch33 = 4
                        check = 1
                    if ch3 == 17 and check == 0 and q == 10 : #ㅂ ㅈ
                        ch33 = 22
                        check = 1
                    if ch3 == 17 and check == 0 and q == 11 : #ㅂ ㅊ
                        ch33 = 23
                        check = 1
                    
                    if ch3 == 19 and check == 0 and q == 12 : #ㅅ ㄹ
                        ch33 = 8
                        check = 1
                        
                    if ch3 == 22 and check == 0 and q == 13 : #ㅈ ㅂ
                        ch33 = 17
                        check = 1
                    if ch3 == 22 and check == 0 and q == 14 : #ㅈ ㅊ
                        ch33 = 23
                        check = 1
                        
                    if ch3 == 23 and check == 0 and q == 15 : #ㅊ ㄴ
                        ch33 = 4
                        check = 1
                    if ch3 == 23 and check == 0 and q == 16 : #ㅊ ㅁ
                        ch33 = 16
                        check = 1
                    if ch3 == 23 and check == 0 and q == 17 : #ㅊ ㅈ
                        ch33 = 22
                        check = 1
                        
                    if ch3 == 24 and check == 0 and q == 18 : #ㅋ ㅌ
                        ch33 = 25
                        check = 1
                    if ch3 == 24 and check == 0 and q == 19 : #ㅋ ㅍ
                        ch33 = 26
                        check = 1
                    if ch3 == 24 and check == 0 and q == 20 : #ㅋ ㅎ
                        ch33 = 27
                        check = 1
                        
                    if ch3 == 25 and check == 0 and q == 21 : #ㅌ ㅍ
                        ch33 = 26
                        check = 1
                    if ch3 == 25 and check == 0 and q == 22 : #ㅌ ㅋ
                        ch33 = 24
                        check = 1
                    if ch3 == 25 and check == 0 and q == 23 : #ㅌ ㅎ
                        ch33 = 27
                        check = 1
                        
                    if ch3 == 26 and check == 0 and q == 24 : #ㅍ ㅋ
                        ch33 = 24
                        check = 1
                    if ch3 == 26 and check == 0 and q == 25 : #ㅍ ㅌ
                        ch33 = 25
                        check = 1
                    if ch3 == 26 and check == 0 and q == 26 : #ㅍ ㅎ
                        ch33 = 27
                        check = 1
                        
                    if ch3 == 27 and check == 0 and q == 27 : #ㅎ ㅋ
                        ch33 = 24
                        check = 1
                    if ch3 == 27 and check == 0 and q == 28 : #ㅎ ㅌ
                        ch33 = 25
                        check = 1
                    if ch3 == 27 and check == 0 and q == 29 : #ㅎ ㅍ
                        ch33 = 26
                        check = 1
                    
                    
                    if check == 1 :
                        cnt += 1
                        if cnt == 4:
                            break
                        ch = chr(44032 + ch1*588 + ch2*28 + ch33)
                        check = 2
                        ch33 = 0
                        #word += ch
                        
                        word = []
                        for p in range (0, len(text[e])) :
                            word.append(text[e][p])
                        
                        word[w] = ch
                        
                        fix = ""
                        for p in range(0, len(text[e])) :
                            fix += word[p]
                    
                        if len(fix) == len(err) :
                            f = open('체언_상세.txt', 'rt', encoding='UTF8')
                            n_data = f.read()
                            if fix in n_data :
                                #print("%d번째 체언 오류 의심단어 수정 %s -> %s" %(e, err, fix))
                                err_lst.append(fix)
                                if e in lst :
                                    lst.remove(e)

                                f.close()
                                
                                    #break  # 여기서 break 하면 하나만 추출 함
                                #print(fix) # 바꿔보며 출력
    return err_lst

def jong_upgrade(text, lst) :
    #n_err = nouns("구구마 가귀 고쇠 남배 선퓽기 여러가지 낙공 오글")
    err_lst = []
    global primary
    for e in range(0, len(lst)): # 에러 단어 개수만큼 반복
        
        word = ""
        
        err = str(text[lst[e]]) # 다음 반복문을 위함
        err_upgrade = err[:-1]    
        
        if len(err_upgrade) >= 2 :
            f = open('체언_상세.txt', 'rt', encoding='UTF8')
            n_data = f.read()
            if err_upgrade in n_data :
                print("%d번째 의심단어 조사 혹은 용언 오류!\n%s" %(e, err_upgrade))
                word_upgrade.append(err_upgrade)
                f.close()
                
        
        if len(err_upgrade) >= 2 and len(err_upgrade) <= 4 :
        
            for w in range (0, len(err_upgrade)): # 공백 제거 한글자씩 접근
                check = 0
                ch11 = 0
                cnt = 0
                for q in range(0, 30) :
                    ## 영어인 경우 구분해서 작성함. 
                    check = 0
                    if '가'<=err_upgrade[w]<='힣':
                        ## 588개 마다 초성이 바뀜. 
                        ch1 = (ord(err_upgrade[w]) - ord('가'))//588
    
                        ch2 = ((ord(err_upgrade[w]) - ord('가')) - (588*ch1)) // 28
                        #print(ch2, "ch2")
                      
                        ch3 = (ord(err_upgrade[w]) - ord('가')) - (588*ch1) - 28*ch2
                        #print(ch3, "ch3")
                        
                        if ch3 == 1 and check == 0 and q == 0 : #ㄱ ㄹ
                            ch33 = 8
                            check = 1
                            
                        if ch3 == 4 and check == 0 and q == 1 : #ㄴ ㄷ
                            ch33 = 8
                            check = 7
                        if ch3 == 4 and check == 0 and q == 2 : #ㄴ ㅁ
                            ch33 = 8
                            check = 16
                        if ch3 == 4 and check == 0 and q == 3 : #ㄴ ㅂ
                            ch33 = 8
                            check = 17
                        if ch3 == 4 and check == 0 and q == 4 : #ㄴ ㅊ
                            ch33 = 8
                            check = 23
                            
                        if ch3 == 7 and check == 0 and q == 5 : #ㄷ ㄴ
                            ch33 = 4
                            check = 1
                            
                        if ch3 == 8 and check == 0 and q == 6 : #ㄹ ㄱ
                            ch33 = 1
                            check = 1
                        if ch3 == 8 and check == 0 and q == 7 : #ㄹ ㅅ
                            ch33 = 19
                            check = 1
                            
                        if ch3 == 16 and check == 0 and q == 8 : #ㅁ ㄴ
                            ch33 = 4
                            check = 1
                            
                        if ch3 == 17 and check == 0 and q == 9 : #ㅂ ㄴ
                            ch33 = 4
                            check = 1
                        if ch3 == 17 and check == 0 and q == 10 : #ㅂ ㅈ
                            ch33 = 22
                            check = 1
                        if ch3 == 17 and check == 0 and q == 11 : #ㅂ ㅊ
                            ch33 = 23
                            check = 1
                        
                        if ch3 == 19 and check == 0 and q == 12 : #ㅅ ㄹ
                            ch33 = 8
                            check = 1
                            
                        if ch3 == 22 and check == 0 and q == 13 : #ㅈ ㅂ
                            ch33 = 17
                            check = 1
                        if ch3 == 22 and check == 0 and q == 14 : #ㅈ ㅊ
                            ch33 = 23
                            check = 1
                            
                        if ch3 == 23 and check == 0 and q == 15 : #ㅊ ㄴ
                            ch33 = 4
                            check = 1
                        if ch3 == 23 and check == 0 and q == 16 : #ㅊ ㅁ
                            ch33 = 16
                            check = 1
                        if ch3 == 23 and check == 0 and q == 17 : #ㅊ ㅈ
                            ch33 = 22
                            check = 1
                            
                        if ch3 == 24 and check == 0 and q == 18 : #ㅋ ㅌ
                            ch33 = 25
                            check = 1
                        if ch3 == 24 and check == 0 and q == 19 : #ㅋ ㅍ
                            ch33 = 26
                            check = 1
                        if ch3 == 24 and check == 0 and q == 20 : #ㅋ ㅎ
                            ch33 = 27
                            check = 1
                            
                        if ch3 == 25 and check == 0 and q == 21 : #ㅌ ㅍ
                            ch33 = 26
                            check = 1
                        if ch3 == 25 and check == 0 and q == 22 : #ㅌ ㅋ
                            ch33 = 24
                            check = 1
                        if ch3 == 25 and check == 0 and q == 23 : #ㅌ ㅎ
                            ch33 = 27
                            check = 1
                            
                        if ch3 == 26 and check == 0 and q == 24 : #ㅍ ㅋ
                            ch33 = 24
                            check = 1
                        if ch3 == 26 and check == 0 and q == 25 : #ㅍ ㅌ
                            ch33 = 25
                            check = 1
                        if ch3 == 26 and check == 0 and q == 26 : #ㅍ ㅎ
                            ch33 = 27
                            check = 1
                                
                        if ch3 == 27 and check == 0 and q == 27 : #ㅎ ㅋ
                            ch33 = 24
                            check = 1
                        if ch3 == 27 and check == 0 and q == 28 : #ㅎ ㅌ
                            ch33 = 25
                            check = 1
                        if ch3 == 27 and check == 0 and q == 29 : #ㅎ ㅍ
                            ch33 = 26
                            check = 1
                        
                        
                        if check == 1 :
                            cnt += 1
                            if cnt == 4:
                                break
                            ch = chr(44032 + ch1*588 + ch2*28 + ch33)
                            check = 2
                            ch33 = 0
                            #word += ch
                            
                            word = []
                            for p in range (0, len(text[lst[e]])-1) :
                                word.append(text[lst[e]][p])
                            
                            word[w] = ch
                            
                            fix = ""
                            for p in range(0, len(text[lst[e]])-1) :
                                fix += word[p]
                        
                            if len(fix) == len(err_upgrade) :
                                f = open('체언_상세.txt', 'rt', encoding='UTF8')
                                n_data = f.read()
                                if fix in n_data :
                                    #print("%d번째 체언 오류 의심단어 수정 %s -> %s" %(e, err_upgrade, fix))
                                    err_lst.append(fix)
                                    primary = primary.replace(err_upgrade, fix, 1)
                                    f.close()
                                    
                                        #break  # 여기서 break 하면 하나만 추출 함
                                    #print(fix) # 바꿔보며 출력
    return primary

def cho_filter(text, lst) :
    #n_err = nouns("구구마 가귀 고쇠 남배 선퓽기 여러가지 낙공 오글")
    global primary
    for e in range(0, len(text)): # 에러 단어 개수만큼 반복
        r_lst = []
        word = ""
        
        err = str(text[e]) # 다음 반복문을 위함
        fix = ""
        
        for w in range (0, len(err)): # 공백 제거 한글자씩 접근
            check = 0
            ch11 = 0
            cnt = 0
            for q in range(0, 31) :
                ## 영어인 경우 구분해서 작성함. 
                check = 0
                if '가'<=err[w]<='힣':
                    ## 588개 마다 초성이 바뀜. 
                    ch1 = (ord(err[w]) - ord('가'))//588
                    #print(ch1)
                    #print(check)
                    #check = 0
                    if ch1 == 0 and check == 0 and q == 0 : #ㄱ  ㄴ
                        #print("엥?")
                        ch11 = 2
                        check = 1
                    if ch1 == 0 and check == 0 and q == 1 : #ㄱ  ㄹ
                        ch11 = 5
                        check = 1
                    
                    
                    if ch1 == 2 and check == 0 and q == 2 : # ㄴ ㄷ
                        ch11 = 3
                        check = 1
                    if ch1 == 2 and check == 0 and q == 3 : # ㄴ ㅁ
                        ch11 = 6
                        check = 1
                    if ch1 == 2 and check == 0 and q == 4 : # ㄴ ㅂ
                        ch11 = 7
                        check = 1
                    
                        
                    
                    if ch1 == 3 and check == 0 and q == 5 : # ㄷ ㄴ
                        ch11 = 2
                        check = 1
                    if ch1 == 3 and check == 0 and q == 6 : # ㄷ ㅂ
                        ch11 = 7
                        check = 1
                    
                    if ch1 == 5 and check == 0 and q == 7 : # ㄹ ㄱ
                        ch11 = 0
                        check = 1
                    if ch1 == 5 and check == 0 and q == 8 : # ㄹ ㅅ
                        ch11 = 9
                        check = 1
                        
                    if ch1 == 6 and check == 0 and q == 9 : #ㅁ ㄴ
                        ch11 = 2
                        check = 1
                    if ch1 == 6 and check == 0 and q == 10 : # ㅁ ㅂ
                        ch11 = 7
                        check = 1
                    
                    if ch1 == 7 and check == 0 and q == 11 : # ㅂ ㄷ
                        ch11 = 3
                        check = 1
                    if ch1 == 7 and check == 0 and q == 12 : # ㅂ ㅁ
                        ch11 = 6
                        check = 1
                    if ch1 == 7 and check == 0 and q == 13 : # ㅂ ㅈ
                        ch11 = 12
                        check = 1
                    if ch1 == 7 and check == 0 and q == 13 : # ㅂ ㅊ
                        ch11 = 14
                        check = 1
                        
                    if ch1 == 9 and check == 0 and q == 14 : # ㅅ ㄹ
                        ch11 = 5
                        check = 1
                        
                    if ch1 == 12 and check == 0 and q == 15 : # ㅈ ㅂ
                        ch11 = 7
                        check = 1
                    if ch1 == 12 and check == 0 and q == 16 : # ㅈ ㅊ
                        ch11 = 14
                        check = 1
                        
                    if ch1 == 14 and check == 0 and q == 17 : # ㅊ ㅂ
                        ch11 = 7
                        check = 1
                    if ch1 == 14 and check == 0 and q == 18 : # ㅊ ㅈ
                        ch11 = 12
                        check = 1
                        
                    if ch1 == 15 and check == 0 and q == 19 : # ㅋ ㅌ
                        ch11 = 16
                        check = 1
                    if ch1 == 15 and check == 0 and q == 20 : # ㅋ ㅍ
                        ch11 = 17
                        check = 1    
                    if ch1 == 15 and check == 0 and q == 21 : # ㅋ ㅎ
                        ch11 = 18
                        check = 1
                    
                    if ch1 == 16 and check == 0 and q == 22 : # ㅌ ㅋ
                        ch11 = 15
                        check = 1
                    if ch1 == 16 and check == 0 and q == 23 : # ㅌ ㅍ
                        ch11 = 17
                        check = 1
                    if ch1 == 16 and check == 0 and q == 24 : # ㅌ ㅎ
                        ch11 = 18
                        check = 1
                    
                    if ch1 == 17 and check == 0 and q == 25 : # ㅍ ㅋ
                        ch11 = 15
                        check = 1
                    if ch1 == 17 and check == 0 and q == 26 : # ㅍ ㅌ
                        ch11 = 16
                        check = 1
                    if ch1 == 17 and check == 0 and q == 27 : # ㅍ ㅎ
                        ch11 = 18
                        check = 1
                    
                    if ch1 == 18 and check == 0 and q == 28 : # ㅎ ㅋ
                        ch11 = 15
                        check = 1
                    if ch1 == 18 and check == 0 and q == 29 : # ㅎ ㅍ
                        ch11 = 17
                        check = 1
                    if ch1 == 18 and check == 0 and q == 30 : # ㅎ ㅌ
                        ch11 = 16
                        check = 1
                    
                    #print(word)
                    #print(ch1, "ch1")
                    ch2 = ((ord(err[w]) - ord('가')) - (588*ch1)) // 28
                    #print(ch2, "ch2")
                    #print(ch2)
                    ch3 = (ord(err[w]) - ord('가')) - (588*ch1) - 28*ch2
                    #print(ch3, "ch3")
                    #print(ch3)
                    
                    if check == 1 :
                        cnt += 1
                        if cnt == 5:
                            break
                        ch = chr(44032 + ch11*588 + ch2*28 + ch3)
                        check = 2
                        ch11 = 0
                        #word += ch
                        
                        word = []
                        for p in range (0, len(text[e])) :
                            word.append(text[e][p])
                        
                        word[w] = ch
                        
                        fix = ""
                        for p in range(0, len(text[e])) :
                            fix += word[p]
                    
                        if len(fix) == len(err) :
                            f = open('체언_상세.txt', 'rt', encoding='UTF8')
                            n_data = f.read()
                            if fix in n_data :
                                    print("%d번째 체언 오류 의심단어 수정 %s -> %s" %(e, err, fix))
                                    if e in lst :
                                        lst.remove(e)
                                    f.close()
                                    primary = primary.replace(err, fix, 1)
                                    #break  # 여기서 break 하면 하나만 추출 함
                            #print(fix) # 바꿔보며 출력
                          
                            #n_data = f.read()
                            
                            #if fix in n_data :
                            #    print("체언 오류 수정 %s -> %s" %(err, fix))
                            #    f.close()
                            #    
                            #    break    
                            #else :
                                
                             #   a+=1
    
                #print(fix)
    return lst

def jung_filter(text, lst) :
    #n_err = nouns("구구마 가귀 고쇠 남배 선퓽기 여러가지 낙공 오글")
    global primary
    for e in range(0, len(text)): # 에러 단어 개수만큼 반복
        r_lst = []
        word = ""
        
        err = str(text[e]) # 다음 반복문을 위함
        fix = ""
        
        for w in range (0, len(err)): # 공백 제거 한글자씩 접근
            check = 0
            ch11 = 0
            cnt = 0
            for q in range(0, 57) :
                ## 영어인 경우 구분해서 작성함. 
                check = 0
                if '가'<=err[w]<='힣':
                    ## 588개 마다 초성이 바뀜. 
                    ch1 = (ord(err[w]) - ord('가'))//588

                    ch2 = ((ord(err[w]) - ord('가')) - (588*ch1)) // 28
                    #print(ch2, "ch2")
                    if ch2 == 0 and check == 0 and q == 0 : #ㅏ ㅗ
                        ch22 = 8
                        check = 1
                    if ch2 == 0 and check == 0 and q == 1 : #ㅏ ㅠ
                        ch22 = 17
                        check = 1
                    if ch2 == 0 and check == 0 and q == 2 : #ㅏ ㅡ
                        ch22 = 18
                        check = 1
                    if ch2 == 0 and check == 0 and q == 3 : #ㅏ ㅕ
                        ch22 = 6
                        check = 1
                        
                        
                    if ch2 == 2 and check == 0 and q == 4 : #ㅑ ㅓ
                        ch22 = 4
                        check = 1
                    if ch2 == 2 and check == 0 and q == 5 : #ㅑ ㅛ
                        ch22 = 12
                        check = 1
                    if ch2 == 2 and check == 0 and q == 6 : #ㅑ ㅜ
                        ch22 = 13
                        check = 1
                    if ch2 == 2 and check == 0 and q == 7 : #ㅑ ㅣ
                        ch22 = 20
                        check = 1
                        
                        
                    if ch2 == 4 and check == 0 and q == 8 : #ㅓ ㅑ
                        ch22 = 2
                        check = 1
                    if ch2 == 4 and check == 0 and q == 9 : #ㅓ ㅛ
                        ch22 = 12
                        check = 1
                    if ch2 == 4 and check == 0 and q == 10 : # ㅓ ㅜ
                        ch22 = 13
                        check = 1
                    if ch2 == 4 and check == 0 and q == 11 : # ㅓ ㅣ
                        ch22 = 20
                        check = 1
                        
                        
                    if ch2 == 6 and check == 0 and q == 12 : #ㅕ ㅏ
                        ch22 = 0
                        check = 1
                    if ch2 == 6 and check == 0 and q == 13 : #ㅕ ㅗ
                        ch22 = 8
                        check = 1
                    if ch2 == 6 and check == 0 and q == 13 : #ㅕ ㅠ
                        ch22 = 17
                        check = 1
                    if ch2 == 6 and check == 0 and q == 14 : #ㅕ ㅣ
                        ch22 = 20
                        check = 1
                        
                        
                    if ch2 == 8 and check == 0 and q == 15 : #ㅗ ㅏ
                        ch22 = 0
                        check = 1
                    if ch2 == 8 and check == 0 and q == 16 : #ㅗ ㅕ
                        ch22 = 6
                        check = 1
                    if ch2 == 8 and check == 0 and q == 17 : #ㅗ ㅛ
                        ch22 = 12
                        check = 1
                       ########################################################################################### 
                    if ch2 == 8 and check == 0 and q == 19 : #ㅗ ㅜ
                        ch22 = 13
                        check = 1
                    if ch2 == 8 and check == 0 and q == 20 : #ㅗ ㅠ
                        ch22 = 17
                        check = 1    
                    if ch2 == 8 and check == 0 and q == 21 : #ㅗ ㅣ
                        ch22 = 20
                        check = 1
                        
                        
                    if ch2 == 12 and check == 0 and q == 22 : #ㅛ ㅑ
                        ch22 = 2
                        check = 1
                    if ch2 == 12 and check == 0 and q == 23 : #ㅛ ㅜ
                        ch22 = 13
                        check = 1
                    if ch2 == 12 and check == 0 and q == 24 : #ㅛ ㅠ
                        ch22 = 17
                        check = 1
                    if ch2 == 12 and check == 0 and q == 25 : #ㅛ ㅡ
                        ch22 = 18
                        check = 1
                        
                        
                    if ch2 == 13 and check == 0 and q == 26 : #ㅜ ㅏ
                        ch22 = 0
                        check = 1
                    if ch2 == 13 and check == 0 and q == 27 : #ㅜ ㅓ
                        ch22 = 4
                        check = 1
                    if ch2 == 13 and check == 0 and q == 28 : #ㅜ ㅗ
                        ch22 = 8
                        check = 1
                    if ch2 == 13 and check == 0 and q == 29 : #ㅜ ㅛ
                        ch22 = 12
                        check = 1
                    if ch2 == 13 and check == 0 and q == 30 : #ㅜ ㅠ
                        ch22 = 17
                        check = 1
                    if ch2 == 13 and check == 0 and q == 31: #ㅜ ㅣ
                        ch22 = 20
                        check = 1
                        
                        
                    if ch2 == 17 and check == 0 and q == 32: #ㅠ ㅏ
                        ch22 = 0
                        check = 1
                    if ch2 == 17 and check == 0 and q == 33 : #ㅠ ㅕ
                        ch22 = 6
                        check = 1
                    if ch2 == 17 and check == 0 and q == 34 : #ㅠ ㅗ
                        ch22 = 8
                        check = 1
                    if ch2 == 17 and check == 0 and q == 35 : #ㅠ ㅛ
                        ch22 = 12
                        check = 1
                    if ch2 == 17 and check == 0 and q == 36 : #ㅠ ㅜ
                        ch22 = 13
                        check = 1
                    if ch2 == 17 and check == 0 and q == 37 : #ㅠ ㅡ
                        ch22 = 18
                        check = 1
                        
                        
                    if ch2 == 1 and check == 0 and q == 38 : #ㅐ ㅔ
                        ch22 = 5
                        check = 1
                    if ch2 == 1 and check == 0 and q == 39 : #ㅐ ㅘ
                        ch22 = 9
                        check = 1
                    if ch2 == 1 and check == 0 and q == 40 : #ㅐ ㅝ
                        ch22 = 14
                        check = 1
                        
                        
                    if ch2 == 5 and check == 0 and q == 41 : #ㅔ ㅐ
                        ch22 = 1
                        check = 1
                    if ch2 == 5 and check == 0 and q == 42 : #ㅔ ㅝ
                        ch22 = 14
                        check = 1
                        
                        
                    if ch2 == 9 and check == 0 and q == 43 : #ㅘ ㅐ
                        ch22 = 1
                        check = 1
                        
                        
                    if ch2 == 14 and check == 0 and q == 44 : #ㅝ ㅐ
                        ch22 = 1
                        check = 1
                        
                        
                    if ch2 == 14 and check == 0 and q == 45 : #ㅝ ㅔ
                        ch22 = 5
                        check = 1
                        
                        
                    if ch2 == 10 and check == 0 and q == 46 : #ㅙ ㅞ
                        ch22 = 15
                        check = 1
                    
                    if ch2 == 15 and check == 0 and q == 47 : #ㅞ ㅙ
                        ch22 = 10
                        check = 1
                    
                    if ch2 == 18 and check == 0 and q == 48 : #ㅡ ㅓ
                        ch22 = 15
                        check = 4
                    if ch2 == 18 and check == 0 and q == 49 : #ㅡ ㅏ
                        ch22 = 15
                        check = 0
                    if ch2 == 18 and check == 0 and q == 50 : #ㅡ ㅛ
                        ch22 = 15
                        check = 12
                    if ch2 == 18 and check == 0 and q == 51 : #ㅡ ㅠ
                        ch22 = 15
                        check = 17
                    
                    if ch2 == 20 and check == 0 and q == 52 : #ㅣ ㅑ
                        ch22 = 2
                        check = 1
                    if ch2 == 20 and check == 0 and q == 53 : #ㅣ ㅕ
                        ch22 = 6
                        check = 1
                    if ch2 == 20 and check == 0 and q == 54 : #ㅣ ㅗ
                        ch22 = 8
                        check = 1
                    if ch2 == 20 and check == 0 and q == 55 : #ㅣ ㅜ
                        ch22 = 13
                        check = 1
                    if ch2 == 20 and check == 0 and q == 56 : #ㅣ ㅠ
                        ch22 = 17
                        check = 1
                        
                    ch3 = (ord(err[w]) - ord('가')) - (588*ch1) - 28*ch2
                    #print(ch3, "ch3")
                    
                    
                    if check == 1 :
                        cnt += 1
                        if cnt == 7:
                            break
                        ch = chr(44032 + ch1*588 + ch22*28 + ch3)
                        check = 2
                        ch22 = 0
                        #word += ch
                        
                        word = []
                        for p in range (0, len(text[e])) :
                            word.append(text[e][p])
                        
                        word[w] = ch
                        
                        fix = ""
                        for p in range(0, len(text[e])) :
                            fix += word[p]
                    
                        if len(fix) == len(err) :
                            f = open('체언_상세.txt', 'rt', encoding='UTF8')
                            n_data = f.read()
                            if fix in n_data :
                                    print("%d번째 체언 오류 의심단어 수정 %s -> %s" %(e, err, fix))
                                    if e in lst :
                                        lst.remove(e)
                                    f.close()
                                    primary = primary.replace(err, fix, 1)
                                    #break  # 여기서 break 하면 하나만 추출 함
                            #print(fix) # 바꿔보며 출력
    return lst

def jong_filter(text, lst) :
    #n_err = nouns("구구마 가귀 고쇠 남배 선퓽기 여러가지 낙공 오글")
    global primary
    for e in range(0, len(text)): # 에러 단어 개수만큼 반복
        r_lst = []
        word = ""
        
        err = str(text[e]) # 다음 반복문을 위함
        fix = ""
        
        for w in range (0, len(err)): # 공백 제거 한글자씩 접근
            check = 0
            ch11 = 0
            cnt = 0
            for q in range(0, 30) :
                ## 영어인 경우 구분해서 작성함. 
                check = 0
                if '가'<=err[w]<='힣':
                    ## 588개 마다 초성이 바뀜. 
                    ch1 = (ord(err[w]) - ord('가'))//588

                    ch2 = ((ord(err[w]) - ord('가')) - (588*ch1)) // 28
                    #print(ch2, "ch2")
                  
                    ch3 = (ord(err[w]) - ord('가')) - (588*ch1) - 28*ch2
                    #print(ch3, "ch3")
                    
                    if ch3 == 1 and check == 0 and q == 0 : #ㄱ ㄹ
                        ch33 = 8
                        check = 1
                        
                    if ch3 == 4 and check == 0 and q == 1 : #ㄴ ㄷ
                        ch33 = 8
                        check = 7
                    if ch3 == 4 and check == 0 and q == 2 : #ㄴ ㅁ
                        ch33 = 8
                        check = 16
                    if ch3 == 4 and check == 0 and q == 3 : #ㄴ ㅂ
                        ch33 = 8
                        check = 17
                    if ch3 == 4 and check == 0 and q == 4 : #ㄴ ㅊ
                        ch33 = 8
                        check = 23
                        
                    if ch3 == 7 and check == 0 and q == 5 : #ㄷ ㄴ
                        ch33 = 4
                        check = 1
                        
                    if ch3 == 8 and check == 0 and q == 6 : #ㄹ ㄱ
                        ch33 = 1
                        check = 1
                    if ch3 == 8 and check == 0 and q == 7 : #ㄹ ㅅ
                        ch33 = 19
                        check = 1
                        
                    if ch3 == 16 and check == 0 and q == 8 : #ㅁ ㄴ
                        ch33 = 4
                        check = 1
                        
                    if ch3 == 17 and check == 0 and q == 9 : #ㅂ ㄴ
                        ch33 = 4
                        check = 1
                    if ch3 == 17 and check == 0 and q == 10 : #ㅂ ㅈ
                        ch33 = 22
                        check = 1
                    if ch3 == 17 and check == 0 and q == 11 : #ㅂ ㅊ
                        ch33 = 23
                        check = 1
                    
                    if ch3 == 19 and check == 0 and q == 12 : #ㅅ ㄹ
                        ch33 = 8
                        check = 1
                        
                    if ch3 == 22 and check == 0 and q == 13 : #ㅈ ㅂ
                        ch33 = 17
                        check = 1
                    if ch3 == 22 and check == 0 and q == 14 : #ㅈ ㅊ
                        ch33 = 23
                        check = 1
                        
                    if ch3 == 23 and check == 0 and q == 15 : #ㅊ ㄴ
                        ch33 = 4
                        check = 1
                    if ch3 == 23 and check == 0 and q == 16 : #ㅊ ㅁ
                        ch33 = 16
                        check = 1
                    if ch3 == 23 and check == 0 and q == 17 : #ㅊ ㅈ
                        ch33 = 22
                        check = 1
                        
                    if ch3 == 24 and check == 0 and q == 18 : #ㅋ ㅌ
                        ch33 = 25
                        check = 1
                    if ch3 == 24 and check == 0 and q == 19 : #ㅋ ㅍ
                        ch33 = 26
                        check = 1
                    if ch3 == 24 and check == 0 and q == 20 : #ㅋ ㅎ
                        ch33 = 27
                        check = 1
                        
                    if ch3 == 25 and check == 0 and q == 21 : #ㅌ ㅍ
                        ch33 = 26
                        check = 1
                    if ch3 == 25 and check == 0 and q == 22 : #ㅌ ㅋ
                        ch33 = 24
                        check = 1
                    if ch3 == 25 and check == 0 and q == 23 : #ㅌ ㅎ
                        ch33 = 27
                        check = 1
                        
                    if ch3 == 26 and check == 0 and q == 24 : #ㅍ ㅋ
                        ch33 = 24
                        check = 1
                    if ch3 == 26 and check == 0 and q == 25 : #ㅍ ㅌ
                        ch33 = 25
                        check = 1
                    if ch3 == 26 and check == 0 and q == 26 : #ㅍ ㅎ
                        ch33 = 27
                        check = 1
                        
                    if ch3 == 27 and check == 0 and q == 27 : #ㅎ ㅋ
                        ch33 = 24
                        check = 1
                    if ch3 == 27 and check == 0 and q == 28 : #ㅎ ㅌ
                        ch33 = 25
                        check = 1
                    if ch3 == 27 and check == 0 and q == 29 : #ㅎ ㅍ
                        ch33 = 26
                        check = 1
                    
                    
                    if check == 1 :
                        cnt += 1
                        if cnt == 4:
                            break
                        ch = chr(44032 + ch1*588 + ch2*28 + ch33)
                        check = 2
                        ch33 = 0
                        #word += ch
                        
                        word = []
                        for p in range (0, len(text[e])) :
                            word.append(text[e][p])
                        
                        word[w] = ch
                        
                        fix = ""
                        for p in range(0, len(text[e])) :
                            fix += word[p]
                    
                        if len(fix) == len(err) :
                            f = open('체언_상세.txt', 'rt', encoding='UTF8')
                            n_data = f.read()
                            if fix in n_data :
                                print("%d번째 체언 오류 의심단어 수정 %s -> %s" %(e, err, fix))
                                if e in lst :
                                    lst.remove(e)

                                f.close()
                                primary = primary.replace(err, fix, 1)
                                    #break  # 여기서 break 하면 하나만 추출 함
                                print(fix) # 바꿔보며 출력
    return lst

def case2(text) :
    global primary
    lst = []
    # 함수 내 print(lst) 실행하면 몇개의 체언 오류 발생 홗인
    lst = nouns_case(text)
    
    # 구문분석 시작 및 체언 오류 출력
    
    print("구문 분석 결과 다음과 같으며 체언 오류 의심은 %d개 입니다\n" %len(lst))
    text = nouns(text)
    
    print("\n체언 자체 오류 보정 결과입니다.\n")
    lst = cho(text, lst)
    lst = jung(text, lst)
    lst = jong(text, lst)
    #print(lst)
    
    print("\n 재검색 실행 \n")
    
    for e in lst :
        print("%d " %(e+1), end = '')
    print("번째 체언 오류의 조사 혹은 용언을 삭제 후 오류 보정을 시행합니다\n")
    
    if cho_upgrade(text, lst) != 1:
        jung_upgrade(text, lst)
        if jung_upgrade(text, lst) != 1:
            jong_upgrade(text, lst)



def case_up(text, lst_case, n_case) :
    global primary
    primary = text
    lst = n_case
    err_text = lst_case
    lst = cho_filter(err_text, lst)
    lst = jung_filter(err_text, lst)
    lst = jong_filter(err_text, lst)
    
    return lst

