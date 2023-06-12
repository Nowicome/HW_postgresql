import psycopg2


class Postgres:
    def __init__(self):
        self.conn = psycopg2.connect(database="postgres_1", user="postgres_1", password="123456789")
        self.cur = self.conn.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def create_tables(self):
        """Создаёт таблицы базы данных (clients, phones)"""
        self.cur.execute("""
                CREATE TABLE IF NOT EXISTS clients(
                    id SERIAL PRIMARY KEY,
                    first_name varchar(60) NOT NULL,
                    second_name varchar(60) NOT NULL,
                    email varchar(60) NOT NULL UNIQUE
                    );
                CREATE TABLE IF NOT EXISTS phones(
                    id SERIAL PRIMARY KEY,
                    client_id INT NOT NULL REFERENCES clients(id),
                    number INT NOT NULL
                    );
                """)
        self.conn.commit()
        return print("complete")

    def delete_all(self):
        """Удаляет таблицы базы данных, созданные методом класса 'create_tables'"""
        self.cur.execute("""
            DROP TABLE PHONES;
            DROP TABLE CLIENTS;
        """)
        self.conn.commit()
        return print("complete")

    def add_client(self, f_name: str, s_name: str, e_mail: str):
        """Добавляет в базу данных нового клиента"""
        self.cur.execute("""
            INSERT INTO clients (first_name, second_name, email)
            VALUES (%s, %s, %s) RETURNING id;
        """, (f_name, s_name, e_mail))
        new_id = self.cur.fetchone()[0]
        self.conn.commit()
        return print("complete, id of new client is ", new_id)

    def add_phone(self, client_id, number):
        """Добавляет существующему клиенту новый номер телефона"""
        self.cur.execute("""
            INSERT INTO phones (client_id, number)
            VALUES (%s, %s) RETURNING id;
        """, (client_id, number))
        new_id = self.cur.fetchone()[0]
        self.conn.commit()
        return print("complete, id of new phone is", new_id)

    def delete_phone(self, phone_id):
        """Удаляет телефонт клиента (по id телефона)"""
        self.cur.execute("""
            DELETE FROM phones
            WHERE id = %s;
        """, (phone_id, ))
        self.conn.commit()
        return print("Complete")

    def delete_all_phones(self, client_id):
        """Удаляет все телефоны клиента (по id клиента)"""
        self.cur.execute("""
            DELETE FROM phones
            WHERE client_id = %s;
        """, (client_id, ))
        self.conn.commit()
        return print("Complete")

    def delete_client(self, client_id):
        """Удаляет клиента (по id)"""
        self.cur.execute("""
            DELETE FROM clients
            WHERE id = %s;
        """, (client_id, ))
        self.conn.commit()
        return print("Complete")

    def edit_f_name(self, client_id, new_name):
        """Изменяет имя клиента"""
        self.cur.execute("""
            UPDATE clients
            SET first_name = %s
            WHERE id = %s;
        """, (new_name, client_id))
        self.conn.commit()
        return print("Complete")

    def edit_s_name(self, client_id, new_s_name):
        """Изменяет фамилию клиента"""
        self.cur.execute("""
            UPDATE clients
            SET second_name = %s
            WHERE id = %s;
        """, (new_s_name, client_id))
        self.conn.commit()
        return print("Complete")

    def edit_email(self, client_id, new_email):
        """"Изменяет email клиента"""
        self.cur.execute("""
            UPDATE clients
            SET email = %s
            WHERE id = %s;
        """, (new_email, client_id))
        self.conn.commit()
        return print("Complete")

    def edit_phone(self, phone_id, new_phone):
        """Изменяет телефон клиента"""
        self.cur.execute("""
            UPDATE phones
            SET number = %s
            WHERE id = %s;
        """, (new_phone, phone_id))
        self.conn.commit()
        return print("Complete")

    def find_with_name(self, name):
        """Находит id клиента по имени"""
        self.cur.execute("""
            SELECT id
            FROM clients
            WHERE first_name = %s;
        """, (name, ))
        ap = self.cur.fetchall()
        return ap

    def find_with_s_name(self, s_name):
        """Находит id клиента по фамилии"""
        self.cur.execute("""
            SELECT id
            FROM clients
            WHERE second_name = %s;
        """, (s_name, ))
        ap = self.cur.fetchone()
        return ap

    def find_with_email(self, email):
        """Находит id клиента по email"""
        self.cur.execute("""
            SELECT id
            FROM clients
            WHERE email = %s;
        """, (email, ))
        ap = self.cur.fetchone()
        return ap

    def find_with_phone(self, phone):
        """Находит id клиента по номеру телефона"""
        self.cur.execute("""
            SELECT c.id
            FROM clients c
            JOIN phones p ON c.id = p.client_id
            WHERE number = %s;
        """, (phone, ))
        ap = self.cur.fetchall()
        return ap

    def is_id_real(self, client_id):
        """Проверяет есть ли в базе клиент с указанным id"""
        self.cur.execute("""
            SELECT count(id)
            FROM clients
            WHERE id = %s;
        """, (client_id, ))
        ap = self.cur.fetchone()
        return ap

    def have_phone(self, client_id, number):
        """Проверяет есть у клиента указанный телефон"""
        self.cur.execute("""
            SELECT count(id)
            FROM phones
            WHERE client_id = %s and number = %s;
        """, (client_id, number))
        ap = self.cur.fetchone()
        return ap

    def is_phone(self, phone_id):
        """Проверяет есть ли в базе телефон с указанным id"""
        self.cur.execute("""
            SELECT count(id)
            FROM phones
            WHERE id = %s;
        """, (phone_id, ))
        ap = self.cur.fetchall()
        return ap

    def is_client_phones(self, client_id):
        """Проверяет зарегестрированы ли на клиента телефоны"""
        self.cur.execute("""
            SELECT count(id)
            FROM phones
            WHERE client_id = %s;
        """, (client_id, ))
        ap = self.cur.fetchone()
        return ap

    def client_info(self, client_id):
        """Запрос данных клиента по его id"""
        self.cur.execute("""
            SELECT id, first_name, second_name, email
            FROM clients
            WHERE id = %s;
        """, (client_id, ))
        ap = self.cur.fetchone()
        return ap

    def client_phones(self, client_id):
        """Запрос телефонов клиента по его id"""
        self.cur.execute("""
            SELECT id, number
            FROM phones
            WHERE client_id = %s;
        """, (client_id, ))
        ap = self.cur.fetchall()
        return ap

    def all_clients(self):
        """Запрос телефонов клиента по его id"""
        self.cur.execute("""
            SELECT id
            FROM clients;
        """)
        ap = self.cur.fetchall()
        return ap
