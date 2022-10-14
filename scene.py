from turtle import circle
from manim import *

# create a circle with inner colored pink
class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen


# create a square and interpolate it into a circle
class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity = 0.5 )

        square = Square()
        square.rotate(PI / 4)  # rotate the square by Pi/4

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out the square


# using .animate method to interpolate a square into a circle
class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()  #create shapes first

        self.play(Create(square))  # display the creation of square
        self.play(square.animate.rotate(PI/4))  # rotate the square
        self.play(Transform(square, circle))  # interpolate the square into circle
        self.play(circle.animate.set_fill(PINK, opacity = 0.5))  # color the circle


# difference between .animate and rotate method
class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color = BLUE, fill_opacity = 0.7).shift(2 * LEFT)
        right_square = Square(color = GREEN, fill_opacity = 0.7).shift(2 * RIGHT)
        self.play(left_square.animate.rotate(PI/2), Rotate(right_square, angle = PI/2), run_time = 2)
        self.wait()



# create a square and circle next to each other
class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity = 0.5)

        square = Square()  # create a square
        square.set_fill(BLUE, opacity = 0.5)

        square.next_to(circle, UP, buff = 0.5)  # position square right to circle
        self.play(Create(circle), Create(square))  #display the shapes 


# add a static shape vs play an animation
class AnimateExample(Scene):
    def construct(self):
        square = Square().set_fill(RED, opacity = 1.0)
        self.add(square)  # this scene adds a square

        # following the square fadeout to white
        self.play(square.animate.set_fill(WHITE))
        self.wait()

        # following the square goes up and rotate
        self.play(square.animate.shift(UP).rotate(PI/3))
        self.wait()

# create a custom animation
"""class Count(Animation):
    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs) -> None:
        super().__init__(number, **kwargs)  # pass number as the mobject of animation
        self.start = start  # set start and end
        self.end = end

    def interpolate_mobject(self, alpha: float) -> None:
        value = self.start + (alpha * (self.end - self.start))
        self.mobject.set_value(value)  # 
"""

# display text in manim
class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello world", font_size = 144)
        self.add(text)

# display text in a particular font
class FontExample(Scene):
    def construct(self):
        ft = Text("Hello world", color = RED, font = "Noto Sans")
        self.add(ft)


# slant font
class SlantExample(Scene):
    def construct(self):
        text_a = Text("This a in font italic", slant = ITALIC)
        self.add(text_a)
        self.wait(2)

    def construct(self):
        text_b = Text("This a in font oblique", slant = OBLIQUE)
        self.add(text_b)
# up: add two texts seem to display only the last one?


# color gradient of text
class GradientExample(Scene):
    def construct(self):
        g_text = Text("Hello world", gradient = (RED, BLUE, GREEN), font_size = 96)
        self.add(g_text)

# test of LaTex
class HelloLaTex(Scene):
    def construct(self):
        l_text = Tex(r"number is $\frac{3}{5}$", font_size = 90)
        self.add(l_text)


# LaTex in manim, mathtex and tex
class LaTexExample(Scene):
    def construct(self):
        l_text1 = MathTex(r"number is \frac{3}{5}", font_size = 96)
        l_text2 = Tex(r"number is $\frac{3}{5}$", font_size = 90)

        self.add(VGroup(l_text1, l_text2), arrange(DOWN))


# example of a coordinate system
class AxesAndFunc(Scene):
    def construct(self):
        ax = Axes(x_range = (-5, 5), y_range = (-10, 10))
        q_func = ax.plot(lambda x: x**2-3*x-4, color = RED)
        q_area = ax.get_area(q_func, x_range = (-1, 0))
        self.play(Create(ax))
        self.play(Create(q_func))
        self.play(FadeIn(q_area))






