# platy
Diploma's application management software. It was written according to the originally  performed by gramos (Gaston Ramos) in Ruby&Rails.


### Package Installation debian buster
```bash
apt install git
apt install python-dev
apt install python-pip
apt install pkg-config
apt install libpq-dev
apt install libyaml-dev
apt install libldap2-dev
apt install libsasl2-dev
apt install gettext
apt install libjpeg-dev
apt install zlib1g-dev
apt install libgtk2.0-dev
apt install libgirepository1.0-dev
```

### Python lib Installation
```bash
pip install -r requirements.txt
```

### Application configuration
```bash
cp sdump/settings.tpl.py sdump/settings.py
```

### Util commands
```bash
python manage.py migrate --database=platy_owner

pip freeze > requirements.txt
```

### Postgres configuration
```bash
createdb sdump_db;
createuser sdump_owner -P;

/etc/postgresql/9.4/main/pg_hba.conf
hostssl  sdump_db     sdump_owner        ::1/128                 password
/etc/init.d/postgresql restart
psql -h localhost -U sdump_owner -p 5432 -d sdump_db
```
