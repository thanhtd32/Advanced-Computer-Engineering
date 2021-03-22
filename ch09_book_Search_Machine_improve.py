#Author: Tran Duy Thanh
#Email: thanhtd@uel.edu.vn
#Date: 2021/03/21
#Description:
# These codes I improved from Professor's document and translate to English to do:
    # 1. 도서 입력 (Book input)
    # 2. 도서명으로 검색(Search by book name)
    # 3. 저자명으로 검색(Search by author name)
    # 4. 출판사명으로 검색 (Search by publisher name)
    # 5. 종료(End)
# with input a new book:
    #제목(title)>>
    #저자명(Author's name)>>
    #출판사(Publisher)>>
    #가격(price)>>
    #출판년도(Publication year)>>
mybooks=[
    {"제목":"안드로이드앱개발","저자":"최전산","출판사":"PCB","가격":"25000","출판년도":"2017"},
    {"제목":"파이선","저자":"강수라","출판사":"연두","가격":"23000","출판년도":"2019"},
    {"제목":"박정식","저자":"박정식","출판사":"SSS","가격":"38000","출판년도":"2018"},
    {"제목":"HTML5","저자":"주환","출판사":"대한","가격":"33000","출판년도":"2012"},
    {"제목":"컴파일러","저자":"장진웅","출판사":"PCB","가격":"24000","출판년도":"2011"},
    {"제목":"C언어","저자":"홍말숙","출판사":"한국","가격":"29000", "출판년도": "2010"},
    {"제목":"프로그래밍언어론","저자":"현정숙","출판사":"정의출판","가격":"41000", "출판년도": "2009"},
    {"제목":"안드로이드","저자":"이광희","출판사":"한극","가격":"42000", "출판년도": "2013"},
    {"제목":"앱인벤터","저자":"박규진","출판사":"대한","가격":"30000", "출판년도": "2015"},
]
while True:#Book input/search
    choice=input('''도서 입력/검색
    1. 도서 입력 (Book input)
    2. 도서명으로 검색(Search by book name)
    3. 저자명으로 검색(Search by author name)
    4. 출판사명으로 검색 (Search by publisher name)
    5. 종료(End)
    선택(1,2,3,4,5):''')
    if choice=='1':#book input
        while True:
            book=dict()
            title=input("제목(title)>>")
            author=input("저자명(Author's name)>>")
            publisher = input("출판사(Publisher)>>")
            price = input("가격(price)>>")
            year = input("출판년도(Publication year)>>")
            book["제목"]=title
            book["저자"] = author
            book["출판사"] = publisher
            book["가격"] = price
            book["출판년도"] = year
            mybooks.append(book)
            print("Enter a new book successfully!")
            continueEnterBook=input("Do you want to continue enter new book or not(Y/N)?>>")
            if continueEnterBook=='N' or continueEnterBook=='n':
                break
    elif choice=='2' : #도서명
        kwd="제목"
    elif choice=='3':#저자명
        kwd="저자"
    elif choice=='4':#출판사
        kwd="출판사"
    elif choice=='5':#end
        break;
    else:
        print("입력이 잘못되었습니다.")#Input is wrong
    if choice=='2' or choice=='3' or choice=='4':#finding the book with keyword:
        userin=input(kwd+">>>")
        find=False
        print("제목\t\t저자\t\t출판사\t\t가격\t\t출판년도")
        print("-"*40)
        for onebook in mybooks:
            if userin==onebook[kwd]:
                print(onebook["제목"],"\t",onebook["저자"],"\t",onebook["출판사"],"\t",
                      onebook["가격"],"\t",onebook["출판년도"])
                find=True
        print("-" * 40)
        if find==False:
            print("검색한 도서가 없습니다.")#There are no books found.
print("Thanks so much for your using the program!")
