from manim import *  # noqa: F403

from common import BaseSlide, chapter, digit_row, gather


class LargestNumber(BaseSlide):
    def all_ones(self, count, value, scale):
        """( ? ? ? )_2 -> ( 1 1 1 )_2, with place values, summed up to their decimal value."""
        blank = digit_row(count, "?").scale(scale)
        ones = digit_row(count, "1").scale(scale)
        self.play(Create(blank))
        self.next_slide()
        self.play(Transform(blank, ones))

        cells = ones[1:-1]  # boxes only, most significant first
        places = VGroup(*[MathTex(str(count - 1 - i)).scale(0.8).next_to(c, UP) for i, c in enumerate(cells)])
        powers = [MathTex(f"2^{count - 1 - i}").scale(0.8).next_to(c, DOWN) for i, c in enumerate(cells)]
        self.play(Write(places))
        self.play(*[Write(p) for p in powers])
        self.next_slide()

        terms = []
        for k in range(count):
            terms += [f"2^{k}", "+"]
        total = MathTex("= (", *terms[:-1], r")_{10}").scale(scale).next_to(ones, DOWN, buff=1.0)
        # powers are listed most significant first; the sum starts at 2^0
        self.play(FadeOut(places), gather(powers[::-1], total, [1 + 2 * k for k in range(count)]))
        self.next_slide()

        result = MathTex("= (", str(value), r")_{10}").scale(scale * 1.3).next_to(ones, RIGHT)
        self.play(ReplacementTransform(total, result))
        self.play(VGroup(blank, result).animate.move_to(ORIGIN))
        self.next_slide()
        self.play(FadeOut(blank, result))

    def construct(self):
        chapter(self, "The largest number")

        self.all_ones(3, 7, 1.5)
        self.all_ones(4, 15, 1.3)

        # n ones
        blank = digit_row(4, "?", dots_after=2).scale(1.3)
        ones = digit_row(4, "1", dots_after=2).scale(1.3)
        self.play(Create(blank))
        self.next_slide()
        self.play(Transform(blank, ones))

        cells = [ones[1], ones[2], ones[4], ones[5]]
        place_names = ["n-1", "n-2", "1", "0"]
        places = VGroup(*[MathTex(p).scale(0.7).next_to(c, UP) for p, c in zip(place_names, cells)])
        powers = [MathTex(f"2^{{{p}}}").scale(0.7).next_to(c, DOWN) for p, c in zip(place_names, cells)]
        brace = Brace(VGroup(*cells), UP, buff=0.7)
        n_label = MathTex("n").next_to(brace, UP)
        self.play(Write(places))
        self.play(*[Write(p) for p in powers])
        self.play(GrowFromCenter(brace), Write(n_label))
        self.next_slide()

        total = MathTex(
            "= (", "2^0", "+", "2^1", "+", r"\cdots", "+", "2^{n-2}", "+", "2^{n-1}", r")_{10}"
        ).scale(1.3).next_to(ones, DOWN, buff=1.0)
        self.play(FadeOut(places), gather(powers[::-1], total, [1, 3, 7, 9]))
        self.next_slide()

        result = MathTex("= (", "2^n - 1", r")_{10}").scale(1.6).next_to(ones, RIGHT)
        self.play(ReplacementTransform(total, result))
        self.play(VGroup(blank, result, brace, n_label).animate.move_to(ORIGIN))
        self.next_slide(auto_next=True)

        # carry this forward as a reminder
        summary = MathTex(r"(\underbrace{1 1 \cdots 1}_{n})_2 = (2^n - 1)_{10}").scale(0.8).to_edge(UL)
        self.play(ReplacementTransform(VGroup(blank, result, brace, n_label), summary))
