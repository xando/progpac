#!/bin/sh
./progpac/static/limejs/bin/lime.py build game -o progpac/static/game/game-min.js 
heroku config:set GIT_REV=`git rev-parse HEAD`
python progpac/manage.py compress --settings=compress_settings
python progpac/manage.py collectstatic -i limejs --noinput -v 2
heroku maintenance:on
git push heroku master
heroku run python progpac/manage.py migrate core 
heroku maintenance:off
