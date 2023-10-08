import json
import datetime as dt

def handle_response(message, author) -> str:
    m_ = message.lower()
    
    #YYYY-MM-DD
    curr_date = str(dt.date.today())
    #^ might want to specifically define this in the if statements instead
    
    if (m_ == "hello"):
        return f"Hello {author}"
    
    #Current Todo
    if (m_ == "todo list"):
        print("working")
        with open("C:\\Users\\User\\Documents\\GitHub\\DiscordBot\\Discord-Bot\\data.json") as f:
            data = json.load(f)
            return data
            for date in data:
                if date["date"] == curr_date:
                    return ", ".join(date["entries"])
    
    #Adding to Todo
    if "todo add" in m_:
        add = m_[9:]

        #Reading data
        with open("data.json") as f:
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
        
    return "Unknown message!"