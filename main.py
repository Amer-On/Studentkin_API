from fastapi import FastAPI
import uvicorn
from checker import *
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

@app.get("/go_to_base/{email}/{group}/{last_name}/{first_name}/{patronymic}/{password}")
async def gtb(email, group, last_name, first_name, patronymic, password):
    try:
        go_to_base(email, group, last_name, first_name, patronymic, password)
        return "OK"
    except:
        return "NOT OK"

@app.get("/reg_validness/{email}/{group}/{last_name}/{first_name}/{patronymic}/{password}")
async def reg_validness(email, group, last_name, first_name, patronymic):
    response = {
        "email": "mail_busy" if find_user(email) else check_email(email),
        "group": "valid" if try_group(group) else "invalid",
        "name": "valid" if try_student(group, last_name, first_name, patronymic) else "invalid"
    }
    return response

@app.get("/email_validness/{email}")
async def email_validness(email):
    return "mail_busy" if find_user(email) else check_email(email)

@app.get("/group_validness/{group}")
async def group_validness(group):
    return "valid" if try_group(group) else "invalid"

@app.get("/name_validness/{group}/{last_name}/{first_name}/{patronymic}")
async def name_validness(group, last_name, first_name, patronymic):
    return "valid" if try_student(group, last_name, first_name, patronymic) else "invalid"

@app.get("/delete_user/{mail}")
async def delete_user_def(mail):
    delete_user(mail)

@app.get("/try_elder/{l_name}/{f_name}/{patr}")
async def try_elder_def(l_name, f_name, patr):
    return try_elder(l_name, f_name, patr)

@app.get("/get_elder/{group}")
async def get_elder_def(group):
    return get_elder(group)

@app.get("/get_group/{email}")
async def gg(email):
    return find_group(email)

@app.get("/get_user_l/{email}")
async def get_user_l_def(email):
    return get_user_l(email)

@app.get("/get_user_f/{email}")
async def get_user_f_def(email):
    return get_user_f(email)

@app.get("/get_user_p/{email}")
async def get_user_p_def(email):
    return get_user_p(email)

if __name__ == "__main__":
    uvicorn.run(app, host="185.117.155.28", port=8000)
    # uvicorn.run(app, host="127.0.0.1", port=8000) # localhost

