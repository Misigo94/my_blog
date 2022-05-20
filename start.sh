export MAIL_USERNAME=misigomart@gmail.com
export MAIL_PASSWORD=Misigomart94
export SECRET_KEY='1234'
export SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://martin3:password@localhost:5432/blogdb'

#  python3.9 manage.py migrate
# python3.9 manage.py shell
python3.9 manage.py server

