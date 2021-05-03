#! /bin/bash

file_name="";

echo "Enter DNS (my-api.com):"
read dns
if [ ! -n "$dns" ]
then
	echo "Error: DNS variable not provided: my-api.com";
    exit 1;
fi

echo "Enter Folder name (my-api):"
read folder
if [ ! -n "$folder" ]
then
	echo "Error: folder variable not provided: my-api";
    exit 1;
fi

echo "Enter Process Name (my_api):"
read process_name
if [ ! -n "$process_name" ]
then
	echo "Error: porcess name variable not provided: my_web_app";
    exit 1;
fi

echo "Enter Port (4000):"
read port
if [ ! -n "$port" ]
then
	echo "Error: port variable not provided: 4000";
    exit 1;
fi

echo "Enter environment variable (qa):"
read envt
if [ ! -n "$envt" ]
then
	echo "Error: environtment variable not provided: qa";
    exit 1;
fi

echo "Enter virtualenv (my-venv):"
read venv
if [ ! -n "$venv" ]
then
	echo "Error: virtualenv variable not provided: /home/USER/.virtualenvs/my-venv/";
    exit 1;
fi

echo "Enter Django App name (my_django_app):"
read django
if [ ! -n "$django" ]
then
	echo "Error: Django App name variable not provided: my_django_app";
    exit 1;
fi

echo "Enter DB Name (db_name):"
read db_name
if [ ! -n "$db_name" ]
then
	echo "Error: DB Name variable not provided: db_name";
    exit 1;
fi

echo "Enter DB User (db_user):"
read db_user
if [ ! -n "$db_user" ]
then
	echo "Error: DB User variable not provided: db_user";
    exit 1;
fi

echo "Enter DB Password (db_password):"
read db_password
if [ ! -n "$db_password" ]
then
	echo "Error: DB Password variable not provided: db_password";
    exit 1;
fi

echo "Enter App ID (0):"
read app_id
if [ ! -n "$app_id" ]
then
	echo "Error: App ID variable not provided: 0";
    exit 1;
fi

echo "Enter Django workers (2):"
read django_workers
if [ ! -n "$django_workers" ]
then
	echo "Error: Django workers variable not provided: 2";
    exit 1;
fi

# ============ Functions ============
# $1 type -> nginx / supervisor
# $2 environment
# $3 dns
# $4 port
# $5 venv
# $6 django
# $7 db_name
# $8 db_user
# $9 db_password
# $10 app_id
# $11 django_workers
PopulateFile () {
    file_name="$4.$3.$2.conf";
    cp $1.conf $file_name;
    sed -i "s/PORT/$4/gi" $file_name;
    sed -i "s/DNS/$3/gi" $file_name;
    sed -i "s/ENVT/$2/gi" $file_name;
    sed -i "s/FOLDER/$folder/gi" $file_name;
    sed -i "s/PROCESS_NAME/$process_name/gi" $file_name;
    sed -i "s/VENV/$5/gi" $file_name;
    sed -i "s/DJANGO/$6/gi" $file_name;
    sed -i "s/DB_NAME/$7/gi" $file_name;
    sed -i "s/DB_USER/$8/gi" $file_name;
    sed -i "s/DB_PASSWORD/$9/gi" $file_name;
    sed -i "s/APP_ID/${10}/gi" $file_name;
    sed -i "s/DJANGO_WORKERS/${11}/gi" $file_name;
}

echo "Deploy Nginx configuration? (y/n)"
read deploy

if [ "$deploy" == "y" ]
then
	PopulateFile "nginx" "$envt" "$dns" "$port";
    sudo cp ./$file_name /etc/nginx/sites-available/;
    sudo ln -s /etc/nginx/sites-available/$file_name /etc/nginx/sites-enabled/;
    sudo nginx -t;
    sudo service nginx restart;
    echo "======================================";
    echo "$file_name:";
    cat $file_name;
    echo "======================================";
    rm ./$file_name;
fi

echo "Deploy Supervisor configuration? (y/n)"
read deploy
if [ "$deploy" == "y" ]
then
    PopulateFile "supervisor" "$envt" "$dns" "$port" "$venv" "$django" "$db_name" "$db_user" "$db_password" "$app_id" "$django_workers";
    sudo cp ./$file_name /etc/supervisor/conf.d/;
    sudo supervisorctl reread;
    sudo supervisorctl update;
    sudo supervisorctl status;
    echo "======================================";
    echo $file_name;
    cat $file_name;
    echo "======================================";
    rm ./$file_name;
fi

echo "Done"
exit 0;
