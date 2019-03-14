import sys
from notebook import Notebook,Note

class Menu:

    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1":self.show_notes,
            "2":self.search_notes,
            "3":self.add_note,
            "4":self.modify_note,
            "5":self.quit
        }

    def display_menu(self):
        print("""
        NoteBook Menu
        
        1.Show all Notes
        2.Search Note
        3.Add Note
        4.Modify Note
        5.Quit
        """)

    def run(self):

        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{} is not a valid choice".format(choice))

    def show_notes(self,notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{} : {} {}".format(note.id,note.tags,note.memo))

    def search_notes(self):
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        memo = input("Enter the Memo: ")
        self.notebook.new_note(memo)
        print("Your note has been added")

    def modify_note(self):
        id = input("Enter the note ID : ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(id,memo)
        if tags:
            self.notebook.modify_tag(id,tags)

    def quit(self):
        print("Thank you for using your notebook today")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()
