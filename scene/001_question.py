from manim import *  # noqa: F403

from common import BaseSlide


class Question(BaseSlide):
    def construct(self):
        title = Tex("How many bits?", font_size=112)
        self.play(Write(title))
        self.next_slide()

        decimal = MathTex(r"(N)_{10}").scale(2)
        self.play(ReplacementTransform(title, decimal))
        self.next_slide()

        unknown = MathTex(r"(N)_{10}", "= (", "?", ")_2").scale(2)
        self.play(TransformMatchingTex(decimal, unknown))
        self.next_slide()

        boxes = MathTex(r"(N)_{10}", "= (", r"\square \square \cdots \square", ")_2").scale(2)
        self.play(TransformMatchingTex(unknown, boxes))
        brace = Brace(boxes[2])
        n = MathTex(r"n = \ ?").next_to(brace, DOWN)
        self.play(Write(brace))
        self.play(Write(n), run_time=0.5)
        self.next_slide()
        self.play(FadeOut(*self.mobjects))

        # an easy one first
        seven = MathTex(r"(7)_{10}").scale(2)
        self.play(Write(seven))
        self.next_slide()

        seven_binary = MathTex(r"(7)_{10}", "= (", "111", ")_2").scale(2)
        self.play(TransformMatchingTex(seven, seven_binary))
        self.next_slide()

        brace = Brace(seven_binary[2])
        n = MathTex("n = 3").next_to(brace, DOWN)
        self.play(Write(brace))
        self.play(Write(n), run_time=0.5)
        self.next_slide(auto_next=True)
        self.play(FadeOut(*self.mobjects))
