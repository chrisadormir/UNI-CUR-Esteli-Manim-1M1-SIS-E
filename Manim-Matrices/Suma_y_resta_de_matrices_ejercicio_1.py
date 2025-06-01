from manim import *

class Suma_y_resta_de_matrices_ejercicio_1(Scene):
    def construct(self):
        title_gradient = [YELLOW_A, YELLOW_C]
        highlight_color = [PURPLE_A, PURPLE_E]
        matrix_color = YELLOW

        title = Text("Suma y resta de matrices", font_size=48)
        title.set_color_by_gradient(*title_gradient)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title))
        self.wait(0.5)

        matrix_a = [[2, 3], [1, 5]]
        matrix_b = [[4, 1], [0, -2]]
        matrix_c = [[3, 2], [1, 1]]

        def create_matrix(matrix, label_text, format_negatives=True):
            if format_negatives:
                formatted_matrix = [
                    [f"({x})" if x < 0 else str(x) for x in row]
                    for row in matrix
                ]
            else:
                formatted_matrix = [
                    [str(x) for x in row]
                    for row in matrix
                ]
            matrix_mob = Matrix(
                formatted_matrix,
                left_bracket="(",
                right_bracket=")",
                v_buff=1.0,
                h_buff=1.0
            )
            matrix_mob.get_brackets().set_color(matrix_color)
            label = MathTex(label_text, font_size=36)
            return VGroup(label, matrix_mob).arrange(RIGHT, buff=0.3)

        a_group = create_matrix(matrix_a, "A =")
        b_group = create_matrix(matrix_b, "B =", format_negatives=False)
        c_group = create_matrix(matrix_c, "C =")

        matrix_groups = VGroup(a_group, b_group, c_group).arrange(RIGHT, buff=1.0)
        matrix_groups.next_to(title, DOWN, buff=0.8)

        self.play(FadeIn(matrix_groups))
        self.wait()

        def format_operation(a, b, c):
            b_str = f"({b})" if b < 0 else str(b)
            return f"{a}+{b_str}-{c}"

        operation_elements = [
            [format_operation(a, b, c) for a, b, c in zip(row_a, row_b, row_c)]
            for row_a, row_b, row_c in zip(matrix_a, matrix_b, matrix_c)
        ]

        operation_label = MathTex("A + B - C = ", font_size=36)
        
        operation_matrix = Matrix(
            operation_elements,
            left_bracket="(",
            right_bracket=")",
            v_buff=1.4,
            h_buff=2.1
        )
        
        operation_matrix.get_brackets().stretch_to_fit_height(operation_matrix.height*1.2)
        operation_matrix.get_brackets().set_color(matrix_color)
        
        for element in operation_matrix.get_entries():
            element.set_font_size(32)

        operation_matrix.get_entries()[3].shift(RIGHT*0.2)
        operation_matrix.get_brackets().stretch_to_fit_width(operation_matrix.width*1.05)

        operation_group = VGroup(operation_label, operation_matrix).arrange(RIGHT, buff=0.3)
        operation_group.next_to(matrix_groups, DOWN, buff=1.0)

        self.play(Write(operation_group))
        self.wait()

        def highlight_operators(operator_char, color):
            operators = []
            
            if operator_char == "+":
                main_op = operation_label[0][1]
            else:
                main_op = operation_label[0][3]
            operators.append(main_op)
            
            for element in operation_matrix.get_entries():
                tex = element.tex_string
                op_positions = [i for i, c in enumerate(tex) if c == operator_char]
                for pos in op_positions:
                    if operator_char == "-" and pos > 0 and tex[pos-1] == "(":
                        continue
                    op_part = element[0][pos:pos+1]
                    operators.append(op_part)
            
            boxes = []
            for op in operators:
                box = SurroundingRectangle(
                    op,
                    corner_radius=0.1,
                    stroke_width=2,
                    buff=0.1,
                    stroke_color=color,
                    fill_color=color,
                    fill_opacity=0.2
                )
                boxes.append(box)
            
            self.play(*[Create(box) for box in boxes])
            self.wait(1)
            self.play(*[FadeOut(box) for box in boxes])
            self.wait()

        highlight_operators("+", color_gradient(highlight_color, 2)[0])
        highlight_operators("-", color_gradient(highlight_color, 2)[0])

        result_values = [
            [a+b-c for a, b, c in zip(row_a, row_b, row_c)]
            for row_a, row_b, row_c in zip(matrix_a, matrix_b, matrix_c)
        ]

        working_matrix = operation_matrix.copy()
        self.add(working_matrix)
        self.remove(operation_matrix)

        for i in range(len(matrix_a)):
            for j in range(len(matrix_a[0])):
                entry_index = i*2 + j
                current_entry = working_matrix.get_entries()[entry_index]

                expr_box = SurroundingRectangle(
                    current_entry,
                    corner_radius=0.1,
                    stroke_width=2,
                    buff=0.15,
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
                self.wait(0.5)

        final_matrix = Matrix(
            result_values,
            left_bracket="(",
            right_bracket=")",
            v_buff=1.3,
            h_buff=2.0
        )
        final_matrix.get_brackets().set_color(matrix_color)
        final_matrix.move_to(working_matrix.get_center())

        self.play(
            ReplacementTransform(working_matrix.get_brackets(), final_matrix.get_brackets()),
            *[ReplacementTransform(working_matrix.get_entries()[i], final_matrix.get_entries()[i]) 
              for i in range(len(working_matrix.get_entries()))],
            run_time=1.5
        )

        self.wait(3)
