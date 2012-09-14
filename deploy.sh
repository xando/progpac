#!/bin/sh

INSTANCE=$1
DIR=$(dirname $0)


$DIR/progpac/static/limejs/bin/lime.py build game -o progpac/static/game/game-min.js 

python $DIR/progpac/manage.py compress --settings=compress_settings
python $DIR/progpac/manage.py collectstatic -i limejs --noinput -v 2

heroku config:set GIT_REV=`git rev-parse HEAD` -a $INSTANCE
heroku maintenance:on -a $INSTANCE

git push $INSTANCE master 
heroku run -a $INSTANCE python $DIR/progpac/manage.py syncdb --noinput 
heroku run -a $INSTANCE python $DIR/progpac/manage.py migrate core 

heroku maintenance:off -a $INSTANCE
