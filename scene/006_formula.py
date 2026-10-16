from manim import *  # noqa: F403

from common import BaseSlide, chapter


class Formula(BaseSlide):
    def construct(self):
        chapter(self, "The formula")
        largest = MathTex(r"\text{largest with } n \text{ digits} = b^n - 1").scale(0.8).to_edge(UL)
        self.add(largest)

        steps = [
            (r"N \le b^n - 1", r"\text{$N$ has to fit in $n$ digits}"),
            (r"N + 1 \le b^n", ""),
            (r"\log_b (N + 1) \le \log_b b^n", r"\text{take } \log_b \text{ of both sides}"),
            (r"\log_b (N + 1) \le n", ""),
        ]
        shown = VGroup()
        for tex, note in steps:
            line = MathTex(tex).scale(1.2)
            if shown:
                line.next_to(shown, DOWN, buff=0.45).align_to(shown, LEFT)
            else:
                line.shift(1.8 * UP + 1.5 * LEFT)
            group = VGroup(line)
            if note:
                group.add(MathTex(note).scale(0.7).set_opacity(0.7).next_to(line, RIGHT, buff=0.6))
            self.play(Write(group))
            shown.add(group)
            self.next_slide()

        smallest = Tex("the smallest such $n$:").scale(0.9)
        formula = MathTex(r"n = \lceil \log_b (N + 1) \rceil").scale(2)
        VGroup(smallest, formula).arrange(DOWN, buff=0.5)
        self.play(FadeOut(shown), Write(smallest), Write(formula))
        box = SurroundingRectangle(formula, color=YELLOW, buff=0.3)
        self.play(Create(box))
        self.next_slide()

        formula_small = VGroup(formula, box)
        self.play(FadeOut(smallest, largest), formula_small.animate.scale(0.45).to_edge(UL))

        examples = VGroup(
            MathTex(r"(26)_{10} = (222)_3", r"\qquad \lceil \log_3 27 \rceil = 3"),
            MathTex(r"(27)_{10} = (1000)_3", r"\qquad \lceil \log_3 28 \rceil = 4"),
        ).scale(1.2).arrange(DOWN, buff=0.8)
        for example in examples:
            self.play(Write(example[0]))
            self.play(TransformFromCopy(formula, example[1]))
            self.next_slide(auto_next=example is examples[-1])
        self.play(FadeOut(*self.mobjects))
