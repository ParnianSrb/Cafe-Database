row = ['Milkshake', 'Chocolate', 'Whipped Cream', 12000]
string = ''
for item in row:
    string = string + str(item) + '\t'

print(string)

for row in rows:
    string = f'{row[0]}: '
    for i in range(1, len(row)):
        string = string + str(row[i])

    self.listWidget_view.addItem(string)

for row in rows:
    string = ''
    for item in row:
        string = string + str(item) + ',  '
    print(f'{string}')
    self.listWidget_view.addItem(string)