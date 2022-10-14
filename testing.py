from manim import *
from cmath import cos, sin
from re import X

# used for testing small chunks of code

# Position: P1M3, definition of addition, point moving to right

class MoveAlongPathExample(Scene):
    def construct(self):
        d1 = Dot((-2, 0, 0), radius=0.05).set_color(ORANGE)
        d2 = Dot(radius=0.05).set_color(BLUE)
        l1a = Line(2 * LEFT, ORIGIN)
        l1b = Line(ORIGIN, 2.5 * RIGHT)
        v1a = VMobject()
        v1b = VMobject()

        
        self.add(d1, d2, l1a, l1b, v1a, v1b)
        v1a.add_updater(lambda x: x.become(Line(2 * LEFT, d1.get_center()).set_color(ORANGE)))
        v1b.add_updater(lambda y: y.become(Line(ORIGIN, d2.get_center()).set_color(BLUE)))
        self.play(MoveAlongPath(d1, l1a), rate_func=linear, run_time = 0.5)
        self.wait()
        self.play(MoveAlongPath(d2, l1b), rate_func=linear, run_time = 0.5)


# Begin another test
