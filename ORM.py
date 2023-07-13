import json
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy.dialects.mysql import INTEGER, FLOAT


Base = declarative_base()


class Publisher(Base):
    __tablename__ = "publisher"
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=60), unique=True)


class Shop(Base):
    __tablename__ = "shop"
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=60), unique=True)


class Book(Base):
    __tablename__ = "book"
    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=60), unique=True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"), nullable=False)

    publisher = relationship(Publisher, backref="book")


class Stock(Base):
    __tablename__ = "stock"
    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book.id"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), nullable=False)
    count = sq.Column(INTEGER(unsigned=True), nullable=False)

    book = relationship(Book, backref="stock")
    shop = relationship(Shop, backref="stock")


class Sale(Base):
    __tablename__ = "sale"
    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(FLOAT(5, 2, unsigned=True), nullable=False)
    date_sale = sq.Column(sq.DATE, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    stock = relationship(Stock, backref="sale")


def create_tables(engine):
    Base.metadata.create_all(engine)


def drop_tables(engine):
    Base.metadata.drop_all(engine)


if __name__ == "__main__":
    DSN = "postgresql://postgres_1:123456789@localhost:5432/postgres_2"
    engine = sq.create_engine(DSN)
    drop_tables(engine)
    create_tables(engine)
    Session = sessionmaker(bind=engine)

    with open('tests_data.json', 'r') as fd:
        data = json.load(fd)

    session = Session()
    for record in data:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[record.get('model')]
        session.add(model(id=record.get('pk'), **record.get('fields')))
    session.commit()

    req = input("Input name or id of publisher: ")

    try:              # req is number or text?
        req = int(req)
        a = False
    except ValueError:
        a = True

    if a:
        if session.query(Publisher).filter(Publisher.name == req).all():
            for i in session.query(Book.title, Shop.name, Sale.price, Sale.date_sale)\
                    .join(Publisher).join(Stock).join(Shop).join(Sale).filter(Publisher.name == req).all():
                title, shop, price, date = i
                print(f"{title} | {shop} | {price} | {date}")
        else:
            print("Have not this publisher in the database")
    elif session.query(Publisher).filter(Publisher.id == req).all():
        for i in session.query(Book.title, Shop.name, Sale.price, Sale.date_sale)\
                .join(Publisher).join(Stock).join(Shop).join(Sale).filter(Publisher.id == req).all():
            title, shop, price, date = i
            print(f"{title} | {shop} | {price} | {date}")
    else:
        print("Have not this publisher_id in the database")
    session.close()
