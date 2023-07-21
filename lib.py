# pytest_failed_black_passed
class QuadraticEquationSolver:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        d = self.b**2 - 4 * self.a * self.c

        if d <= 0:
            return []

        if d == 0:
            return [-self.b / (2 * self.a)]

        return [
            (-self.b + d**0.5) / (2 * self.a),
            (-self.b - d**0.5) / (2 * self.a),
        ]


# 30975168992760024573
