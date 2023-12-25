def args_try(main_arg, *args, **kwargs):
    print(f"main arg : {main_arg}")
    print(f"var args : {args}")
    print(f"key word args : {kwargs}")

print("Hello!")
args_try("foo", "bar1", "bar2", "bar3", pos1=0, pos2="1", pos3=2.0, pos4="three")

