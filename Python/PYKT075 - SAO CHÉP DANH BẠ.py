with open('SOTAY.txt', 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f if line.strip()]

def sapxep(contact):
    name, phone, date = contact
    part = name.split()
    last_name = part[-1]
    first_name = ' '.join(part[:-1])
    return [last_name, first_name]


contacts = []
i = 0
current_date = ''
while i < len(lines):
    if 'Ngay' in lines[i]:
        current_date = lines[i][5:]
        i += 1
    else:
        name = lines[i]
        phone = lines[i + 1]
        contacts.append([name, phone, current_date])
        i += 2

contacts.sort(key=sapxep)

for i in range(len(contacts)):
    print(f"{contacts[i][0]}: {contacts[i][1]} {contacts[i][2]}")
