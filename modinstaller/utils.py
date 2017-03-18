def bind(control, bind_type):
    def bind_(func):
        control.Bind(bind_type, func)
    return bind_