import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial potential terms with varying degrees and coefficients
        poly = 0
        for i in range(self.dim):
            poly += 0.5 * (x[i] ** 6) - 2.3 * (x[i] ** 5) + 3.7 * (x[i] ** 4) - 1.8 * (x[i] ** 3) + 0.9 * (x[i] ** 2)
        
        # Trigonometric wave interference terms creating oscillatory behavior
        waves = 0
        for i in range(self.dim):
            waves += 2.1 * np.sin(3.2 * x[i]) * np.cos(2.7 * x[i]) + 1.5 * np.sin(4.1 * x[i]) + 0.8 * np.cos(5.3 * x[i])
        
        # Radial symmetry component with multiple peaks and valleys
        radial = 0
        r_squared = np.sum(x ** 2)
        radial += 3.2 * np.exp(-0.1 * r_squared) * np.sin(2.5 * np.sqrt(r_squared)) + 1.8 * np.exp(-0.05 * r_squared) * np.cos(3.1 * np.sqrt(r_squared))
        
        # Cross-dimensional interaction terms with variable coupling strengths
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dx = x[i] - x[j]
                dy = x[i] + x[j]
                cross += 0.7 * np.sin(1.5 * dx) * np.cos(2.3 * dy) + 0.4 * np.exp(-0.5 * (dx**2 + dy**2))
        
        # Add a global scaling factor and offset
        return 2.5 * poly + 1.8 * waves + 0.3 * radial + 0.15 * cross + 25 * self.dim