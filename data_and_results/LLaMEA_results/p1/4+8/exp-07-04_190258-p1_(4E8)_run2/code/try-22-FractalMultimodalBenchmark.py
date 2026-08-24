import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Fractal-like recursive sinusoidal modulation
        fractal = 0
        for i in range(self.dim):
            # Recursive modulation with decreasing amplitude
            mod = 1.0
            for j in range(1, 6):  # 5 levels of recursion
                mod *= 0.5
                fractal += mod * np.sin(2**j * x[i]) * np.cos(3**j * x[i])
        
        # Gradient complexity component with varying frequencies
        gradient = 0
        for i in range(self.dim):
            gradient += (x[i]**3) * np.sin(x[i]) * np.cos(0.5 * x[i])
        
        # Cross-dimensional interaction with exponential decay
        cross = 0
        for i in range(self.dim - 1):
            cross += np.exp(-0.1 * (x[i] - x[i+1])**2) * np.sin(x[i] * x[i+1])
        
        # Global scaling factor to balance contributions
        return 0.1 * quadratic + fractal + gradient + cross