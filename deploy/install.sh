#! /bin/bash

file_name="";
show_help_message="To display help, use: ./install.sh -h";

if [ "$1" == "-h" ]
then
	cat ./install.txt
    exit 0;
fi

while getopts d:f:n:p:e: flag
do
    case "${flag}" in
        d) dns=${OPTARG};;
        f) folder=${OPTARG};;
        n) porcess_name=${OPTARG};;
        p) port=${OPTARG};;
        e) envt=${OPTARG};;
    esac
done

# ============ Functions ============
# $1 type -> nginx / supervisor
# $2 environment
# $3 dns
# $4 port
PopulateFile () {
    file_name="$4.$3.$2.conf";
    cp $1.conf $file_name;
    sed -i "s/PORT/$4/gi" $file_name;
    sed -i "s/DNS/$3/gi" $file_name;
    sed -i "s/ENVT/$2/gi" $file_name;
    sed -i "s/FOLDER/$folder/gi" $file_name;
    sed -i "s/PROCESS_NAME/$porcess_name/gi" $file_name;
}

if [ ! -n "$dns" ]
then
	echo "Error: DNS variable not provided: -d my-web-app.com";
    echo $show_help_message;
    exit 1;
fi
if [ ! -n "$folder" ]
then
	echo "Error: folder variable not provided: -f my-web-app";
    echo $show_help_message;
    exit 1;
fi
if [ ! -n "$porcess_name" ]
then
	echo "Error: porcess name variable not provided: -n my_web_app";
    echo $show_help_message;
    exit 1;
fi
if [ ! -n "$port" ]
then
	echo "Error: port variable not provided: -p 4000";
    echo $show_help_message;
    exit 1;
fi
if [ ! -n "$envt" ]
then
	echo "Error: environtment variable not provided: -e qa";
    echo $show_help_message;
    exit 1;
fi

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
    PopulateFile "supervisor" "$envt" "$dns" "$port";
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
