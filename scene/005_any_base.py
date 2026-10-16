from manim import *  # noqa: F403

from common import BaseSlide, chapter, digit_row


class AnyBase(BaseSlide):
    def construct(self):
        chapter(self, "Any base")
        reminder = MathTex(r"(\underbrace{1 1 \cdots 1}_{n})_2 = (2^n - 1)_{10}").scale(0.8).to_edge(UL)
        self.add(reminder)

        blank = digit_row(4, "?", base="b", side=1.5, dots_after=2).arrange(RIGHT, buff=0.45)
        biggest = digit_row(4, "b-1", base="b", font_size=34, side=1.5, dots_after=2).arrange(RIGHT, buff=0.45)
        self.play(Create(blank))
        self.next_slide()
        self.play(Transform(blank, biggest))

        cells = [biggest[1], biggest[2], biggest[4], biggest[5]]
        place_names = ["n-1", "n-2", "1", "0"]
        places = VGroup(*[MathTex(p).scale(0.8).next_to(c, UP) for p, c in zip(place_names, cells)])
        # each place is worth b^place times its digit; stacked on two lines so neighbours don't collide
        values = VGroup(*[
            VGroup(MathTex(f"b^{{{p}}}"), MathTex(r"\times (b-1)"))
            .arrange(DOWN, buff=0.12).scale(0.65).next_to(c, DOWN)
            for p, c in zip(place_names, cells)
        ])
        self.play(Write(places))
        self.play(Write(values))
        self.next_slide()

        long_sum = MathTex(
            "b^0", r"(b-1)", "+", "b^1", r"(b-1)", "+", r"\cdots", "+", "b^{n-1}", r"(b-1)"
        ).scale(1.1)
        for k in (1, 4, 9):
            long_sum[k].set_color(YELLOW)
        self.play(FadeOut(places, blank), ReplacementTransform(values, long_sum))
        self.next_slide()

        factored = MathTex(r"(b-1)", r"\big(b^0 + b^1 + \cdots + b^{n-1}\big)").scale(1.1)
        factored[0].set_color(YELLOW)
        self.play(TransformMatchingShapes(long_sum, factored))
        self.next_slide()

        series = MathTex(r"b^0 + b^1 + \cdots + b^{n-1}", "=", r"\frac{b^n - 1}{b - 1}").next_to(factored, DOWN, buff=0.8)
        self.play(Write(series))
        self.next_slide()

        substituted = MathTex(r"(b-1)", r"\times", r"\frac{b^n - 1}{b - 1}").scale(1.1)
        substituted[0].set_color(YELLOW)
        self.play(FadeOut(series), TransformMatchingShapes(factored, substituted))
        self.next_slide()

        result = MathTex(r"b^n - 1").scale(1.6)
        self.play(ReplacementTransform(substituted, result))
        self.next_slide()

        statement = MathTex(
            r"(\underbrace{(b-1) \cdots (b-1)}_{n})_b", "=", r"(b^n - 1)_{10}"
        ).scale(1.1)
        caption = Tex("the largest number $n$ digits can hold").scale(0.8).next_to(statement, DOWN, buff=0.6)
        self.play(TransformMatchingShapes(result, statement), FadeOut(reminder))
        self.play(Write(caption))
        self.next_slide(auto_next=True)
        self.play(FadeOut(*self.mobjects))
