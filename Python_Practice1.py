def main():

    booklist = []

    choice = 0
    while choice != 4:
        print("******* Book Manager *******")
        print("1 , Add A New Book, ")
        print("2 , Look For A Book,")
        print("3 , Display All Book,")
        print("4 , Quit ()")
        choice = int(input("Enter The Choice"))

        if choice == 1 :
            print("Adding A Book .... ")
            nBook = input("Enter The Name Of The Book ; ")
            nAuthor = input ("Enter The Name Of The Author ; ")
            nPublishier = input("Enter The Name Of The Publishier ; ")
            booklist.append([nBook,nAuthor,nPublishier])
            print("Add Successfully")
        
        elif choice == 2 :
            print("What Book You Want To LookUp !! ")
            LookUp = input("Enter The Name Of The Book : ")
            for book in booklist :
                if  LookUp in book:
                    print(book)
                else:
                    print(f"There Is No Book Name {LookUp} ")
        elif choice == 3 :
            print ("Displaying All Books ...")
            for i in range (len(booklist)):
                print(booklist[i])

        else :
            print("QUITTING ..")

    print("Program Terminated !!!! ")
        
if __name__ == "__main__":
    main()