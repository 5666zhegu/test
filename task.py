#熟悉了如何去使用字典去设置任务
#有数字的话可以先设置一个全局变量
#字符串的设定后面可以加个.strip()
# 用expect去接受数字，更加有保障，不会因为输入错误而退出代码
#一行式的代码（if else）判断更加简洁和方便



todo_list = []
current_id = 1

def show_menu() :
    print("\n任务管理器")
    print("1.添加任务")
    print("2.显示所有任务")
    print("3.修改任务内容")
    print("4.删除任务")
    print("5.标记完成/未完成")
    print("6.退出任务")

def add_task() :
    global current_id
    content = input("请输入你要添加的任务：").strip()
    new_task = {
        'id': current_id,
        'content' : content,
        'complete' : False
    }
    todo_list.append(new_task)
    current_id += 1
    print(f"已添加任务：({new_task['id']}.{new_task['content']})")

def show_task() :
    if not todo_list :
        print("目前暂无任务")
        return
    print("任务列表如下所示：")
    for task in todo_list :
        status = "√" if task['complete'] else "×"
        print(f"{task['id']}.({status}) {task['content']}")

def find_task_by_id(task_id) :
    for task in todo_list :
        if task['id'] == task_id :
            return task
        return None


def modify_task() :
    task_id = input("你要修改的任务ID是：")
    try :
        task_id = int(task_id)
    except ValueError :
        print("你输入的是无效信息")
        return

    task = find_task_by_id(task_id)
    if not task :
        print("你所查找的任务ID为空")
        return
    new_content = input("任务修改的内容为:").strip()
    task['content'] = new_content
    print(f"任务已经修改完成，{task['id']}.{task['content']}")

def delete_task() :
    task_id = input("请输入你想要删除任务的ID:")
    try :
        task_id = int(task_id)
    except ValueError :
        print("请输入有效数字内容")
        return
    global todo_list
    todo_list_length = len(todo_list)
    todo_list = [task for task in todo_list if task['id'] != task_id]
    if len(todo_list) < todo_list_length :
        print("任务删除成功")
    else :
        print("没有找到ID所对应的任务")
def toggle_complete() :
    task_id = input("请输入你要修改的状态的ID:")
    try :
        task_id = int(task_id)
    except ValueError :
        print("请输入有效内容:")
        return

    task = find_task_by_id(task_id)
    task['complete'] = not task['complete']
    status = "完成" if task['complete'] else "未完成"
    print(f"成功修改状态为{status}")

while True :
    show_menu()
    choice = int(input("请选择（1-6）中的其中一项："))
    if choice == 1 :
        add_task()
    elif choice == 2 :
        show_task()
    elif choice == 3 :
        modify_task()
    elif choice == 4 :
        delete_task()
    elif choice == 5 :
        toggle_complete()
    elif choice == 6 :
        print("任务结束")
        break
    else :
        print("输入无效，请重新尝试")







