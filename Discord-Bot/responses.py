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
        return f"{update_scraper.get_latest_release(m_name)}"
    
    if (m_.startswith("score")):
        m_name = m_[len("score "):]
        return f"{m_name}'s Bayesian Average: {update_scraper.get_bayesian_score(m_name)}/10"
        
    return "Unknown message!"