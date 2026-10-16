from manim import *  # noqa: F403

from common import BaseSlide, chapter

GUESS = [r"\lceil", r"\log", r"_b N", r"\rceil", "=", "n"]


class FirstGuess(BaseSlide):
    def construct(self):
        chapter(self, "A first guess")

        log = MathTex(r"\log", r"_b N = n").scale(2.5).shift(0.5 * UP)
        line = Line(log.get_left(), log.get_right()).next_to(log, DOWN)
        legend = MathTex(
            r"N &\rightarrow \text{decimal number}\\"
            r"b &\rightarrow \text{target base}\\"
            r"n &\rightarrow \text{digits needed}",
            font_size=36,
        ).next_to(line, DOWN, buff=0.5).shift(1.5 * LEFT)
        conditions = MathTex(r"N &\ge 1 \\ b &\ge 2", font_size=56).next_to(legend, RIGHT, buff=1.5)

        self.play(Write(log))
        self.next_slide()
        self.play(Create(line), Write(legend))
        self.next_slide()
        self.play(Write(conditions))
        self.next_slide()
        self.play(log.animate.scale(0.5).to_edge(UL), FadeOut(line, legend, conditions))

        # try it on 13
        thirteen = MathTex("(", "13", ")_{", "10", "}").scale(2)
        thirteen_digits = MathTex(
            "(", "13", ")_{", "10", "}", r"= \Big(",
            r"\underbrace{\overset{\scriptscriptstyle n-1}{\square} \cdots "
            r"\overset{\scriptscriptstyle 1}{\square}\, \overset{\scriptscriptstyle 0}{\square}}_{n}",
            r"\Big)_", "2",
        ).scale(1.8)
        self.play(Write(thirteen))
        self.next_slide()
        self.play(TransformMatchingTex(thirteen, thirteen_digits))
        self.next_slide()

        log13 = MathTex(r"\log", "_2", "13", r"=\, ?").scale(2)
        self.play(
            ReplacementTransform(thirteen_digits[1], log13[2]),
            FadeOut(VGroup(*thirteen_digits[:1], *thirteen_digits[2:])),
            TransformFromCopy(log[0], log13[0]),
            FadeIn(log13[1], log13[3]),
        )
        self.next_slide()

        bounds = MathTex(r"\log_2 8", "<", r"\log", "_2", "13", "<", r"\log_2 16").scale(2)
        self.play(TransformMatchingTex(log13, bounds))
        self.next_slide()

        bounds_values = MathTex(
            "3", "=", r"\log_2 8", "<", r"\log", "_2", "13", "<", r"\log_2 16", "=", "4"
        ).scale(1.5)
        self.play(TransformMatchingTex(bounds, bounds_values))
        self.next_slide()

        between = MathTex("3", "<", r"\log", "_2", "13", "<", "4").scale(2)
        self.play(TransformMatchingTex(bounds_values, between))
        self.next_slide()

        approx = MathTex(r"\log", "_2", "13", r"\approx 3.7").scale(2)
        self.play(TransformMatchingTex(between, approx))
        self.next_slide()

        # 3.7 bits? a bit is all or nothing
        self.play(approx.animate.scale(0.75).shift(2 * UP))
        cells = VGroup(*[Square(1) for _ in range(4)]).arrange(RIGHT, buff=0.2).shift(0.5 * DOWN)

        def fill(cell, fraction=1.0):
            return (
                Rectangle(width=fraction, height=1, stroke_width=0, fill_color=YELLOW, fill_opacity=0.5)
                .align_to(cell, LEFT)
                .align_to(cell, UP)
            )

        full = VGroup(*[fill(c) for c in cells[:3]])
        partial = fill(cells[3], 0.7)
        label = Tex("3.7 bits?").next_to(cells, DOWN, buff=0.4)
        self.play(Create(cells))
        self.play(LaggedStart(*[FadeIn(f) for f in full], lag_ratio=0.3), FadeIn(partial), Write(label))
        self.next_slide()

        label_4 = Tex("4 bits").move_to(label)
        self.play(Transform(partial, fill(cells[3])), Transform(label, label_4))
        self.next_slide()

        ceil = MathTex(r"\lceil", r"\log", "_2", "13", r"\rceil", "=", "4").scale(1.5).move_to(approx)
        self.play(TransformMatchingTex(approx, ceil))
        self.next_slide()

        # check: 13 = (1101)_2
        digits = VGroup(*[MathTex(d).scale(1.5).move_to(c) for d, c in zip("1101", cells)])
        weights = VGroup(*[MathTex(str(w)).next_to(c, DOWN) for w, c in zip((8, 4, 2, 1), cells)])
        self.play(FadeOut(full, partial, label), Write(digits))
        self.play(Write(weights))
        self.next_slide()

        total = MathTex("8 + 4 + 1 = 13").next_to(weights, DOWN, buff=0.5)
        self.play(weights[2].animate.set_opacity(0.25), digits[2].animate.set_opacity(0.4), Write(total))
        self.next_slide()

        guess = MathTex(*GUESS).scale(2)
        self.play(FadeOut(cells, digits, weights, total, log), TransformMatchingTex(ceil, guess))
        self.next_slide(auto_next=True)
        self.play(guess.animate.scale(0.5).to_edge(UL))
