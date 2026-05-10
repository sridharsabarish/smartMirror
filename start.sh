#! /bin/bash 

cd src

python3 -m serverForhumidity.py  &

python3 app.py & 
