import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Shifted global optimum
        self.optimum = np.full(dim, 1.5)
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = (x - self.optimum) / 3.5
        
        # Polynomial base with varying degrees
        poly_base = np.sum((x_norm ** 3) + 0.5 * (x_norm ** 2) + 0.1 * x_norm)
        
        # Fractal-like self-similar structure using recursive sine
        fractal = 0.0
        for i in range(self.dim):
            temp = x_norm[i]
            for _ in range(4):  # 4 levels of recursion
                temp = np.sin(3 * temp)
            fractal += temp ** 2
        
        # Exponential interaction terms with varying coupling strengths
        exp_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                coupling = 0.1 * (j - i)
                exp_interaction += np.exp(-coupling * (x_norm[i]**2 + x_norm[j]**2)) * np.sin(3 * (x_norm[i] - x_norm[j]))
        
        # Hybrid multimodal component with polynomial and trigonometric mix
        hybrid = 0.0
        for i in range(self.dim):
            hybrid += (x_norm[i]**4 - 2 * x_norm[i]**2 + 1) * np.cos(5 * x_norm[i])
        
        # Cross-term with asymmetric interaction
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += np.sin(2 * x_norm[i]) * np.cos(2 * x_norm[i+1]) * (1 + 0.1 * x_norm[i]**2)
        
        # Global structure with high-frequency oscillation
        high_freq = np.sum(np.sin(25 * x_norm) ** 2 + np.cos(25 * x_norm) ** 2)
        
        # Combine all components with different weights
        return 0.8 * poly_base + 1.2 * fractal + 1.0 * exp_interaction + 0.9 * hybrid + 0.6 * cross_term + 1.5 * high_freq