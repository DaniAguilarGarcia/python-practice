from flask import Flask, request
@app.route("/book/<isbn>")
def get_author(isbn):
    res = request.get("https://openlibrary.org/isbn/{escape(isbn)}.JSON")

    if res.status_code == 200:
        return {"message": res.JSON()}
    elif res.status_code == 404:
        return {"message" : "Network not found!"}
    else:
        return {"message" : "something went wrong"}