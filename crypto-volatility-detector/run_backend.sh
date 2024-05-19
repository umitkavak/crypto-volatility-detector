#!/bin/bash
cd backend
source ../venv/bin/activate
export FLASK_APP=app.py
flask run
