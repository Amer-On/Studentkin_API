from fastapi import FastAPI
from pandas import *
from users import *
from elders import try_elder, get_elder

app = FastAPI()

@app.get("/try_group/{group}")
async def try_group_def(group):
    return try_group(group)

@app.get("/try_group_with_flow/{flow}/{group}")
async def try_group_with_flow_def(flow, group):
    return try_group_with_flow(flow, group)

@app.get("/try_student/{group}/{first_name}/{last_name}/{patronymic}")
async def try_student_def(group, first_name, last_name, patronymic):
    return try_student(group, first_name, last_name, patronymic)

@app.get("/go_to_base/{mail}/{group}/{last_name}/{first_name}/{patronymic}/{password}")
async def go_to_base_def(mail, group, last_name, first_name, patronymic, password):
    if find_user(mail):
        return "Указанный mail уже существует"
    valid = check_valid_reg(mail, group, last_name, first_name, patronymic)
    if valid != "True":
        return valid
    go_to_base(mail, group, last_name, first_name, patronymic, password)
    return "OK"

@app.get("/delete_user/{mail}")
async def delete_user_def(mail):
    delete_user(mail)

@app.get("/try_elder/{l_name}/{f_name}/{patr}")
async def try_elder_def(l_name, f_name, patr):
    return try_elder(l_name, f_name, patr)

@app.get("/get_elder/{group}")
async def get_elder_def(group):
    return get_elder(group)

