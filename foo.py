def args_try(main_arg, *args, **kwargs):
    print(f"main arg : {main_arg}")
    print(f"var args : ")
    for i, j in enumerate(args, 0):
        print(f"i : {i}\t j : {j}")
    print(f"key word args : ")
    for key, item in kwargs.items():
        print(f"Key : {key}\t item : {item}")

print("Hello!")
args_try("foo", "bar1", "bar2", "bar3", pos1=0, pos2="1", pos3=2.0, pos4="three")

