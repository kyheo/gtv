# Install postgres and postgis
apt-get update
apt-get install -y postgresql-9.3 \
                   postgresql-9.3-postgis-2.1 \
                   postgresql-server-dev-9.3 \
                   postgresql-client-9.3 

# Create user an database.
sudo -u postgres psql --command="CREATE USER geodjango PASSWORD '1234';"
sudo -u postgres psql --command="CREATE DATABASE gtv OWNER geodjango ENCODING 'utf8';"
sudo -u postgres psql --command="GRANT ALL PRIVILEGES ON DATABASE gtv to geodjango;"
sudo -u postgres psql gtv --command='CREATE EXTENSION postgis'

# Change listen parameter
CONF_DIR="/etc/postgresql/9.3/main"
sed -i.bak s"/#listen_addresses = 'localhost'/listen_addresses = '*'/"g $CONF_DIR/postgresql.conf
echo  'host    all             all             0.0.0.0/0            md5' >> $CONF_DIR/pg_hba.conf
/etc/init.d/postgresql restart
