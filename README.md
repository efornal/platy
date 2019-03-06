# platy
Diploma's application management software. It was written according to the originally  performed by gramos (Gaston Ramos) in Ruby&Rails.


### Package Installation debian stretch
```bash
sudo apt-get install python-dev
sudo apt-get install python-pip
sudo apt-get install libpq-dev
sudo apt-get install libyaml-dev
sudo apt-get install libldap2-dev
sudo apt-get install libsasl2-dev
sudo apt-get install gettext
sudo apt-get install libjpeg-dev
sudo apt-get install zlib1g-dev
sudo apt-get install python-dnspython # for reidi
sudo apt-get install mariadb-client # for dumpserver
sudo apt-get install pkg-config
sudo apt-get install libgtk2.0-dev
sudo apt-get install libgirepository1.0-dev
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
