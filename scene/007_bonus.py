from manim import *  # noqa: F403

from common import BaseSlide, chapter


class Bonus(BaseSlide):
    def construct(self):
        bonus = Tex("Bonus!", font_size=112)
        self.play(Write(bonus))
        self.next_slide()

        chapter(self, "Bonus")
        identity = MathTex(r"\lceil \log_b (N + 1) \rceil", "=", r"\lfloor \log_b N \rfloor + 1").scale(1.6)
        self.play(FadeOut(bonus), Write(identity))
        self.next_slide()

        # why: N sits between two powers of b
        self.play(identity.animate.scale(0.6).to_edge(UP, buff=1.2))
        lines = VGroup(
            MathTex(r"b^k \le N < b^{k+1}", r"\quad \Rightarrow \quad", r"\lfloor \log_b N \rfloor = k"),
            MathTex(r"b^k < N + 1 \le b^{k+1}", r"\quad \Rightarrow \quad", r"\lceil \log_b (N + 1) \rceil = k + 1"),
        ).arrange(DOWN, buff=0.7, aligned_edge=LEFT).shift(0.3 * DOWN)
        for line in lines:
            self.play(Write(line))
            self.next_slide()

        self.play(Indicate(identity, color=YELLOW))
        self.next_slide(auto_next=True)
        self.play(FadeOut(*self.mobjects))
