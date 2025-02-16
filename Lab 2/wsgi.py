import click, sys
from models import db, User,Todo
from app import app
from sqlalchemy.exc import IntegrityError

#Creation of an object

@app.cli.command("init", help="Creates and initializes the database")
def initialize():
  db.drop_all()
  db.init_app(app)
  db.create_all()

  #Creating a user object bo by calling the class model constructor
  bob = User('bob', 'bob@mail.com', 'bobpass')
  #adding a todo to bob
  bob.todos.append(Todo('wash car'))
  #Save the user to the database using  the db.session.add() and db.session.commit()
  db.session.add(bob)
  db.session.commit()
  print(bob)
  print('database intialized')

  
#retrieve a user by their username
@app.cli.command("get-user", help="Retrieves a User")
@click.argument('username', default='bob')
def get_user(username):
  #.first() returns the first object as default
    bob = User.query.filter_by(username=username).first()
    if not bob:
       print(f'{username} not found! ')
       return
    print(bob)


@app.cli.command('get-users')
def get_users():
   #This gets all the objects of a model
   users = User.query.all()
   print(users)

#Adding a command to update the email of a user
@app.cli.command("change-email")
@click.argument('username', default = 'bob')
@click.argument('email', default = 'bob@mail.com')
def change_email(username,email):
   bob = User.query.filter_by(username=username).first()
   if not bob:
      print(f'{username} not found!')
      return
   bob.email = email
   db.session.add(bob)
   db.session.commit()
   print(bob)

   #creating a user with error handling
@app.cli.command('create-user')
@click.argument('username', default='rick')
@click.argument('email', default='rick@mail.com')
@click.argument('password', default='rickpassword')
def create_user(username, email, password):
    newuser = User(username,email,password)
    try:
      db.session.add(newuser)
      db.session.commit()
    except IntegrityError as e:
      #let's the database undo any previous steps of a transaction
      db.session.rollbacl()

      print("Username or email already taken!")
    else:
      print(newuser)


#Deleting an object
@app.cli.command('delete-user')
@click.argument('username', default='bob')
def delete_user(username):
   bob = User.query.filter_by(username=username).first()
   if not bob:
      print(f'{username} not found')
      return
   db.session.delete(bob)
   db.session.commit()
   print(f'{username} deleted')


#Todos commmands
@app.cli.command('get-todos')
@click.argument('username', default='bob')
def get_user_todos(username):
   bob = User.query.filter_by(username=username).first()
   if not bob:
      print(f'{username} not found!')
      return
   print(bob.todos)


@app.cli.command('add-todo')
@click.argument('username', default='bob')
@click.argument('text', default='wash car')
def add_tastk(username, text):
   bob = User.query.filter_by(username=username).first()
   if not bob:
      print(f'{username} not found!')
      return
   new_todo = Todo(text)
   bob.todos.append(new_todo)
   db.session.add(bob)
   db.session.commit()

@click.argument('todo_id', default=1)
@click.argument('username', default='bob')
@app.cli.command('toggle-todo')
def toggle_todo_command(todo_id, username):
  user = User.query.filter_by(username=username).first()
  if not user:
    print(f'{username} not found!')
    return

  todo = Todo.query.filter_by(id=todo_id, user_id=user.id).first()
  if not todo:
    print(f'{username} has no todo id {todo_id}')

  todo.toggle()
  print(f'{todo.text} is {"done" if todo.done else "not done"}!')

@app.cli.command('add-category', help="Adds a category to a todo")
@click.argument('category', default='chores')
@click.argument('todo_id', default=6)
@click.argument('username', default='bob')
def add_todo_category_command(category, todo_id, username,):
  user = User.query.filter_by(username=username).first()
  if not user:
    print(f'user {username} not found!')
    return

  res = user.add_todo_category(todo_id, category)
  if not res:
    print(f'{username} has no todo id {todo_id}')
    return

  todo = Todo.query.get(todo_id)
  print(todo)

  
  #according to the __repr__ method we can print the new user
  