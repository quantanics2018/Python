def mixed_args_kwargs(arg1, arg2, *args, **kwargs):
    print("First two arguments:", arg1, arg2)
    print("Additional positional arguments:", args)
    print("Additional keyword arguments:", kwargs)

mixed_args_kwargs(1, 2, 3, 4, name='Adhiban', age=18)
# Output:
# First two arguments: 1 2
# Additional positional arguments: (3, 4)
# Additional keyword arguments: {'name': 'Adhiban', 'age': 18}
