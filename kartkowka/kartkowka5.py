#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
a = {"a":1,"b":3,"c":3, "d":10, "e":10}
def kartkowka(ini_dict):
    print("Słownik początkowy", str(ini_dict))
    result = {}
    for key, value in ini_dict.items():
        if value not in result.values():
            result[key] = value
    return result
print("Słownik bez duplikacji",kartkowka(a))