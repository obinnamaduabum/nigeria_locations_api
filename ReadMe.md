python manage.py makemigrations name_of_application

python3 manage.py migrate

#Activate
source env/bin/activate

#run dependencies 
pip3 install -r requirements.txt

# generate dependencies 
pip3 freeze > requirements.txt

# run app
python3 manage.py runserver