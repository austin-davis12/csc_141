send_messages = ['What are you up to?','How has your day been?','What is new?']
sent_messages = []

while send_messages:
    unsent_texts = send_messages.pop()
    print(f'Texts:{unsent_texts}')
    sent_messages.append(unsent_texts)

for sent_message in sent_messages:
    print(sent_message)