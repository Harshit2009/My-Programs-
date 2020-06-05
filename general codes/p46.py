try :
    import mymodule
except ImportError :
    print("Whoa! We seem to be missing a module we require here.")
    import sys
    sys.exit()
