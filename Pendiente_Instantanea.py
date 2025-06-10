from manim import *

class PendienteInstantanea(Scene):
    def construct(self):
        # Título
        titulo = Text("Pendiente Instantánea", font_size=48, color=BLUE)
        titulo.to_edge(UP)
        self.play(Write(titulo))
        self.wait(0.5)
        self.play(FadeOut(titulo, run_time=0.5))  # Fade out title fast
        
        # Crear ejes
        axes = Axes(
            x_range=[-1, 4, 1],
            y_range=[-1, 5, 1],
            x_length=8,
            y_length=6,
            axis_config={"color": WHITE},
            tips=False,
        )
        
        # Etiquetas de los ejes
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        
        # Función cuadrática f(x) = x²
        def func(x):
            return x**2
        
        # Crear la curva
        curve = axes.plot(func, x_range=[0, 2.5], color=YELLOW)
        func_label = MathTex("f(x) = x^2", color=YELLOW).next_to(curve, UP).shift(LEFT*2)
        
        self.play(Create(curve), Write(func_label))
        self.wait(1)
        
        # Punto donde calcularemos la pendiente instantánea
        x_point = 1.5
        y_point = func(x_point)
        point = Dot(axes.coords_to_point(x_point, y_point), color=RED, radius=0.08)
        point_label = MathTex(f"({x_point}, {y_point:.1f})", color=RED).next_to(point, UR, buff=0.2)
        
        self.play(Create(point), Write(point_label))
        
        # Texto explicativo
        explicacion1 = Text("Calculemos la pendiente instantánea en este punto", 
                           font_size=24, color=WHITE).to_edge(DOWN, buff=1.5)
        self.play(Write(explicacion1))
        self.wait(2)
        
        # Crear líneas secantes que se aproximan
        h_values = [1.0, 0.5, 0.25, 0.1]
        colors = [GREEN, ORANGE, PINK, PURPLE]
        
        explicacion2 = Text("Usamos líneas secantes que se acercan al punto", 
                           font_size=24, color=WHITE).to_edge(DOWN, buff=1.5)
        self.play(Transform(explicacion1, explicacion2))
        
        secant_lines = []
        slope_texts = []
        aux_points = []
        
        for i, h in enumerate(h_values):
            # Segundo punto para la línea secante
            x2 = x_point + h
            y2 = func(x2)
            
            # Calcular pendiente de la secante
            slope = (y2 - y_point) / h
            
            # Crear línea secante extendida
            start_point = axes.coords_to_point(x_point - 0.3, y_point - 0.3 * slope)
            end_point = axes.coords_to_point(x2 + 0.3, y2 + 0.3 * slope)
            secant_line = Line(start_point, end_point, color=colors[i])
            
            # Punto secundario para la secante
            aux_point = Dot(axes.coords_to_point(x2, y2), color=colors[i], radius=0.06)
            
            # Texto con la pendiente
            slope_text = MathTex(f"m = {slope:.2f}", color=colors[i], font_size=36)
            slope_text.to_corner(UL, buff=1).shift(DOWN * i * 0.5)
            
            if i > 0:
                self.play(
                    Transform(secant_lines[0], secant_line),
                    Transform(aux_points[0], aux_point),
                    Transform(slope_texts[0], slope_text),
                    run_time=1
                )
            else:
                secant_lines.append(secant_line)
                aux_points.append(aux_point)
                slope_texts.append(slope_text)
                self.play(Create(secant_line), Create(aux_point), Write(slope_text))
            
            self.wait(1)
        
        # Línea tangente (pendiente instantánea)
        # Para f(x) = x², f'(x) = 2x, entonces f'(1.5) = 3
        instant_slope = 2 * x_point
        
        start_tangent = axes.coords_to_point(x_point - 0.8, y_point - 0.8 * instant_slope)
        end_tangent = axes.coords_to_point(x_point + 0.8, y_point + 0.8 * instant_slope)
        tangent_line = Line(start_tangent, end_tangent, color=RED, stroke_width=4)
        
        explicacion3 = Text("La línea tangente nos da la pendiente instantánea", 
                           font_size=24, color=WHITE).to_edge(DOWN, buff=1.5)
        
        final_slope_text = MathTex(f"\\text{{Pendiente instantánea}} = {instant_slope:.1f}", 
                                  color=RED, font_size=40)
        final_slope_text.to_corner(UL, buff=1)
        
        self.play(
            Transform(explicacion1, explicacion3),
            Transform(secant_lines[0], tangent_line),
            FadeOut(aux_points[0]),
            Transform(slope_texts[0], final_slope_text)
        )
        
        # Fórmula de la derivada
        formula = MathTex("f'(x) = \\lim_{h \\to 0} \\frac{f(x+h) - f(x)}{h}", 
                         color=BLUE, font_size=36)
        formula.to_edge(DOWN, buff=0.5)
        
        self.play(Transform(explicacion1, formula))
        self.wait(3)

        # Antes de escribir la conclusión, fade out the graph elements
        all_graph_objects = VGroup(
            axes, x_label, y_label, curve, func_label,
            point, point_label, secant_lines[0], aux_points[0], slope_texts[0]
        )
        self.play(FadeOut(all_graph_objects), FadeOut(explicacion1))
        self.wait(0.5)
        
        # Conclusión
        conclusion = Text("¡La pendiente instantánea es la derivada!", 
                         font_size=32, color=GREEN)
        conclusion.move_to(ORIGIN + DOWN * 2)
        
        self.play(Write(conclusion))
        self.wait(2)

