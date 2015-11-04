import db
import debug

t = input("""Для начала здраствуйте!
Вы планируете воспользоваться программой? если да введите yes - """)
if t == 'yes':
    db.creat_list()
    db.zapis()
    debug.loadd(db.mem())
else:
    pass
