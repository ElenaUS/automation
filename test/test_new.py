# -*- coding: utf-8 -*-
from model.base import Base
from model.login import Login
import pytest

def test_new(fix, json_data, db):
    element = json_data
    fix.check.check_profile(Login(username="Hermoine Granger"))

    def clean(data):
        return Base(id=data.id, amount=data.amount, username=data.username.strip())

    res = map(clean, db.get_group_list())

    old_list = fix.check.get_list()
    fix.check.create_amount(element)
    new_group = fix.check.get_list()
    # assert len(old_list) == len(new_group), "Списки транзакций не равны"
    print(old_list)

