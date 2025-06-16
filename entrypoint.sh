#!/bin/bash

set -e  # Exit on error

if [ "$(hostname)" != "django-container" ]; then
  # echo "Skipping initialization script because hostname is not 'django-container'."
  exec "$@"
  exit 0
fi

REQUIRED_VARS=("DB" "DB_USER" "PASSWORD" "HOST")

# echo "🔍 Checking required environment variables..."
for VAR in "${REQUIRED_VARS[@]}"; do
  if [ -z "${!VAR}" ]; then
    echo "❌ Environment variable $VAR is not set. Please read the documentation on Github and check your .env file."
    exit 1
  fi
done
# echo "✅ All required environment variables are set."

# echo "🔄 Waiting for MySQL to be ready at $HOST:$PORT..."
until mysql -h "$HOST" -P "$PORT" -u "root" -p"$ROOTPW" -D "$DB" -e "SELECT 1;" &> /dev/null; do
  sleep 1
done
# echo "✅ MySQL is ready."

# Check if the 'stations' table exists
# echo "🔍 Checking if 'stations' table exists in database '$DB'..."
TABLE_EXISTS=$(mysql -h "$HOST" -P "$PORT" -u "$USER" -p"$ROOTPW" -D "$DB" -sse "SHOW TABLES LIKE 'stations';")

if [ "$TABLE_EXISTS" != "stations" ]; then
  python manage.py migrate
  echo "📦 This seems to be your first time running this project. The initialization process may take some time..."
  python manage.py fetcher &
# else
  # echo "✅ 'stations' table already exists. Skipping migration and custom command."
fi

# echo "🚀 Starting application..."
exec "$@"
