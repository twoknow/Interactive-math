from cmath import cos, sin
from re import X
from manim import *


'''06-07-2022, happen to know it is 宇轩's birthday, so create a video'''

# happy birthday
class Mike(Scene):
    def construct(self):
        m_name = Text("Happy birthday, Mike!", color = RED)
        self.play(Create(m_name.shift(UP*2.5)))
        self.wait()

        ax = Axes(x_range = (-5,5), y_range = (-5,5))
        fig1 = ax.plot(lambda x: (x-2)*(x+2), x_range = (-2, 2), color = ORANGE)
        fig2 = ax.plot(lambda x: 0.5*(x-2)*(x+2), x_range = (-2, 2), color = ORANGE)

        cir1 = Circle(radius = 0.5, color = BLUE)
        cir2 = Circle(radius = 0.5, color = BLUE)
        self.play(Create(fig1), Create(fig2))
        self.play(Create(cir1.shift(UP + LEFT)), Create(cir2.shift(UP + RIGHT)))




'''4th day of Manim learning, keep going. 07-07-2022'''

class Positioning(Scene):
    def construct(self):
        lattice = NumberPlane()
        self.add(lattice)

        # next_to method
        red_dot = Dot(color = RED)
        green_dot = Dot(color = GREEN)
        green_dot.next_to(red_dot, RIGHT)
        self.add(red_dot, green_dot)

        # shift method
        square = Square(color = ORANGE)
        square.shift(2*UP + 3*RIGHT)
        self.add(square)

        # move_to method
        circle = Circle(color = YELLOW)
        circle.move_to([-2, -3, 0])
        self.add(circle)

        # align_to method
        c2 = Circle(radius = 0.5, fill_opacity = 0.5, color = WHITE)
        c3 = c2.copy().set_color(BLUE)
        c4 = c2.copy().set_color(GREEN)
        c3.align_to(square, UP)
        c4.align_to(square, RIGHT)
        self.add(c2, c3, c4)


# text and tex in manim
class LatexExample(Scene):
    def construct(self):
        tex1 = Tex(r'\LaTex', font_size = 96)
        self.add(tex1)
# failed, still checking
# 
# 
# another birthday, 伯鑫

class Boxin(Scene):
    def construct(self):
        m_name = Text("Happy birthday to you", color = RED)
        name1= Text("Happy birthday, 伯鑫")
        text1 = Text("让我们做个简单的数学题: " ).shift(UP*2)
        text2 = Text("答案是：e, = Excellence!")
        text3 = Text("这就是伯鑫")

        ax = Axes(x_range = (-5, 5), y_range = (-3, 3))
        f1 = ax.plot(lambda x: 0.45*(x-2)*(x+2), x_range = (-2, 2))
        a1 = ax.get_area(f1, x_range = (-2, 2), color = ORANGE)

        c1 = Circle(radius = 0.4, color = YELLOW)
        c2 = Circle(radius = 0.4, color = YELLOW)

        expre = Tex(r"$\lim_{n \to \infty} (1 + \frac{1}{n})^{n} = ?$", font_size = 96)
        
        self.play(Create(m_name.shift(UP)))
        self.wait()
        self.play(Create(m_name.shift(DOWN)))
        self.wait()
        self.play(Create(name1.shift(UP)))
        self.wait()
        self.play(Create(m_name.shift(DOWN)))
        self.wait()
        self.play(FadeOut(m_name), FadeOut(name1))

        # self.play (FadeIn(a1))
        # self.play(Indicate(c1.shift(LEFT + UP*2)), Indicate(c2.shift(RIGHT + UP*2)))

        self.add(text1)
        self.play(Create(expre), run_time = 3)

        self.play(FadeOut(text1), FadeOut(expre))
        self.wait()
        self.play(Create(text2))
        self.wait()
        self.play(FadeOut(text2))
        self.play(Create(text3))
        self.wait()


        

from manim import *

from manim import *

from manim import *

class PointWithTrace(Scene):
    def construct(self):
        path = VMobject()
        dot = Dot()
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)
        self.add(path, dot)
        self.play(Rotating(dot, radians=PI, about_point=RIGHT, run_time=2))
        self.play(dot.animate.shift(UP))
        self.play(dot.animate.shift(LEFT))
        self.wait()

# test of LaTex, successful!
class T(Scene):
    def construct(self):
        expre = Tex(r"$\lim_{n \to \infty} (1 + \frac{1}{n})^n$", font_size = 96)
        self.add(expre)


# try an example given in Manim Community
from manim import *

class AddPackageLatex(Scene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        tex = Tex(
            r"$\mathscr{H} \rightarrow \mathbb{H}$}",
            tex_template=myTemplate,
            font_size=144,
        )
        self.add(tex)
# failed, do not know why

# use of scale
class BigSmall(Scene):
    def construct(self):
        tri = Triangle(color = RED).scale(2.5)
        s = Square(color = YELLOW)

        self.play(DrawBorderThenFill(tri))
        self.play(s.animate.move_to([4, 0, 0]))


# how ArcBetweenPoints work
from manim import *

class ArcBetweenPointsExample(Scene):
    def construct(self):
        circle = Circle(radius=1, stroke_color=GREY)
        dot_1 = Dot(color=GREEN).move_to([2, 0, 0]).scale(0.5)
        dot_1_text = Tex("(2,0)").scale(0.5).next_to(dot_1, RIGHT).set_color(BLUE)
        dot_2 = Dot(color=GREEN).move_to([0, 2, 0]).scale(0.5)
        dot_2_text = Tex("(0,2)").scale(0.5).next_to(dot_2, UP).set_color(BLUE)
        dot_3 = Dot(color=GREEN).move_to([-2, 0, 0]).scale(0.5)
        dot_3_text = Tex("(?,?)").scale(0.5).next_to(dot_3, LEFT).set_color(YELLOW)
        
        arc= ArcBetweenPoints(start=[2, 0, 0], end=2 * LEFT, stroke_color=YELLOW, radius = 2)
        self.add(circle, dot_1, dot_2, dot_3, dot_1_text, dot_2_text, dot_3_text)
        self.play(Create(arc))
        self.wait()


# circle surround method
class CircleSurround(Scene):
    def construct(self):
        tri = Triangle()
        cir = Circle().surround(tri)

        self.add(tri, cir)


# another try of tex using mathtex
class Mtex(Scene):
    def construct(self):
        text1 = MathTex(r"\binom{n}{2}")
        text2 = MathTex(r"(a+b)^2 &= (a+b) \times (a+b)\\ &= a^2 +2ab +b^2")
        self.add(text2)


# arrangement of figures
class Grouping(Scene):
    def construct(self):
        red_dot = Dot(color=RED)
        blue_dot = Dot(color=BLUE).next_to(red_dot, UP)
        dot_group = VGroup(red_dot, blue_dot)

        stars = VGroup(*[Star(color = YELLOW, fill_opacity = 0) for _ in range(10)])
        
        self.add(dot_group, stars)


# config
config.background_color = BLACK
config.frame_width = 16  #this is the typical setting, like a rectangle
config.frame_height = 9  #these two can be changed into other 'shapes'

class Any(Scene):
    def construct(self):
        cir = Circle(color=RED)
        self.add(cir)


# local config
class Another(Scene):
    def construct(self):
        Text.set_default(color = RED, font_size = 96)  #config here all the texts
        text1 = Text("Math is beautiful")

        self.add(text1)


# now comes the polygon
class Polyg(Scene):
    def construct(self):
        polygs = VGroup(
            *[RegularPolygon(6, radius = 1) for _ in range(5)]
        ).arrange(RIGHT)
        self.play(DrawBorderThenFill(polygs))


# animations can be grouped as well, using lag_ratio
class SuccessiveAnim(Scene):
    def construct(self):
        cirs = VGroup(
            *[Circle(radius = 1, color = RED) for i in range(12)]
            ).arrange_in_grid(4, 3)
        self.play(AnimationGroup(*[FadeIn(c) for c in cirs], lag_ratio= 0.5))


# combinations of animations
class Anim(Scene):
    def construct(self):
        cir1 = Circle(color=RED)
        squ1 = Square(color=BLUE)
        fgroup = VGroup(cir1, squ1)

        self.add(cir1, squ1)
        self.play(cir1.animate.shift(DOWN), squ1.animate.shift(UP))
        self.wait()
        self.play(fgroup.animate.arrange(DOWN))
        self.play(cir1.animate.scale(3))
        

# make a copy and modify + restore the initial mobject
class MovetoTarget(Scene):
    def construct(self):
        c = Circle(color=RED)
        r = Rectangle(color=YELLOW)
        r.save_state()

        c.generate_target().scale(0.5).shift(UP+RIGHT)
        self.play(MoveToTarget(c))

        self.play(r.animate.shift(DOWN))
        self.play(Restore(r))


# try an example in Manimgl
# from manimlib import *

class SquareToCircle1(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)
        square = Square()

        self.play(ShowCreation(square)) # ShowCreation is equivalent to Create
        self.wait()
        self.play(ReplacementTransform(square, circle))
        self.wait()

# Now try to set up a custom animation that count from start to end
class Count(Animation):
    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs) -> None:
        # Pass number as the mobject of the animation
        super().__init__(number,  **kwargs)
        # Set start and end
        self.start = start
        self.end = end

    def interpolate_mobject(self, alpha: float) -> None:
        # Set value of DecimalNumber according to alpha
        value = self.start + (alpha * (self.end - self.start))
        self.mobject.set_value(value)


class CountingScene(Scene):
    def construct(self):
        # Create Decimal Number and add it to scene
        number = DecimalNumber(10).set_color(WHITE).scale(5)
        # Add an updater to keep the DecimalNumber centered as its value changes
        number.add_updater(lambda number: number.move_to(ORIGIN))

        self.add(number)
        self.wait()

        # Play the Count Animation to count from 10 to 100 in 3 seconds
        self.play(Count(number, 10, 100), run_time=3, rate_func=linear)

        self.wait()


'''Now comes the real course: OPERATIONS'''
# Let's go!
# Document is stored in OVERLEAF

# About naming rules:
# 0. The modules we are in be explictly named.
# 1. Subtitles are named with "t"+"m_{n}"+"s_{n}" where "t" stands for "subtitle",
# "m_{n}" and "s_{n}" denote the n-th module and sentence in that module, respectively.
# 2. Words and LaTex formulae in the scene are named with "text"+"m_{n}"+"s_{n}" and 
# "math"+"m_{n}"+"s_{n}", respectively.


# Scene 1: P1
class P1(Scene):
    def construct(self):
    # begin the 1st section M1
        tm1s1 = Text("加减乘除是我们对数学的基本认识", font_size=30)
        tm1s2 = Text("但事实上，运算律才是幕后的大 BOSS", font_size=30).shift(DOWN * 4)
        # tm1s3 = Text("", font_size=30)
        tm1s4 = Text("我们不妨从最简单的加法开始说起", font_size=30).shift(DOWN * 4)

        # Below are for the 1st sentence tm1s1：加减乘除是基本认识
        mathm1s1a = Tex(r'$+$', font_size = 48)
        mathm1s1b = Tex(r'$-$', font_size = 48)
        mathm1s1c = Tex(r'$\times$', font_size = 48)
        mathm1s1d = Tex(r'$\div$', font_size = 48)
        m1group1 = VGroup(mathm1s1a, mathm1s1b, mathm1s1c, mathm1s1d)

        # Below are for the 2nd sentence tm1s2：运算律才是背后的大BOSS
        mathm1s2a = Tex(r'$4 + 5 = 5 + 4 $')
        textm1s2a = Text("交换律：", font_size=30)
        mathm1s2b = Tex(r'$(3 + 4) + 6 = 3 + (4 + 6)$')
        textm1s2b = Text("结合律：", font_size=30)
        
        m1group2a = VGroup(textm1s2a, mathm1s2a).arrange(RIGHT)
        m1group2b = VGroup(textm1s2b, mathm1s2b).arrange(RIGHT)
        m1group2 = VGroup(m1group2a, m1group2b).arrange(DOWN) 
        
        # Below are for the 3rd sentence tm1s3：不妨从最简单的加法说起
        mathm1s3 = Tex(r'$13+39+91$')
        textm1s3 = Text("计算：", font_size=30)
        m1group3 = VGroup(textm1s3, mathm1s3).arrange(RIGHT)

        # Below are for the 4th sentence tm1s4: 就用到了结合律
        mathm1s4 = MathTex(r'13 +(39 + 91) = (13 + 39) + 91')
        textm1s4 = Text("结合律：", font_size= 30)
        m1group4 = VGroup(textm1s4, mathm1s4).arrange(RIGHT)

        # BEGIN ANIMATING
        self.play(m1group1.animate.arrange(RIGHT), tm1s1.animate.shift(DOWN * 4), run_time = 3)
        self.play(FadeOut(tm1s1))
        self.play(ReplacementTransform(m1group1, m1group2), Create(tm1s2), run_time = 3)
        self.play(FadeOut(tm1s2))
        self.play(Create(tm1s4), ReplacementTransform(m1group2, m1group3), run_time = 2)
        self.play(FadeOut(tm1s4))

    # begin the 2nd section M2
        self.next_section()
        tm2s1 = Text("假设要快速计算 13+39+91", font_size=30).shift(DOWN * 4)
        tm2s2 = Text("简便的做法是先算 39+91, 得到 130", font_size=30).shift(DOWN * 4)
        tm2s3 = Text("然后再和 13 相加, 最终得 143", font_size=30).shift(DOWN * 4)
        tm2s4 = Text("这里先加 39 和 91 ", font_size=30).shift(DOWN * 4)
        tm2s5 = Text("就用到了加法结合律", font_size=30).shift(DOWN * 4)

        mathm2s1 = MathTex(r'13 + 39 + 91 & = 13 + (39 + 91) \\ & = 13 + 130')
        mathm2s2 = MathTex(r'13 + 39 + 91 & = 13 + (39 + 91) \\ & = 13 + 130 \\ &= 143')
        mathm2s3 = MathTex(r'(39 +91)')

        self.play(Create(tm2s1), run_time = 3)
        self.play(FadeOut(tm2s1), FadeOut(m1group3))
        self.play(Write(tm2s2), Write(mathm2s1), run_time = 4)
        self.play(FadeOut(tm2s2))
        self.play(Write(tm2s3), ReplacementTransform(mathm2s1,mathm2s2), run_time = 3)
        self.play(FadeOut(tm2s3), FadeOut(mathm2s2))
        self.play(Write(tm2s4), Indicate(mathm2s3), run_time = 1.5)
        self.play(FadeOut(tm2s4))
        self.play(Write(tm2s5), ReplacementTransform(mathm2s3, mathm1s4), run_time = 3)
        self.play(FadeOut(tm2s5), FadeOut(mathm1s4))
        self.wait()

    # begin the 3rd section of P1
        self.next_section()
        planem3 = NumberPlane((-8, 12),(-5,5))
        d1 = Dot((-2, 0, 0), radius=0.05).set_color(ORANGE)
        d2 = Dot(radius=0.05).set_color(BLUE)
        l1a = Line(2 * LEFT, ORIGIN)
        l1b = Line(ORIGIN, 2.5 * RIGHT)
        v1a = VMobject()
        v1b = VMobject()
        v1a.add_updater(lambda x: x.become(Line(2 * LEFT, d1.get_center()).set_color(ORANGE)))
        v1b.add_updater(lambda y: y.become(Line(ORIGIN, d2.get_center()).set_color(BLUE)))


        tm3s1 = Text("我们回到数轴来看加法, a + b 就是：", font_size = 30).shift(DOWN * 4)
        tm3s2 = Text("从原点出发先向右走 a 单位，再向右走 b 单位", font_size = 30).shift(DOWN * 4)
        tm3s3 = Text("此时交换律 4 + 5 = 5 + 4 就是", font_size = 30).shift(DOWN * 4)
        tm3s4 = Text("先向右走 4 单位再接着走 5 单位", font_size = 30).shift(DOWN * 4)
        tm3s5 = Text("和先向右走 5 单位再接着走 4 单位", font_size = 30).shift(DOWN * 4)
        tm3s6 = Text("二者都可以到达同样的终点 9", font_size=30).shift(DOWN * 4)
        mathm3s1 = Tex(r"$4 + 5 \overset{!}{=} 5 + 4$", color = YELLOW).shift(0.5 * UP)

        # these are for 4+5
        d1 = Dot((-2, 0, 0), radius=0.1).set_color(ORANGE)
        d2 = Dot(radius=0.1).set_color(BLUE)
        l1a = Line(2 * LEFT, ORIGIN)
        l1b = Line(ORIGIN, 2.5 * RIGHT)
        v1a = VMobject()
        v1b = VMobject()

        # below are for 5+4
        l2a = Line(2 * LEFT, 0.5 * RIGHT)
        l2b = Line(0.5 * RIGHT, 2.5 * RIGHT)
        l2c = Line(2 * LEFT, 2.5 * RIGHT)
        v2a = VMobject()
        v2b = VMobject()
        v2c = VMobject()


        brace1 = Brace(l1a, UP, color = ORANGE)
        brace2 = Brace(l1b, UP, color = BLUE)
        label1 = Text("a").next_to(brace1, UP)
        label2 = Text("b").next_to(brace2, UP)
        label3 = Text("4", color=YELLOW).next_to(ORIGIN, UP)
        label4 = Text("9", color=YELLOW).next_to((2.5, 0, 0), UP)
        label5 = Text("5", color=YELLOW).next_to(0.5 * RIGHT, UP)

        self.add(planem3, d1, d2, l1a, l1b, v1a, v1b, brace1, brace2, label1, label2)
        v1a.add_updater(lambda x: x.become(Line(2 * LEFT, d1.get_center()).set_color(ORANGE)))
        v1b.add_updater(lambda y: y.become(Line(ORIGIN, d2.get_center()).set_color(BLUE)))
        v2a.add_updater(lambda m: m.become(Line(2 * LEFT, d1.get_center()).set_color(ORANGE)))
        v2b.add_updater(lambda n: n.become(Line(0.5 * RIGHT, d2.get_center()).set_color(BLUE)))
        v2c.add_updater(lambda t: t.become(Line(2 * LEFT, d1.get_center()).set_color(YELLOW)))

        self.play(Write(tm3s1), run_time = 4)  # 从原点出发
        self.play(FadeOut(tm3s1))
        self.play(Write(tm3s2), run_time = 2.5)  # 先向右走，再接着走
        self.play(MoveAlongPath(d1, l1a), rate_func=linear, run_time = 0.5)
        self.wait(0.5)
        self.play(MoveAlongPath(d2, l1b), rate_func=linear, run_time = 0.5)
        self.play(FadeOut(tm3s2))
        self.remove(d1, d2, l1a, l1b, v1a, v1b, brace1, brace2, label1, label2)
        self.wait()

        self.play(Write(tm3s3), Write(mathm3s1), run_time = 3) # 交换律 4+5=5+4 就是
        self.play(mathm3s1.animate.shift(UP * 1.5), FadeOut(tm3s3))
        self.play(Write(tm3s4), run_time = 2) # 先向右走 4 单位再接着走 5 单位
        self.play(MoveAlongPath(d1, l1a), rate_func=linear, run_time = 0.5)
        self.add(label3)
        self.wait(0.5)
        self.play(MoveAlongPath(d2, l1b), rate_func=linear, run_time = 0.5)
        self.add(label4)
        self.play(FadeOut(tm3s4))
        self.remove(label3, label4, v1a, v1b, d1, d2)
         
        self.play(Write(tm3s5), run_time = 2)  # 和先向右走 5 单位再向右走 4 单位
        self.play(MoveAlongPath(d1, l2a), rate_func=linear, run_time = 0.5)
        self.add(label5)
        self.wait(0.5)
        self.play(MoveAlongPath(d2, l2b), rate_func=linear, run_time = 0.5)
        self.add(label4)
        self.play(FadeOut(tm3s5))
        self.remove(label5, label4, v2a, v2b, d1, d2)
        self.wait(0.5)

        self.play(Write(tm3s6), run_time = 1.5)
        self.play(MoveAlongPath(d1, l2c), rate_func=linear, run_time = 1)
        self.play(Indicate(label4))
        self.remove(label4)
        self.wait()

        # begin talking about associative law
       

        





        




        


