username=input('Введите ваше имя: ')
title=input('Введите заголовок заметки: ')
content=input('Введите описание заметки: ')
status=input('Введите статус заметки: ')
created_date=input('Введите дату создания заметки в формате "день-месяц-год": ')
issue_date=input('Введите дату истечения заметки в формате "день-месяц-год": ')
title1=input('Введите заголовок 1 заметки: ')
title2=input('Введите заголовок 2 заметки: ')
title3=input('Введите заголовок 3 заметки: ')
titles=[title1, title2, title3]

note=[username, title, content, status, created_date [0:5], issue_date [0:5], [title1, title2, title3]]
print(note)
