from manim import *  # noqa: F403

from common import BaseSlide, chapter


class Answers(BaseSlide):
    def qa(self, question, *answer_lines):
        q = Tex(question, color=YELLOW).scale(1.1)
        def typeset(line):
            # a line that is one formula on its own is set as display math, everything else as text
            if line.startswith("$") and line.endswith("$") and line.count("$") == 2:
                return MathTex(line[1:-1])
            return Tex(line)

        answer = VGroup(*[typeset(line).scale(0.95) for line in answer_lines]).arrange(DOWN, buff=0.35)
        VGroup(q, answer).arrange(DOWN, buff=0.7)
        self.play(Write(q))
        self.play(Write(answer))
        self.next_slide()
        self.play(FadeOut(q, answer))

    def construct(self):
        chapter(self, "Answers")

        self.qa(
            r"1. Why did the guess fail when $N = b^q$?",
            r"$b^q = (1\,0 \cdots 0)_b$",
            r"needs $q + 1$ digits, but $\log_b b^q$ is exactly $q$,",
            "so the ceiling has nothing to round up.",
        )
        self.qa(
            "2. What's the correct formula?",
            r"$n = \lceil \log_b (N + 1) \rceil = \lfloor \log_b N \rfloor + 1$",
            r"$2 \to \lceil \log_2 3 \rceil = 2 \qquad 8 \to \lceil \log_2 9 \rceil = 4 \qquad 81 \to \lceil \log_3 82 \rceil = 5$",
        )
        self.qa(
            r"3. Why $\log$?",
            r"$n$ digits reach at most $b^n - 1$,",
            r"so we need the smallest $n$ with $b^n > N$,",
            "and finding an exponent is exactly what a logarithm does.",
        )

        self.remove(*self.mobjects)
        thanks = Tex(
            r"With the greatest thanks to\\[6pt] M.~M.~Nouri, M.~M.~Mousavi and N.~Araghi"
        )
        self.play(Write(thanks))
        self.wait(2)
