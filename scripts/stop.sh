#!/bin/bash

PROJECT="/opt/swiper"

# 关掉 gunicorn
cat $PROJECT/logs/gunicorn.pid | xargs kill
