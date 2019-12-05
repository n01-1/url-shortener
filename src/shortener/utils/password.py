import logging

from passlib.hash import argon2

logger = logging.getLogger(__name__)


def hash_password(raw_password):
    return argon2.hash(raw_password)


def compare_password(raw_password, hashed_password):
    return argon2.verify(raw_password, hashed_password)
