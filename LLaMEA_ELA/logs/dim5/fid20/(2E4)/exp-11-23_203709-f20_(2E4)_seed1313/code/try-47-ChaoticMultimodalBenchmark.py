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
            poly += 0.3 * (x[i] ** 6) - 1.8 * (x[i] ** 5) + 2.9 * (x[i] ** 4) - 1.2 * (x[i] ** 3) + 0.7 * (x[i] ** 2)
        
        # Trigonometric wave interference terms creating oscillatory behavior
        waves = 0
        for i in range(self.dim):
            waves += 1.8 * np.sin(2.9 * x[i]) * np.cos(2.1 * x[i]) + 1.3 * np.sin(3.7 * x[i]) + 0.6 * np.cos(4.8 * x[i])
        
        # Radial symmetry component with multiple peaks and valleys
        radial = 0
        r_squared = np.sum(x ** 2)
        radial += 2.8 * np.exp(-0.15 * r_squared) * np.sin(2.2 * np.sqrt(r_squared)) + 1.5 * np.exp(-0.08 * r_squared) * np.cos(2.9 * np.sqrt(r_squared))
        
        # Cross-dimensional interaction terms with variable coupling strengths
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dx = x[i] - x[j]
                dy = x[i] + x[j]
                cross += 0.6 * np.sin(1.8 * dx) * np.cos(2.1 * dy) + 0.3 * np.exp(-0.4 * (dx**2 + dy**2))
        
        # Add a global scaling factor and offset
        return 2.2 * poly + 1.5 * waves + 0.25 * radial + 0.12 * cross + 20 * self.dim