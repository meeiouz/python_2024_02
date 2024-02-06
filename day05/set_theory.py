# set: 중복 허용 안됨, 집합 개념
a = {1, 2, 3, 1, 2, 3, 1, 2, 3}
a.add(4) # 추가
a.discard(3) # 삭제
print(a)

# set() - 세트화
b = set([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
print(b)

news = """Memories follow me left and right
I can feel you over here I can feel you over here
you take up every corner of my mind
whatcha gon do now
ever since the da day y-you went away
no I don't know how
how to erase your body from out my brain
whatcha gon do now
maybe I should just focus on me instead
But all I think about
are the nights we were tangled up in your bed
oh no (oh no)
oh no (oh no)
you're going round in circles got you stuck up in my head (yeah)
Memories follow me left and right
I can feel you over here I can feel you over here
you take up every corner of my mind
your love stays with me day and night
I can feel you over here I can feel you over here
you take up every corner of my mind
whatcha gon do now
ever since the da da day y-you went away
someone tell me how
how much more do I gotta drink for the pain
whatcha gon do now
you did things to me that I just can't forget
now all I think about
are the nights we were tangled up in your bed
oh no (oh no)
oh no (oh no)
you're going round in circles got ya stuck up in my head
Memories follow me left and right
I can feel you over here I can feel you over here
you take up every corner of my mind
your love stays with me day and night
I can feel you over here I can feel you over here
you take up every corner of my mind
whatcha gon do now
did ya know you're the one that got away
and even now baby i'm still not ok
did ya know that my dreams they're are the same
everytime I close my eyes
Memories follow me left and right
I can feel you over here I can feel you over here
you take up every corner of my mind
whatcha gon do now
your love stays with me day and night
I can feel you over here i can feel you over here
you take up every corner of my mind
whatcha gon do now
I can feel you over here I can feel you over here
you take up every corner of my mind
whatcha gon do now"""
wordlist = news.split()
no_dupli_words = list(set(wordlist))
no_dupli_words.sort()
print(no_dupli_words)

starbucks = {"아메리카노", "라뗴", "프라푸치노", "샌드위치", "베이글"}
subway = {"샐러드", "샌드위치", "아메리카노", "랩", "쿠키"}
all_menu = starbucks.union(subway) # 합집합
print(all_menu)
inter_menu = starbucks.intersection(subway) # 교집합
print(inter_menu)
pure_starbucks_menu = starbucks.difference(subway) # 차집합
pure_subway_menu = subway.difference(starbucks) # 차집합
no_inter_menu = starbucks.symmetric_difference(subway)
print(no_inter_menu)