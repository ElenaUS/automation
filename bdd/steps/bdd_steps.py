# каким образом реализован
from behave import *
from fixture.fixture import Fixture
from model.login import Login
from model.base import Base


@given("Log in as a specific user {name}")
def login_check(fix, name):
    fix.check.check_profile(Login(username=name))

@when("Сleanup of gaps in database data {id} {amount} {username}")
def clean_bd(fix, id, amount, username):
    clean = Base(id=id, amount=amount, username=username.strip())
    return clean
    res = map(clean, db.get_group_list())


@then("Equal number of tables {amount}")
def asser_end(fix, amount):
    old_list = fix.check.get_list()
    fix.check.create_amount(amount)
    new_group = fix.check.get_list()
    assert len(old_list) == len(new_group), "Списки транзакций не равны"