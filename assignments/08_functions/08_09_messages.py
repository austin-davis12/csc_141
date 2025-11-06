def show_messages(messages):
    for message in messages:
        msg = f'{message.title()}'
        print(msg)

texts = ['What are you up to?','How has your day been?','What is new?']
show_messages(texts)