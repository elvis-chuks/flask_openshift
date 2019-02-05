from flask import Flask, flash, request,render_template, redirect, url_for, session, make_response


################# routes ####################################
@application.route("/")
def index():
    return 'hello world'

if __name__ == "__main__":
    application.run(debug=True)
