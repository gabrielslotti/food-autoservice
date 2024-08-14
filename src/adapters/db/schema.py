from contextlib import contextmanager
from sqlalchemy import (
    create_engine,
    ForeignKey,
    String,
    Integer,
    Float,
    Text,
)
from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    Mapped,
    mapped_column,
)
from sqlalchemy.dialects.postgresql import JSONB

# Internal imports
from settings import settings

SQLALCHEMY_DATABASE_URL = str(settings.db_url)
Base = declarative_base()


class DBSession:
    def __init__(self) -> None:
        self.engine = create_engine(SQLALCHEMY_DATABASE_URL)
        self.Session = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine
        )

    @contextmanager
    def get_db(self):
        session = self.Session()
        try:
            yield session
        finally:
            session.close()


class CustomerTable(Base):
    __tablename__ = "customer"

    id: Mapped[Integer] = mapped_column(type_=Integer, primary_key=True)
    cpf: Mapped[String(11)] = mapped_column(type_=String(11), nullable=False)
    first_name: Mapped[String(60)] = mapped_column(type_=String(60), nullable=False)
    last_name: Mapped[String(60)] = mapped_column(type_=String(60), nullable=False)
    email: Mapped[String(120)] = mapped_column(type_=String(120), nullable=False)


class ItemsCategoryTable(Base):
    __tablename__ = 'items_category'

    id: Mapped[Integer] = mapped_column(type_=Integer, primary_key=True)
    description: Mapped[String(40)] = mapped_column(type_=String(40), nullable=False)


class ItemsTable(Base):
    __tablename__ = 'items'

    id: Mapped[Integer] = mapped_column(type_=Integer, primary_key=True)
    title: Mapped[String(120)] = mapped_column(type_=String(120), nullable=False)
    description: Mapped[Text()] = mapped_column(type_=Text(), nullable=False)
    category: Mapped[Integer] = mapped_column(ForeignKey("items_category.id"))
    amount: Mapped[Integer] = mapped_column(type_=Integer, nullable=False)
    price: Mapped[Float] = mapped_column(type_=Float, nullable=False)


class OrderStatusTable(Base):
    __tablename__ = 'order_status'

    id: Mapped[Integer] = mapped_column(type_=Integer, primary_key=True)
    description: Mapped[String(20)] = mapped_column(type_=String(20), nullable=False)


class OrderTable(Base):
    __tablename__ = 'order'

    id: Mapped[Integer] = mapped_column(type_=Integer, primary_key=True)
    customer_id: Mapped[id] = mapped_column(type_=Integer, nullable=True)
    status: Mapped[Integer] = mapped_column(ForeignKey("order_status.id"))
    items: Mapped[JSONB] = mapped_column(type_=JSONB, nullable=False)
