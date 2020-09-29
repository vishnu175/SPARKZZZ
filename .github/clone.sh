#!/bin/bash














FILE=/app/.git

if [ -d "$FILE" ] ; then

    echo "$FILE directory exists already."

else

    git clone https://github.com/vishnu175/SPARKZZZ sparkzzz_ub

    rm -rf userbot

    mv sparkzzz_ub/.git .

    mv sparkzzz_ub/userbot .

    rm -rf sparkzzz_ub

    python ./.github/update.py

fi

python -m userbot
