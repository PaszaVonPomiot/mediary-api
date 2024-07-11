from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlmodel import Field, Session, SQLModel, create_engine, select

app = FastAPI()

# SQLite database URL
sqlite_file_name = "mediary.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# Create the database engine
engine = create_engine(sqlite_url, echo=True)


# Define the User model
class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    email: str


# Create the database tables
SQLModel.metadata.create_all(engine)


# Define the Pydantic model for user creation
class UserCreate(BaseModel):
    name: str
    email: str


@app.post("/users/", response_model=User)
def create_user(user: UserCreate):
    with Session(engine) as session:
        db_user = User.from_orm(user)
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user


@app.get("/users/", response_model=list[User])
def read_users(skip: int = 0, limit: int = 10):
    with Session(engine) as session:
        users = session.exec(select(User).offset(skip).limit(limit)).all()
        return users


@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    with Session(engine) as session:
        user = session.get(User, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user


@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: UserCreate):
    with Session(engine) as session:
        db_user = session.get(User, user_id)
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        db_user.name = user.name
        db_user.email = user.email
        session.commit()
        session.refresh(db_user)
        return db_user


@app.delete("/users/{user_id}", response_model=User)
def delete_user(user_id: int):
    with Session(engine) as session:
        user = session.get(User, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        session.delete(user)
        session.commit()
        return user
