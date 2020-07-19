in_id = input("아이디를 입력해주세요.\n")
in_pw = input("패스워드를 입력해주시요.\n")

members_id = ['egoing', 'leezche', 'graphittie']
members_pw = ['1111', '2222', '3333']

for i, p in zip(members_id, members_pw):
    if i==in_id and p==in_pw:
        print("Hello, World!")
    
print("Who are you?")