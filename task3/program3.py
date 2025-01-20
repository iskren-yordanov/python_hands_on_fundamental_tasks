"""entry point for task3"""

import json

def search_and_replace(json_obj, attribute_name):
    """ Function goes in deps and serches for the attribute_name, 
    if found it replaces the value with None.
    This is recursive since we dont know how much nested the JSON file is. 
    Recursion is executed only is a type of List or Dict is present
    since those types can have inner values to check for attribute_name
    """
    for el in json_obj:
        if attribute_name in el:
            el[attribute_name] = None

        # if type is Dict or List, check if any of the inside values can have lower leves
        if isinstance(el, (dict,list)):
            for key in el:
                #print(type(el[e]), el[e])
                if isinstance(el[key], (dict, list)):
                    search_and_replace(el[key], attribute_name)


def modify_json_file(original_file_name: str, new_file_name: str, att_name: str) -> bool:
    """main function to read and write the Json Data"""
    with open("task3/" + original_file_name + ".json", "r", encoding="UTF8") as f1:
        data = json.load(f1)

    search_and_replace(data, att_name)

    with open("task3/" + new_file_name + ".json", "w", encoding="UTF8") as f2:
        json.dump(data, f2)

if __name__=="__main__":
    modify_json_file("src_data", "new_src_data", "name")
