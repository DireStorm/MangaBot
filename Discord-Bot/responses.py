def handle_response(message) -> str:
    m_ = message.lower()
    
    if (m_ == "hello"):
        return "Hello"
    
    return "Unknown message!"