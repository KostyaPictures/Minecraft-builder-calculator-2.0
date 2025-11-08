import json

def get_names(path):
    l=[]
    jsonf=path+"\\config\\code.json"
    with open(jsonf, 'r', encoding="UTF-8") as file:
        conf = json.load(file)
        for i in conf:
            l.append(i)
        return l
    #print(get_names("D:\prog\minecraftBuilderCalculator2-0"))

def get_conf(path):
    l=[]
    jsonf=path+"\\config\\config.json"
    with open(jsonf, 'r', encoding="UTF-8") as file:
        conf = json.load(file)
        for c in conf:
            l.append(conf[c])
        return l
    #print(get_conf("D:\prog\minecraftBuilderCalculator2-0",3))

def get_save(path):
    jsonf=path+"\\config\\config.json"
    with open(jsonf, 'r', encoding="UTF-8") as file:
        save = json.load(file)
        for c in save:
            if c=="save_config":
                return save[c]

def get_rnd(path):
    jsonf=path+"\\config\\config.json"
    with open(jsonf, 'r', encoding="UTF-8") as file:
        rnd = json.load(file)
        for c in rnd:
            if c=="do_not_round":
                return rnd[c]

def get_stack(path):
    jsonf=path+"\\config\\config.json"
    with open(jsonf, 'r', encoding="UTF-8") as file:
        stack = json.load(file)
        for c in stack:
            if c=="stack_items":
                return stack[c]

def get_logs(path):
    jsonf=path+"\\config\\config.json"
    with open(jsonf, 'r', encoding="UTF-8") as file:
        logs = json.load(file)
        for c in logs:
            if c=="in_logs":
                return logs[c]

def change_conf(path, ind, value_):
    with open(path+"\\config\\config.json", 'r+', encoding="UTF-8") as f_wr:
        data = json.load(f_wr)
        print(f"data: {data}")
        l=[]
        for j in data:
            print(f"j: {j}")
            l.append(j)
            print(f"l: {l}")
        name=l[ind]
        print(f"name: {name}")

        try:
            data.update({name: value_})
        except KeyError:
            return False

        f_wr.seek(0)
        json.dump(data, f_wr, indent=2)
        f_wr.truncate()
        return True
    #change_conf("D:\prog\minecraftBuilderCalculator2-0", 2, True)

def get_values(name, path):
    jsonf=path+"\\config\\code.json"
    with open(jsonf, 'r', encoding="UTF-8") as file:
        dct = json.load(file)
        return dct[name]

def to_default(path):
    with open(path+"\\config\\config.json", 'r+', encoding="UTF-8") as f_wr:
        data = json.load(f_wr)
        try:
            data.update({
                "in_logs": False,
                "stack_items": True,
                "do_not_round": False,
                "save_config": False,
                "cb1": "blocks",
                "cb2": "blocks",
                "ent_1": ""
            })
        except KeyError:
            return False

        f_wr.seek(0)
        json.dump(data, f_wr, indent=2)
        f_wr.truncate()
        return True