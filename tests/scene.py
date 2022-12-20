from manim import *

class LineTest(Scene):
    def construct(self):
        p1 = [-1, -1, 0]
        p2 = [1, 1, 0]
        a = Line(p1, p2)
        self.add(a)
        self.wait()

class GraphTest(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4]
        edges = [(1, 2), (2, 3), (3, 4), (1, 3), (1, 4)]
        g = Graph(vertices, edges)
        self.add(g)
        self.wait()

class GraphAutoPosition(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4, 5, 6, 7, 8]
        edges = [(1, 7), (1, 8), (2, 3), (2, 4), (2, 5),
                 (2, 8), (3, 4), (6, 1), (6, 2),
                 (6, 3), (7, 2), (7, 4)]
        autolayouts = ["spring", "circular", "kamada_kawai",
                       "planar", "random", "shell",
                       "spectral", "spiral"]
        graphs = [Graph(vertices, edges, layout=lt).scale(0.5)
                  for lt in autolayouts]
        r1 = VGroup(*graphs[:3]).arrange()
        r2 = VGroup(*graphs[3:6]).arrange()
        r3 = VGroup(*graphs[6:]).arrange()
        self.add(VGroup(r1, r2, r3).arrange(direction=DOWN))

class GraphManualPosition(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4]
        edges = [(1, 2), (2, 3), (3, 4), (4, 1)]
        lt = {1: [0, 0, 0], 2: [1, 1, 0], 3: [1, -1, 0], 4: [-1, 0, 0]}
        G = Graph(vertices, edges, layout=lt)
        self.add(G)

class LabeledModifiedGraph(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4, 5, 6, 7, 8]
        edges = [(1, 7), (1, 8), (2, 3), (2, 4), (2, 5),
                 (2, 8), (3, 4), (6, 1), (6, 2),
                 (6, 3), (7, 2), (7, 4)]
        g = Graph(vertices, edges, layout="circular", layout_scale=3,
                labels=True,
                vertex_config={7: {"fill_color": RED}},
                edge_config={(1, 7): {"stroke_color": RED},
                               (2, 7): {"stroke_color": RED},
                               (4, 7): {"stroke_color": RED}})
        self.add(g)

class ChangeGraphLayout(Scene):
    def construct(self):
        G = Graph([1, 2, 3, 4, 5], [(1, 2), (2, 3), (3, 4), (4, 5)],
                  layout={1: [-2, 0, 0], 2: [-1, 0, 0], 3: [0, 0, 0],
                          4: [1, 0, 0], 5: [2, 0, 0]}
                  )
        self.play(Create(G))
        self.play(G.animate.change_layout("circular"))
        self.wait()

class CustomArrow(Arrow):
    def __init__(self,
        *args: Any,
        stroke_width: float = 20,
        buff: float = 0,
        max_tip_length_to_length_ratio: float = 0.27,
        max_stroke_width_to_length_ratio: float = 3,
        **kwargs,):
        super().__init__(*args, stroke_width=stroke_width, buff=buff, max_tip_length_to_length_ratio=max_tip_length_to_length_ratio, max_stroke_width_to_length_ratio=max_stroke_width_to_length_ratio, color=GOLD, **kwargs)

class ChangeGraphNodeColor(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4, 5]
        edges = [(1, 2), (2, 3), (3, 4), (4, 5)]
        G = Graph(vertices, edges,
                edge_type=CustomArrow,
                labels=True,
                layout={1: [-2, 0, 0], 2: [-1, 0, 0], 3: [0, 0, 0],
                        4: [1, 0, 0], 5: [2, 0, 0]}
                )
        self.play(Create(G))
        self.play(G.animate.change_layout("circular"))

        t = MathTex(r"1", color=BLACK)
        # G.vertices[1].set_fill(RED)
        t.next_to(G.vertices[1], LEFT, buff=-0.35)
        self.add(t)
        self.play(G.vertices[1].animate.set_fill(RED))
        
        self.wait()
