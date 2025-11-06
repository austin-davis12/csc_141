def messages(send_messages,sent_messages):

    while send_messages:
        unsent_texts = send_messages.pop()
        print(f'Texts:{unsent_texts}')
        sent_messages.append(unsent_texts)

def show_text_messages(sent_message):
    print('\nSent Messages:')
    for sent_message in sent_messages:
        print(sent_message)

send_messages = ['What are you up to?','How has your day been?','What is new?']
sent_messages = []

messages(send_messages[:],sent_messages)
show_text_messages(sent_messages)

print(send_messages)
print(sent_messages)