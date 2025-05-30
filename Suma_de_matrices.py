from manim import *
import numpy as np

class Suma_de_Matrices(Scene):
    def construct(self):
        title_gradient = [BLUE_A, BLUE_D]
        highlight_color = [PURPLE_A, PURPLE_D]
        matrix_color = YELLOW
        
        title = Text("Suma de matrices", font_size=48)
        title.set_color_by_gradient(*title_gradient)
        title.move_to(ORIGIN + UP * 1.5)
        
        self.play(Write(title))
        self.play(title.animate.shift(UP * 0.2))
        self.wait(0.5)
        
        matrix_a = [[1, 2], [3, 4]]
        matrix_b = [[5, 6], [7, 8]]
        
        a_label = MathTex("A = ", font_size=36)
        b_label = MathTex("B = ", font_size=36)
        
        a_matrix = IntegerMatrix(matrix_a, left_bracket="(", right_bracket=")")
        b_matrix = IntegerMatrix(matrix_b, left_bracket="(", right_bracket=")")
        
        a_matrix.get_brackets().set_color(matrix_color)
        b_matrix.get_brackets().set_color(matrix_color)
        
        a_group = VGroup(a_label, a_matrix).arrange(RIGHT)
        b_group = VGroup(b_label, b_matrix).arrange(RIGHT)
        
        matrix_groups = VGroup(a_group, b_group).arrange(RIGHT, buff=1.5)
        matrix_groups.next_to(title, DOWN, buff=0.7)
        
        self.play(FadeIn(matrix_groups))
        self.wait()
        
        self.play(
            matrix_groups.animate.scale(0.8).shift(UP * 0.5),
            title.animate.shift(UP * 0.1)
        )
        self.wait()
        
        sum_matrix_elements = [
            [f"{a}+{b}" for a, b in zip(row_a, row_b)]
            for row_a, row_b in zip(matrix_a, matrix_b)
        ]
        
        sum_label = MathTex("A + B = ", font_size=36)
        sum_matrix = Matrix(sum_matrix_elements, left_bracket="(", right_bracket=")")
        sum_matrix.get_brackets().set_color(matrix_color)
        
        sum_group = VGroup(sum_label, sum_matrix).arrange(RIGHT)
        sum_group.next_to(matrix_groups, DOWN, buff=0.8)
        
        self.play(Write(sum_group))
        self.wait()
        
        plus_signs = []
        
        main_plus = sum_label[0][1]
        plus_signs.append(main_plus)
        
        for element in sum_matrix.get_entries():
            tex = element.tex_string
            plus_pos = tex.find("+")
            if plus_pos >= 0:
                plus_part = element[0][plus_pos:plus_pos+1]
                plus_signs.append(plus_part)
        
        highlight_boxes = []
        for sign in plus_signs:
            box = SurroundingRectangle(
                sign,
                corner_radius=0.1,
                stroke_width=2,
                buff=0.1,
                stroke_color=color_gradient(highlight_color, 2)[0],
                fill_color=PURPLE,
                fill_opacity=0.2
            )
            highlight_boxes.append(box)
        
        self.play(*[Create(box) for box in highlight_boxes])
        self.wait(1)
        self.play(*[FadeOut(box) for box in highlight_boxes])
        self.wait()
        
        for i in range(len(matrix_a)):
            for j in range(len(matrix_a[0])):                
                a_entry = a_matrix.get_entries()[i*2 + j]
                b_entry = b_matrix.get_entries()[i*2 + j]
                sum_entry = sum_matrix.get_entries()[i*2 + j]
                
                parts = sum_entry.tex_string.split("+")
                a_num = parts[0]
                b_num = parts[1]
                
                sum_a_part = sum_entry[0][:len(a_num)]
                sum_b_part = sum_entry[0][-len(b_num):]
                
                a_box = SurroundingRectangle(
                    a_entry,
                    corner_radius=0.1,
                    stroke_width=2,
                    buff=0.1,
                    stroke_color=color_gradient(highlight_color, 2)[0],
                    fill_color=PURPLE,
                    fill_opacity=0.2
                )
                
                sum_a_box = SurroundingRectangle(
                    sum_a_part,
                    corner_radius=0.1,
                    stroke_width=2,
                    buff=0.1,
                    stroke_color=color_gradient(highlight_color, 2)[0],
                    fill_color=PURPLE,
                    fill_opacity=0.2
                )
                
                self.play(Create(a_box), Create(sum_a_box))
                self.wait(0.5)
                self.play(FadeOut(a_box), FadeOut(sum_a_box))
                
                b_box = SurroundingRectangle(
                    b_entry,
                    corner_radius=0.1,
                    stroke_width=2,
                    buff=0.1,
                    stroke_color=color_gradient(highlight_color, 2)[0],
                    fill_color=PURPLE,
                    fill_opacity=0.2
                )
                
                sum_b_box = SurroundingRectangle(
                    sum_b_part,
                    corner_radius=0.1,
                    stroke_width=2,
                    buff=0.1,
                    stroke_color=color_gradient(highlight_color, 2)[0],
                    fill_color=PURPLE,
                    fill_opacity=0.2
                )
                
                self.play(Create(b_box), Create(sum_b_box))
                self.wait(0.5)
                self.play(FadeOut(b_box), FadeOut(sum_b_box))
        
        self.wait()
        
        result_values = [[6, 8], [10, 12]]
        
        working_matrix = sum_matrix.copy()
        self.add(working_matrix)
        self.remove(sum_matrix)
        
        for i in range(len(matrix_a)):
            for j in range(len(matrix_a[0])):
                entry_index = i*2 + j
                current_entry = working_matrix.get_entries()[entry_index]
                
                expr_box = SurroundingRectangle(
                    current_entry,
                    corner_radius=0.1,
                    stroke_width=2,
                    buff=0.1,
                    stroke_color=GREEN,
                    fill_color=GREEN,
                    fill_opacity=0.2
                )
                
                self.play(Create(expr_box))
                self.wait(0.3)
                
                result_value = str(result_values[i][j])
                replacement = MathTex(result_value, font_size=36)
                replacement.move_to(current_entry.get_center())
                
                self.play(
                    ReplacementTransform(current_entry, replacement),
                    FadeOut(expr_box)
                )
                
                working_matrix.get_entries()[entry_index] = replacement
                self.wait(0.5)
        
        final_matrix = IntegerMatrix(result_values, left_bracket="(", right_bracket=")")
        final_matrix.get_brackets().set_color(matrix_color)
        final_matrix.move_to(working_matrix.get_center())
        
        new_brackets = final_matrix.get_brackets()
        old_brackets = working_matrix.get_brackets()
        
        self.play(
            ReplacementTransform(old_brackets, new_brackets),
            *[ReplacementTransform(working_matrix.get_entries()[i], final_matrix.get_entries()[i]) 
              for i in range(len(working_matrix.get_entries()))],
            run_time=1.5
        )
        
        self.wait(2)
