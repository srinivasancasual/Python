import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["assigments"]
mycol = mydb["firstcollection"]
#x = mycol.find_one()
#print(x)

while True:
    try:
        print("1.Enter Book Details","2.View Books","3.Search Books","4.Remove Books","5.Exit")
        user_input=int(input("Enter Option"))
        if user_input==5:
            break
        elif user_input==1:
            book_id=int(input("Enter Book Id"))
            book_title=input("Enter Book Title")
            book_pages=int(input("Enter Book Pages"))
            book_price=float(input("Enter Book Price"))
            mydict = dict()
            mydict["book_id"]=book_id
            mydict["book_title"]=book_title
            mydict["book_pages"]=book_pages
            mydict["book_price"]=book_price
            mycol.insert_one(mydict)
            print("------Books Added Successfully------")
        elif user_input==2:
            mydoc = mycol.find()
            print("--------All Books Details----------")
            for x in mydoc:
                print(x)
            
        elif user_input==3:
            book_id=int(input("Enter the Book ID"))
            myquery=dict()
            myquery["book_id"]=book_id
            mydoc = mycol.find(myquery)
            print("-------Search Results---------")
            for x in mydoc:
                print(x["book_title"])
                print(x["book_title"])
                print(x["book_title"])
                print(x["book_title"])
        elif user_input==4:
            book_id=int(input("Enter the Book ID"))
            myquery=dict()
            myquery["book_id"]=book_id
            try:
                mycol.delete_one(myquery)
                print("------Books Removed------")
            except:
                print("-------No Books Found-------")
            
    except:
        print("Error Occured Try Again")