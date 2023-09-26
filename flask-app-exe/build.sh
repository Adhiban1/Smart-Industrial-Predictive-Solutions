python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
pyinstaller --onefile --name run app.py
./dist/run