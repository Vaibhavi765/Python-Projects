import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import filedialog

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f'{self.name}, {self.phone}, {self.email}'

class ContactManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title('Contact Management System')

        self.contacts = []

        self.listbox = tk.Listbox(root, width=50, height=20)
        self.listbox.pack(padx=10, pady=10)

        self.add_button = tk.Button(root, text='Add Contact', command=self.add_contact)
        self.add_button.pack(pady=5)

        self.view_button = tk.Button(root, text='View Contact', command=self.view_contact)
        self.view_button.pack(pady=5)

        self.update_button = tk.Button(root, text='Update Contact', command=self.update_contact)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(root, text='Delete Contact', command=self.delete_contact)
        self.delete_button.pack(pady=5)

        self.save_button = tk.Button(root, text='Save Contacts', command=self.save_contacts)
        self.save_button.pack(pady=5)

        self.load_button = tk.Button(root, text='Load Contacts', command=self.load_contacts)
        self.load_button.pack(pady=5)

    def add_contact(self):
        name = simpledialog.askstring('Input', 'Enter name:')
        phone = simpledialog.askstring('Input', 'Enter phone number:')
        email = simpledialog.askstring('Input', 'Enter email address:')
        if name and phone and email:
            contact = Contact(name, phone, email)
            self.contacts.append(contact)
            self.listbox.insert(tk.END, name)
            messagebox.showinfo('Success', 'Contact added successfully.')
        else:
            messagebox.showwarning('Input Error', 'All fields are required.')

    def view_contact(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            contact = self.contacts[index]
            messagebox.showinfo('Contact Details', str(contact))
        else:
            messagebox.showwarning('Selection Error', 'Please select a contact.')

    def update_contact(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            name = simpledialog.askstring('Input', 'Enter new name:', initialvalue=self.contacts[index].name)
            phone = simpledialog.askstring('Input', 'Enter new phone number:', initialvalue=self.contacts[index].phone)
            email = simpledialog.askstring('Input', 'Enter new email address:', initialvalue=self.contacts[index].email)
            if name and phone and email:
                self.contacts[index].name = name
                self.contacts[index].phone = phone
                self.contacts[index].email = email
                self.listbox.delete(index)
                self.listbox.insert(index, name)
                messagebox.showinfo('Success', 'Contact updated successfully.')
            else:
                messagebox.showwarning('Input Error', 'All fields are required.')
        else:
            messagebox.showwarning('Selection Error', 'Please select a contact.')

    def delete_contact(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            contact_name = self.contacts[index].name
            self.contacts.pop(index)
            self.listbox.delete(index)
            messagebox.showinfo('Success', f'Contact {contact_name} deleted successfully.')
        else:
            messagebox.showwarning('Selection Error', 'Please select a contact.')

    def save_contacts(self):
        filename = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text files', '*.txt')])
        if filename:
            with open(filename, 'w') as file:
                for contact in self.contacts:
                    file.write(str(contact) + '\n')
            messagebox.showinfo('Success', f'Contacts saved to {filename}.')

    def load_contacts(self):
        filename = filedialog.askopenfilename(filetypes=[('Text files', '*.txt')])
        if filename:
            try:
                with open(filename, 'r') as file:
                    self.contacts = []
                    self.listbox.delete(0, tk.END)
                    for line in file:
                        name, phone, email = line.strip().split(', ')
                        contact = Contact(name, phone, email)
                        self.contacts.append(contact)
                        self.listbox.insert(tk.END, name)
                messagebox.showinfo('Success', f'Contacts loaded from {filename}.')
            except FileNotFoundError:
                messagebox.showwarning('File Error', f'File {filename} not found.')

if __name__ == '__main__':
    root = tk.Tk()
    cms = ContactManagementSystem(root)
    root.mainloop()
    