from turtle import *


def snowflake_koxa(km):
    if km > 6:
        km = km // 3
        snowflake_koxa(km)
        lt(60)
        snowflake_koxa(km)
        rt(120)
        snowflake_koxa(km)
        lt(60)
        snowflake_koxa(km)
    else:
        fd(km)
        lt(60)
        fd(km)
        rt(60 * 2)
        fd(km)
        lt(60)
        fd(km)

up()
goto(-100, 100)
down()
shape("turtle")
speed(-1)
snowflake_koxa(100)
rt(60 * 2)
snowflake_koxa(100)
rt(60 * 2)
snowflake_koxa(100)
mainloop()