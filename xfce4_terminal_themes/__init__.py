try:
    from setproctitle import setproctitle
    setproctitle('xfce4-terminal-themes')
except ImportError:
    pass
