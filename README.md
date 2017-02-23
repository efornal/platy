# platy
Diploma's application management software. It was written according to the originally  performed by gramos (Gaston Ramos) in Ruby&Rails.

### Package Installation
```bash
sudo apt-get install python2.7

pip install -r app/requirements.txt
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
