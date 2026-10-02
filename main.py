from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

@app.get("/", summary="Главный на районе" , tags=["Boss"])
def root():
    return "Hello world"

books = [
    {
        "id": 1,
        "title": "ASD67",
        "author": "Tim Coock"
    },
    {
        "id": 2,
        "title": "Backshot",
        "author": "Billy Harington"
    }
]

@app.get(
    "/books",
    tags=["books"],
    summary="Get all books"
)
def read_books():
    return books

@app.get(
    "/books/{book_id}",
    tags=["books"],
    summary="Get specific books"
)
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")



class NewBook(BaseModel):
    tittle: str
    author: str



@app.post("/books",
          tags=["books"]
          )
def create_book(new_book: NewBook):
    books.append({
        "id": len(books)+1,
        "tittle": new_book.tittle,
        "author": new_book.author
    })
    return {"success": True, "message": "book destroyed"}