import json
class Task:
    def __init__(self):
        self.task = {}
    def add (self):
        print("What do you want to add")
        add = input("")# 1 = not done  2 = progres 3 = done
        self.task.update({add : "not_done"})
    def remove (self):
        print("What do you want to remove")
        remove = input("")
        if remove not in self.task:
            print("That is not in youre list")
        else:
            self.task.pop(remove)
    def update (self):
        print("This is youre list: ")
        for i in self.task.keys():
            print(f"{i}\n")
    def list_done(self):
        print("deine gemachte liste")
        for i,d in self.task.items():
            if d == "done":
                print(f"{i}\n")
    def list_not_done(self):
        print("Das sind deine nicht gemacht sind: ")
        for i, d in self.task.items():
            if d == "not_done":
                print(f"{i}\n")
    def list_in_progres(self):
        print("Die sind in Progres")
        for i, d in self.task.items():
            if d == "progres":
                print(f"{i}\n")
    def mark(self):
        y = input(f"Was willst du markieren {self.task.keys()}")
        if y not in self.task.keys():
            print("is not in there")
        else:
            x = input("as what do you want to mark")
            if x == "progres":
                self.task[y] = "progres"
                print(f"{y} ist jetzt in Progress")
            elif x == "done":
                self.task[y] = "done"
                print(f"{y} ist jetzt done")
            else:
                print("Das kannst du nicht markieren")
    def anzeigen(self):
        print(self.task)
list = Task()
while True:
    print("Was willst du machen | add | remove | list_done | list_not_done | mark | update | stop")
    frage = input("")
    if frage == "add":
        list.add()
    elif frage == "remove":
        list.remove()
    elif frage == "list_done":
        list.list_done()
    elif frage == "list_not_done":
        list.list_not_done()
    elif frage == "list_in_progres":
        list.list_in_progres()
    elif frage == "mark":
        list.mark()
    elif frage == "update":
        list.update()
    elif frage == "stop":
        break
    elif frage == "speichern":
        with open ("Application.json", "w") as datei:
            json.dump(list.task, datei)