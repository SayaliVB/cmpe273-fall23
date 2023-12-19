mkdir lab2
cd lab2

python3 -m venv virtualenv

source virtualenv/bin/activate
pip3 install 'strawberry-graphql[debug-server]'

pip3 install 'strawberry-graphql[fastapi]'

strawberry server main(from main.py)