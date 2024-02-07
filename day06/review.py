megaMovie = {
   'movie': [
        {'name': '엑션', 'price': 10000},
        {'name': '로코', 'price': 8000},
        {'name': '공포', 'price': 9000},
    ]
}
print(f"{megaMovie['movie']}")
movieNumber = int(input("영화를 고르시오(0~2번):"))
print(f"구매하신 영화는 {megaMovie['movie'][movieNumber]['name']}이고 가격은 {megaMovie['movie'][movieNumber]['price']}원 입니다")



#my_dict = {'name': 'Alice', 'age':25}

#print(my_dict['name']) # 'Alice' 연산자
#print(my_dict.get('name') # 'Alice' 기능
#print(my_dict.get('gender', 'Not Specified')) # 'Not Specified' (기본 사용값)

#my_dict = {'name': 'Bob', 'age': 30, 'job': 'Developer'}
# keys
#print(list(my_dict.keys())) # ['name', 'age', 'job']
#values
#print(list(my_dict.values())) # ['Bob', '30', 'Developer']
#items
#print(list(my_dict.items())) #[('name', 'Bob')]