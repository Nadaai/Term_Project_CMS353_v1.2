
user = User(id=1, name='hassan',email='hassan@gmail.com')
db.session.add(user)
db.session.commit()