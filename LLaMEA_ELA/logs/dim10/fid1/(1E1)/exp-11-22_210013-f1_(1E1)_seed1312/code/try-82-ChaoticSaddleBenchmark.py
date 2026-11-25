import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with mild conditioning
        quadratic = 0.1 * np.sum(x**2)
        
        # Chaotic saddle-point component with exponential decay
        chaotic = 0.0
        for i in range(self.dim):
            # Saddle-like behavior with varying curvature
            chaotic += (x[i] - 1)**2 * (x[i] + 1)**2
            # Add exponentially decaying interaction with next dimension
            chaotic += 0.5 * np.exp(-0.1 * abs(x[i])) * np.sin(3 * x[(i + 1) % self.dim])
        
        # Fractal-like high-frequency oscillation with self-similarity
        fractal = 0.0
        for i in range(self.dim):
            # Multiple frequency components with decreasing amplitude
            fractal += 0.3 * np.sin(10 * x[i]) * np.cos(7 * x[(i + 1) % self.dim])
            fractal += 0.15 * np.sin(20 * x[i]) * np.cos(14 * x[(i + 2) % self.dim])
            fractal += 0.075 * np.sin(40 * x[i]) * np.cos(28 * x[(i + 3) % self.dim])
        
        # Correlated noise component with long-range dependence
        noise = 0.0
        for i in range(self.dim):
            # Correlated through a geometric series
            noise += (0.5 ** (i % 5)) * np.sin(5 * x[i]) * np.cos(2 * x[(i + 1) % self.dim])
        
        # Global structure with multiple basins of attraction
        global_structure = 0.0
        for i in range(self.dim):
            global_structure += (x[i] - 2)**3 * np.sin(x[i])
            global_structure += 0.5 * np.cos(4 * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Combine all components with appropriate scaling
        return 1.0 * quadratic + 1.5 * chaotic + 1.2 * fractal + 0.8 * noise + 1.3 * global_structure