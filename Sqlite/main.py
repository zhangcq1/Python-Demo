import sqlite3  #导入标准库sqlite
import random  #导入标准库random


def init():
    con = sqlite3.connect(':memory:')
    cur = con.cursor()
    cur.execute('create table mytab(id integer primary key autoincrement not null ,name text ,password text )')
    return con,cur

def add(cur):
    name = input('请输入用户名:')
    pwd = input('请输入密码:')
    cur.execute('insert into mytab (name,password)values(?,?)',(name,pwd))
    print("添加成功")
def delete(cur):
    sid = input('请输入要删除的数据id:')
    if sid.isdigit():
        cur.execute('delete from mytab WHERE id =?',(sid))
        print("删除成功")
    else:
        print("你的输入有误!")

def update(cur):
    sid = input('请输入要更新的数据id:')
    name = input('请输入更新后的用户名:')
    pwd = input('请输入更新后的密码:')
    cur.execute('update mytab set name=?,password=? where id=?',(name,pwd,sid))
    print("更新成功")

def find(cur):
    print("查找所有数据")
    cur.execute('select * from mytab')
    for sid,name,pwd in cur:
        print(sid,name,pwd,sep='---')
def fun():
    cmd = {'add':add,
           'delete':delete,
           'update':update,
           'find':find,
           }
    con, cur = init()
    while 1:
        cd = input('请输入字符命令:\t'
                   'add:添加一条数据\t'
                   'delete:删除一条数据\t'
                   'update:修改一条数据\t'
                   'find:查找数据\t'
                   'exit:退出\n'
                   '请输入:'
                   )
        if cd=='exit':
            cur.close()
            con.close()
            break
        elif cd in cmd.keys():
            cmd[cd](cur)
        else:
            print("你输入的命令有误,请重新输入!")
fun()