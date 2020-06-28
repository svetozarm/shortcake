import os
import random
import sqlalchemy
from datetime import datetime

from app.models import ShortcakeUrl
from app import db

from app.foodname import FoodName


food_name = FoodName()


def get_domain():
    # uncomment this for production
    # return "http://shortcake.xyz/"
    return "http://localhost:5000/"


def get_stored(url):
    retval = ShortcakeUrl.query.filter_by(url=url).first()
    return retval


def get_new(url, date=None):
    suffix = ""
    while True:
        shortcake_url = get_domain() + food_name.generate(url + suffix)
        new_entry = ShortcakeUrl(
            url=url,
            shortcake_url=shortcake_url,
            expiry=datetime.utcnow(),
            ip_address=0,
        )
        try:
            db.session.add(new_entry)
            db.session.commit()
            return new_entry
        except sqlalchemy.exc.IntegrityError as e:
            db.session.rollback()
            if "shortcake_url.shortcake_url" in e.args[0]:
                suffix = f"{suffix} "
            else:
                return None


def get_short(url):
    if shortened := get_stored(url):
        return shortened
    return get_new(url)
