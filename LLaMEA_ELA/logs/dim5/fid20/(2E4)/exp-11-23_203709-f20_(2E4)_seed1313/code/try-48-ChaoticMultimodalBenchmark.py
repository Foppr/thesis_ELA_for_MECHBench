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
            poly += 0.7 * (x[i] ** 6) - 2.8 * (x[i] ** 5) + 4.1 * (x[i] ** 4) - 2.2 * (x[i] ** 3) + 1.1 * (x[i] ** 2)
        
        # Trigonometric wave interference terms creating oscillatory behavior
        waves = 0
        for i in range(self.dim):
            waves += 2.5 * np.sin(3.5 * x[i]) * np.cos(2.9 * x[i]) + 1.8 * np.sin(4.3 * x[i]) + 1.0 * np.cos(5.7 * x[i])
        
        # Radial symmetry component with multiple peaks and valleys
        radial = 0
        r_squared = np.sum(x ** 2)
        radial += 3.5 * np.exp(-0.12 * r_squared) * np.sin(2.7 * np.sqrt(r_squared)) + 2.0 * np.exp(-0.06 * r_squared) * np.cos(3.3 * np.sqrt(r_squared))
        
        # Enhanced cross-dimensional interaction terms with stronger coupling
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dx = x[i] - x[j]
                dy = x[i] + x[j]
                cross += 0.9 * np.sin(1.7 * dx) * np.cos(2.5 * dy) + 0.6 * np.exp(-0.4 * (dx**2 + dy**2))
        
        # Add a global scaling factor and offset with improved balance
        return 2.2 * poly + 1.5 * waves + 0.25 * radial + 0.2 * cross + 20 * self.dim