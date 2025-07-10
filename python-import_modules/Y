#!/usr/bin/python3
import importlib.util

def main():
    # 1. hidden_4.pyc faylını yüklə
    spec = importlib.util.spec_from_file_location("hidden_4", "/tmp/hidden_4.pyc")
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    # 2. Modulun içindəki adları çap et, __ ilə başlayanlar istisna
    names = [name for name in dir(hidden_4) if not name.startswith("__")]
    names.sort()
    for name in names:
        print(name)

if __name__ == "__main__":
    main()
