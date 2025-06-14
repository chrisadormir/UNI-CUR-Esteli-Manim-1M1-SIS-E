from manim import *

class Multiplicacion_de_matrices(Scene):
    def construct(self):
        background = Rectangle().scale(3.2)
        background.set_fill(opacity=0.5)
        background.set_color([TEAL, RED, YELLOW])
        self.add(background)
        
        title = Title("Multiplicacion de matrices", include_underline=True)
        title.shift(DOWN * 0.6)
        self.add(title)
        
        m0 = Matrix([[2, 3]])
        label_a = MathTex("A =").next_to(m0, LEFT, buff=0.3)
        group_a = VGroup(label_a, m0)
        group_a.shift(LEFT * 2)
        self.add(group_a)
        
        m1 = Matrix([[1], [4]])
        label_b = MathTex("B =").next_to(m1, LEFT, buff=0.3)
        group_b = VGroup(label_b, m1)
        group_b.next_to(RIGHT, buff=0.5)
        self.add(group_b)
        
        matrices = VGroup(group_a, group_b)
        self.play(
            matrices.animate.shift(UP * 1.3).scale(0.7),
            run_time=2
        )
        self.wait(0.5)
        
        bracket_width = 1.2
        result_matrix = Matrix([["?"]], bracket_h_buff=bracket_width)
        label_result = MathTex("A \\times B =").next_to(result_matrix, LEFT, buff=0.3)
        group_result = VGroup(label_result, result_matrix)
        group_result.shift(DOWN * 0.5 + RIGHT * 0.7)
        
        self.play(Write(group_result), run_time=2)
        self.wait(0.5)
        
        question_mark = result_matrix.get_entries()[0]
        self.play(FadeOut(question_mark), run_time=1)
        self.wait(0.5)
        
        number_2_a = m0.get_entries()[0]
        box_2 = SurroundingRectangle(number_2_a, color=BLUE_C, buff=0.1)
        box_2.set_fill(TEAL_D, opacity=0.3)
        self.play(Create(box_2), run_time=1)
        self.wait(0.5)
        
        number_1_b = m1.get_entries()[0]
        box_1 = SurroundingRectangle(number_1_b, color=BLUE_C, buff=0.1)
        box_1.set_fill(TEAL_D, opacity=0.3)
        self.play(Create(box_1), run_time=1)
        self.wait(0.5)
        
        copy_2 = number_2_a.copy()
        copy_1 = number_1_b.copy()
        
        result_center = result_matrix.get_center()
        left_position_offset = 0.8
        internal_left_adjustment = 0.1
        
        self.play(copy_2.animate.move_to(result_center + LEFT * left_position_offset + LEFT * internal_left_adjustment), run_time=1.5)
        self.wait(0.5)
        
        times_symbol = MathTex("\\times")
        times_symbol.next_to(copy_2, RIGHT, buff=0.1)
        
        self.play(
            copy_1.animate.next_to(times_symbol, RIGHT, buff=0.1),
            Write(times_symbol),
            run_time=1.5
        )
        self.wait(0.5)
        
        plus_symbol = MathTex("+")
        plus_symbol.next_to(copy_1, RIGHT, buff=0.1)
        self.play(Write(plus_symbol), run_time=1)
        self.wait(0.5)
        
        number_3_a = m0.get_entries()[1]
        box_3 = SurroundingRectangle(number_3_a, color=BLUE_C, buff=0.1)
        box_3.set_fill(TEAL_D, opacity=0.3)
        self.play(
            FadeOut(box_2),
            Create(box_3),
            run_time=1
        )
        self.wait(0.5)
        
        number_4_b = m1.get_entries()[1]
        box_4 = SurroundingRectangle(number_4_b, color=BLUE_C, buff=0.1)
        box_4.set_fill(TEAL_D, opacity=0.3)
        self.play(
            FadeOut(box_1),
            Create(box_4),
            run_time=1
        )
        self.wait(0.5)
        
        copy_3 = number_3_a.copy()
        self.play(copy_3.animate.next_to(plus_symbol, RIGHT, buff=0.1), run_time=1.5)
        self.wait(0.5)
        
        times_symbol_2 = MathTex("\\times")
        times_symbol_2.next_to(copy_3, RIGHT, buff=0.1)
        copy_4 = number_4_b.copy()
        
        self.play(
            Write(times_symbol_2),
            copy_4.animate.next_to(times_symbol_2, RIGHT, buff=0.1),
            run_time=1.5
        )
        self.wait(0.5)
        
        self.play(
            FadeOut(box_3),
            FadeOut(box_4),
            run_time=1
        )
        self.wait(0.5)
        
        first_expression = VGroup(copy_2, times_symbol, copy_1)
        highlight_box_1 = SurroundingRectangle(first_expression, color=RED_C, buff=0.1)
        highlight_box_1.set_fill(RED_D, opacity=0.3)
        self.play(Create(highlight_box_1), run_time=1)
        self.wait(0.5)
        
        answer_2 = MathTex("2")
        answer_2.move_to(first_expression.get_center())
        self.play(
            FadeOut(highlight_box_1),
            Transform(first_expression, answer_2),
            run_time=1.5
        )
        self.wait(0.5)
        
        second_expression = VGroup(copy_3, times_symbol_2, copy_4)
        highlight_box_2 = SurroundingRectangle(second_expression, color=RED_C, buff=0.1)
        highlight_box_2.set_fill(RED_D, opacity=0.3)
        self.play(Create(highlight_box_2), run_time=1)
        self.wait(0.5)
        
        answer_12 = MathTex("12")
        answer_12.move_to(second_expression.get_center())
        self.play(
            FadeOut(highlight_box_2),
            Transform(second_expression, answer_12),
            run_time=1.5
        )
        self.wait(0.5)
        
        final_expression = VGroup(first_expression, plus_symbol, second_expression)
        highlight_box_final = SurroundingRectangle(final_expression, color=PURPLE_A, buff=0.1)
        highlight_box_final.set_fill(PURPLE_C, opacity=0.3)
        self.play(Create(highlight_box_final), run_time=1)
        self.wait(0.5)
        
        final_answer = MathTex("14")
        final_answer.move_to(final_expression.get_center())
        self.play(
            FadeOut(highlight_box_final),
            Transform(final_expression, final_answer),
            run_time=1.5
        )
        self.wait(0.5)
        
        complete_result = VGroup(group_result, final_expression)
        final_highlight_box = SurroundingRectangle(complete_result, color=MAROON_C, buff=0.2)
        final_highlight_box.set_fill(MAROON_A, opacity=0.3)
        self.play(Create(final_highlight_box), run_time=2)
        
        self.wait(2)
