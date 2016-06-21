import rabbyt
print rabbyt.anims.__file__

def setup():
    global anim
    anim = rabbyt.lerp(0,100, dt=100, extend="extrapolate").force_complete()

def test():
    rabbyt.add_time(.1)
    anim.get()
    anim.get()
    anim.get()
    anim.get()
    anim.get()
    anim.get()


if __name__=='__main__':
    from timeit import Timer
    t = Timer("test()", "from __main__ import test, setup; setup()")
    print min(t.repeat(1000, 1000))
