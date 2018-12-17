#!/bin/bash

PROJECT="/opt/swiper"

cat $PROJECT/logs/gunicorn.pid | xargs kill -HUP
