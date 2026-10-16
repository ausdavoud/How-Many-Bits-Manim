from manim import *  # noqa: F403

from common import BaseSlide, chapter

GUESS = [r"\lceil", r"\log", r"_b N", r"\rceil", "=", "n"]

# x position, N, base, N written in that base, digits it needs, what the guess says
CASES = [
    (-4.6, "2", "2", "10", 2, 1),
    (0.0, "8", "2", "1000", 4, 3),
    (4.6, "81", "3", "10000", 5, 4),
]


class WhereItFails(BaseSlide):
    def construct(self):
        chapter(self, "Where it fails")
        guess = MathTex(*GUESS).to_edge(UL)
        self.add(guess)

        shown = VGroup()
        for i, (x, number, base, digits, n, says) in enumerate(CASES):
            # written above the columns, so it never lands on top of earlier cases
            written = MathTex(
                rf"({number})_{{10}} = (\underbrace{{{digits}}}_{{n = {n}}})_{{{base}}}"
            ).scale(1.3).move_to([0, 2.1, 0])
            self.play(Write(written))
            self.next_slide()

            needed = MathTex(rf"n = {n}").move_to([x, -0.9, 0])
            formula = MathTex(rf"\lceil \log_{{{base}}} {number} \rceil = {says}").move_to([x, 0.3, 0])
            box = SurroundingRectangle(formula, color=RED, buff=0.25)
            self.play(ReplacementTransform(written, needed), TransformFromCopy(guess, formula))
            self.play(Create(box))
            shown.add(needed, formula, box)
            if i < len(CASES) - 1:
                divider = Line([x + 2.3, 1.1, 0], [x + 2.3, -1.4, 0], stroke_opacity=0.4)
                self.play(Create(divider))
                shown.add(divider)
            self.next_slide()

        # what the failures have in common
        powers = VGroup(*[
            MathTex(p).scale(0.9).next_to(shown[k], DOWN, buff=0.45)
            for p, k in ((r"2 = 2^1", 0), (r"8 = 2^3", 4), (r"81 = 3^4", 8))
        ])
        self.play(Write(powers))
        self.next_slide()

        pattern = MathTex(r"N = b^q", r"\Rightarrow", r"\lceil \log_b N \rceil", r"+ 1").scale(1.6)
        self.play(FadeOut(shown, powers), ReplacementTransform(guess, pattern))
        self.next_slide()
        self.play(FadeOut(pattern))

        questions = VGroup(
            Tex(r"1. Why does it fail when $N = b^q$?"),
            Tex("2. What's the correct formula?"),
            Tex(r"3. Why $\log$?"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        for q in questions:
            self.play(Write(q))
        self.next_slide(auto_next=True)
        self.play(FadeOut(*self.mobjects))
