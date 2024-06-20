KB = {'games': {'PUBG': 'It is a real time good game', 'Subway Surfers': 'It is a player friendly game based on surfing'},
            'news': {'Morning': '1.PM attended the Inguration in Karnataka', 'Evening': 18}}

user_views = {'PUBG': 0,'Evening':0,'Morning':0, 'Subway Surfers':0}
class KBS:
    def search_article(self):
        search_key = input("Enter the word you would like to search: ")
        global found,x
        found=False
        x=search_key
        for key, value in KB.items():
            sub=str(key)
            if sub.lower() == search_key.lower():
                found=True
                for sub_key, sub_value in value.items():
                    print(f"{key}:{sub_key}\n{sub_value}")
                    user_views[sub_key]+=1
                break
            elif search_key not in key:
                for sub_key, sub_value in value.items():
                    sub=str(sub_key)
                    if sub.lower() == search_key.lower():
                                print(f"{key}:{sub_key}\n{sub_value}")
                                user_views[sub_key]+=1
                                found=True
                                break
            if not found and search_key not in value:
                for sub_key, sub_value in value.items():
                        sub=str(sub_value)
                        for word in sub.split():
                            if word.lower() == search_key.lower():
                                print(f"{key}:{sub_key}\n{sub_value}")
                                user_views[sub_key]+=1
                                found=True
                                break

    def update(self):
        new = input("Enter the article you would like to update:")
        key_copy = list(KB.keys())
        found = False
        for key in key_copy:
            keysub_copy = list(KB[key].keys())
            for sub_key in keysub_copy:
                sub = str(sub_key)
                if sub.lower() == new.lower():
                    found = True
                    x = new
                    d = KB[key].pop(sub_key)
                    rwt=int(input("Do you want to add to the content existing content (yes-1/no-0): "))
                    if rwt==1:
                        mean = input("\nEnter the new content :")
                        KB[key].update({x: d+' '+mean})
                        print(KB[key].get(x))
                        break
                    else:
                        mean = input("\nEnter the new content :")
                        KB[key].update({x:mean})
                        print(KB[key].get(x))
                        break
            if found:
                break
        if not found:
            print(f"{new} article is not available")


    def create(self):
        print("In which genere do u want to create an article")
        ch=int(input("1.Games 2.News 3.New Genere"))
        key_copy=list(KB.keys())
        for key in key_copy:
            if ch==1:
                if key=='games':
                    word=input("\nEnter the title of article: ")
                    print(word,end=' ')
                    keysub_copy=list(KB[key].keys())
                    for sub_key in keysub_copy:
                            sub=str(sub_key)
                            if sub.lower() != word.lower():
                                mean=input("\nEnter the content :")
                                KB[key].update({word:mean})
                                print(KB[key].get(word))
                                user_views[word]=0
                                break
                            else:
                                print(f"\nArticle with key '{word}' already exists. Use the update method instead.")
                                break
                    break

            elif ch==2:
                if key=='news':
                    word=input("Enter the title of article: ")
                    print(word,end=' ')
                    keysub_copy=list(KB[key].keys())
                    for sub_key in keysub_copy:
                            sub=str(sub_key)
                            if sub.lower() != word.lower():
                                mean=input("\nEnter the content :")
                                KB[key].update({word:mean})
                                print(KB[key].get(word))
                                user_views[word]=0
                                break
                            else:
                                print(f"\nArticle with key '{word}' already exists. Use the update method instead.")
                                break
                    break 

            elif ch==3:
                    article=input("Enter the genre you would like to add: ")
                    word=input("Enter the title of article: ")
                    if article in KB:
                        print(f"\nArticle with key '{article}' already exists. Use the update method instead.")
                        break     
                    else:
                        for sub_key in KB[key].keys():
                            sub=str(sub_key)
                            if word in KB or word in sub_key:
                                print(f"\nArticle with key '{article}' already exists. Use the update method instead.")
                                break       
                            else:
                                mean=input("\nEnter the content :")
                                #KB.update({word:mean})
                                KB[article]={word:mean}
                                user_views[word]=0
                                print(f'{article}:{word}\n{KB[article].get(word)}')
                                break    
                    break
            
    def delete(self):
        new=input("Enter the article you would like to delete:")
        key_copy=list(KB.keys())
        for key in key_copy:
                keysub_copy=list(KB[key].keys())
                for sub_key in keysub_copy:
                    sub=str(sub_key)
                    if sub.lower() == new.lower():
                        x=new
                        d=KB[key].pop(sub_key) 
                        print(f"This {sub_key} article is deleted")     

    def generate_popular_content_report(self):
        sorted_articles = sorted(user_views.items(), key=lambda x: x[1], reverse=True)
        print('articles - views')

        for i,j in sorted_articles: 
            h='-'
            print(f"{i}\t%s%2d"%(h,j))


    def view_article(self):
        search_key = input("Enter the article you would like to view: ")
        for key, value in KB.items():
            for sub_key, sub_value in value.items():
                if sub_key.lower() == search_key.lower():
                    print(f"{key}:{sub_key}\n{sub_value}")
                    user_views[sub_key]+=1
                    break          
            
ar=KBS()
while True:
    print("1.Create 2.Search 3.Update 4.Delete 5.Generate popular content 6.View Article 7.Exit")
    ch=int(input('Enter your choice: '))
    if ch==1:
        ar.create()
    elif ch==2: 
        ar.search_article()
        if not found:
            print("\nThis article is not yet available")
    elif ch==3:
        ar.update()
    elif ch==4:
        ar.delete()
    elif ch==5:
         ar.generate_popular_content_report()
    elif ch==6:
         ar.view_article()  
    elif ch==7:
        break
