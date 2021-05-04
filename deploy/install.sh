#! /bin/bash

file_name="";

echo "Enter DNS (api-staging.solefi.iguzman.com.mx):"
read dns
if [ ! -n "$dns" ]
then
	echo "Error: DNS variable not provided: i.e. api-staging.solefi.iguzman.com.mx";
    exit 1;
fi

echo "Enter Folder name (solefi-cms):"
read folder
if [ ! -n "$folder" ]
then
	echo "Error: folder variable not provided: solefi-cms";
    exit 1;
fi

echo "Enter Process Name (solefi_cms_staging):"
read process_name
if [ ! -n "$process_name" ]
then
	echo "Error: porcess name variable not provided: solefi_cms_staging";
    exit 1;
fi

echo "Enter Port (4010):"
read port
if [ ! -n "$port" ]
then
	echo "Error: port variable not provided: 4010";
    exit 1;
fi

echo "Enter environment variable (staging):"
read envt
if [ ! -n "$envt" ]
then
	echo "Error: environtment variable not provided: staging";
    exit 1;
fi

echo "Enter virtualenv (solefi):"
read venv
if [ ! -n "$venv" ]
then
	echo "Error: virtualenv variable not provided: solefi";
    exit 1;
fi

echo "Enter Django App name (solefi_cms):"
read django_app_name
if [ ! -n "$django_app_name" ]
then
	echo "Error: Django App name variable not provided: solefi_cms";
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

echo "Enter Email ID (john@doe.com):"
read email_id
if [ ! -n "$email_id" ]
then
	echo "Error: Email ID variable not provided: 2";
    exit 1;
fi

echo "Enter Email password (******):"
read email_password
if [ ! -n "$email_password" ]
then
	echo "Error: Email password variable not provided: 2";
    exit 1;
fi

# ============ Functions ============
# $1 type -> nginx / supervisor
PopulateFile () {
    file_name="$port.$dns.$envt.conf";
    sudo cp $1.conf $file_name;
    sed -i "s/PORT/$port/g" $file_name;
    sed -i "s/DNS/$dns/g" $file_name;
    sed -i "s/ENVT/$envt/g" $file_name;
    sed -i "s/FOLDER/$folder/g" $file_name;
    sed -i "s/PROCESS_NAME/$process_name/g" $file_name;
    sed -i "s/VENV/$venv/g" $file_name;
    sed -i "s/OS_USER/$USER/g" $file_name;
    sed -i "s/DJANGO_APP_NAME/$django_app_name/g" $file_name;
    sed -i "s/DB_NAME/$db_name/g" $file_name;
    sed -i "s/DB_USER/$db_user/g" $file_name;
    sed -i "s/DB_PASSWORD/$db_password/g" $file_name;
    sed -i "s/APP_ID/$app_id/g" $file_name;
    sed -i "s/DJANGO_WORKERS/$django_workers/g" $file_name;
    sed -i "s/EMAIL_ID/$email_id/g" $file_name;
    sed -i "s/EMAIL_PASSWORD/$email_password/g" $file_name;
}

echo "Create Nginx configuration? (y/n)"
read create

if [ "$create" == "y" ]
then
	PopulateFile "nginx";
    echo "======================================";
    echo "$file_name:";
    cat $file_name;
    echo "======================================";
    echo "Deploy Nginx configuration? (y/n)"
    read deploy
    if [ "$deploy" == "y" ]
    then
        sudo cp ./$file_name /etc/nginx/sites-available/;
        sudo ln -s /etc/nginx/sites-available/$file_name /etc/nginx/sites-enabled/;
        sudo nginx -t;
        sudo service nginx restart;
    fi
    sudo rm ./$file_name;
fi

echo "Create Supervisor configuration? (y/n)"
read create
if [ "$create" == "y" ]
then
    PopulateFile "supervisor";
    echo "======================================";
    echo $file_name;
    cat $file_name;
    echo "======================================";
    echo "Deploy Supervisor configuration? (y/n)"
    read deploy
    if [ "$deploy" == "y" ]
    then
        sudo cp ./$file_name /etc/supervisor/conf.d/;
        sudo supervisorctl reread;
        sudo supervisorctl update;
        sudo supervisorctl status;
    fi
    sudo rm ./$file_name;
fi

echo "Done"
exit 0;
