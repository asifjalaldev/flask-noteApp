from website import create_app

app= create_app()


if __name__ =='__main__':
    # i want to run flask app only when main.py run not other file in same folder
    app.run(debug=True)
