import json
import datetime as dt
import update_scraper

def handle_response(message, author) -> str:
    m_ = message.lower()
    
    if (m_ == "hello"):
        return f"Hello {author.name}"
    
    # Handling Manga Messages 
    if (m_.startswith("updates")):
        m_name = m_[len("updates "):]
        return update_scraper.get_latest_release(m_name)
    
    # Handling Todo Messages
    #todo_handler(m_)
        
    return "Unknown message!"

#def todo_handler(message):
    #YYYY-MM-DD
    curr_date = str(dt.date.today())
    #^ might want to specifically define this in the if statements instead
    
    #Current Todo
    if (message == "todo list"):
        print("working")
        with open("data.json") as f:
            data = json.load(f)
            return data
            for date in data:
                if date["date"] == curr_date:
                    return ", ".join(date["entries"])
    
    #Adding to Todo
    if "todo add" in message:
        add = message[9:]

        #Reading data
        with open("\.data.json") as f:
            data = json.load(f)
            
        #Modifying data
        for date in data:
            if(date["date"] == curr_date):
                date["entries"].append(add)
                break
        else:
            add_dict = {}
            add_dict["date"] = curr_date 
            add_dict["entries"] = []
            add_dict["entries"].append(add)
            data.append(add_dict)
            
        #Overwrite Data
        with open("data.json", "w") as f:
            json.dump(data, f)
        
        #Returning new todo list
        with open("data.json") as f:
            data = json.load(f)
            for date in data:
                if date["date"] == curr_date:
                    return ", ".join(date["entries"])

# def m_get_update(message):
#     # Get info updates about Manga/Manhwa: !updates manga_name
#     m_name = message[len("updates "):]
#     return update_scraper.get_latest_release(m_name)
