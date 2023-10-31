import sqlite3
from kivy.app import App
from kivy.lang import Builder

class MyApp(App):
    def build(self):
        self.init_database()
        return Builder.load_file('main.kv')

    def init_database(self):
        conn = sqlite3.connect('user_data.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                organization TEXT,
                email TEXT,
                password TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def on_login_button_click(self):
        first_name = self.root.ids.first_name_input.text
        last_name = self.root.ids.last_name_input.text
        organization = self.root.ids.organization_input.text
        email = self.root.ids.email_input.text
        password = self.root.ids.password_input.text

        # Insert data into the database
        conn = sqlite3.connect('user_data.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (first_name, last_name, organization, email, password) VALUES (?, ?, ?, ?, ?)',
                       (first_name, last_name, organization, email, password))
        conn.commit()
        conn.close()

        print("Data saved in the database.")

    def print_database(self):
        conn = sqlite3.connect('user_data.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        data = cursor.fetchall()
        conn.close()

        print("User Data in the Database:")
        for row in data:
            print(f"ID: {row[0]}, First Name: {row[1]}, Last Name: {row[2]}, Organization: {row[3]}, Email: {row[4]}, Password: {row[5]}")

if __name__ == '__main__':
    MyApp().run()
