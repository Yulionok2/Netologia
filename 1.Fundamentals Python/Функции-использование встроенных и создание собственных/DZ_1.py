# Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:

# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя 
# владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию, когда пользователь 
# будет пытаться добавить документ на несуществующую полку.

# d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок. 
# Предусмотрите сценарий, когда пользователь вводит несуществующий документ;
# m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую. 
# Корректно обработайте кейсы, когда пользователь пытается переместить несуществующий документ или переместить 
# документ на несуществующую полку;
# as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень. Предусмотрите случай, 
# когда пользователь добавляет полку, которая уже существует.;

documents = [
  {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
  {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
  {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
  '1': ['2207 876234', '11-2'],
  '2': ['10006'],
  '3': []
}

def people_doc_number(list_documents):
  """Команда, которая спрашивает номер документа и выводит имя человека, которому он принадлежит"""
  x = ''
  number = input('Введите номер документа: ')
  for document in documents:
    if document["number"] == number:
      name = document["name"]
      print(f'Этот документ принадлежит: {name}')
      break
  else:
    print('Такого документа не существует')
  return x

def shelf_doc_number(list_directories):
  """Команда, которая спрашивает номер документа и выводит номер полки, на которой он находится"""
  x = ''
  number = input('Введите номер документа: ')
  shelf_true = None
  for shelf_document in directories.items():
    for document_1 in shelf_document[1]:
      if document_1 == number:
        print(f'Документ номер - {number}, находится на полке -  {shelf_document[0]}')
        shelf_true = True
    if shelf_true == True:
      break
  else:
    print(f'Такого документа не существует!')
  return x

def list_documents(list_documents):
  """Команда, которая выводит список всех документов"""
  x = ''
  for doc in documents:
    print(f'{doc["type"]} "{doc["number"]}" "{doc["name"]}"')
  return x

def add_new_doc(list_documents, list_directories):
  """Команда, которая добавляет новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться"""
  x = ''
  number_doc = input('Введите номер нового документа:')
  type_doc = input('Введите тип нового документа:')
  name_doc = input('Введите имя владельца:')
  shelf_number = input(str('Введте номер полки на которой будет хранится документ:'))
  dict_new = {"type": type_doc, "number": number_doc, "name": name_doc}
  if shelf_number in directories.keys():
    directories[shelf_number].append(number_doc)
    documents.append(dict_new)
    print('Документ добавлен')
  else:
    print('Так как такой полки не существует, документ не добавлен')
  return x    

def delete_doc(list_documents, list_directories):
  """Команда, которая спрашивает номер документа и удаляет его из каталога и из перечня полок"""
  x = ''
  document = input('Введите номер документа, который хотите удалить: ')
  doc_none = None
  for doc in documents:
    if doc["number"] == document:
      del(doc["number"])
      for value in directories.values():
        if document in value:
          value.remove(document)
          print('Документ удален из католога и перечня полок')
          doc_none = True
      if doc_none == True:
        break
  else:
    print('Такого документа не существует!')
  return x

def move_doc(list_directories):
  """Команда, которая спрашивает номер документа и целевую полку и перемещает его с текущей полки на целевую"""
  x = ''
  number_doc = input('Введите номер документа который хотите переместить: ')
  shelf_doc = input(str('Введите номер полки на которую хотите переместить документ:'))
  for value in directories.values():
    if shelf_doc in directories:
      if number_doc in value:
        value.remove(number_doc)
        directories[shelf_doc].append(number_doc)
        print(f'Документ номер: "{number_doc}", перемещен на полку номер {shelf_doc}')
        break
  else:
      print('Такого документа или такой полки не существует, проверьте правильность введенных данных')
  return x

def add_shelf(list_directories):
  """Команда, которая спрашивает номер новой полки и добавляет ее в перечень"""
  x = ''
  new_shelf = input('Введите номер полки которую хотите создать:')
  for key in directories.keys():
    if new_shelf == key:
      print('Такая полка уже существует')
      break
  else:
    directories[new_shelf] = list()
    print(f'Полка номер {new_shelf} добавлена')
  return x


def all_commands():
  while True:
    list_commands = '''p - команда, которая спрашивает номер документа и выводит имя человека, которому он принадлежит;
s - команда, которая спрашивает номер документа и выводит номер полки, на которой он находится;
l - команда, которая выводит список всех документов;
a - команда, которая добавляет новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться;
d - команда, которая спрашивает номер документа и удаляет его из каталога и из перечня полок;
m - команда, которая спрашивает номер документа и целевую полку и перемещает его с текущей полки на целевую;
as - команда, которая спрашивает номер новой полки и добавляет ее в перечень;
exit - выход из программы'''
    command = input('Введите команду которую хотите выполнить:')
    if command == 'p':
      print(people_doc_number(documents))
    elif command == 's':
      print(shelf_doc_number(directories))
    elif command == 'l':
      print(list_documents(documents))
    elif command == 'a':
      print(add_new_doc(documents, directories))
    elif command == 'd':
      print(delete_doc(documents, directories))
    elif command == 'm':
      print(move_doc(directories))
    elif command == 'as':
      print(add_shelf(directories))
    elif command == 'help':
      print(list_commands)
    elif command == 'exit':
      print('До свидания!')
      break
