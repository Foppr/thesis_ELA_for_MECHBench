import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Nested chaotic sinusoidal perturbations with multiple frequencies
        chaotic = 0
        for i in range(self.dim):
            chaotic += (np.sin(9 * x[i]) * np.cos(5 * x[i]) * np.tan(3 * x[i]) * 
                       np.exp(-0.15 * x[i]**2) * np.log(1 + 0.1 * x[i]**2))
        
        # Higher-order saddle point structure with polynomial and trigonometric mixing
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**8 - 4 * x[i]**6 + 6 * x[i]**4 - 4 * x[i]**2 + 1) * np.cos(2 * x[i])
        
        # Complex cross-term interactions with multi-scale coupling
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += 0.3 * x[i] * x[j] * np.sin(0.5 * (x[i]**3 + x[j]**3)) * np.cos(0.2 * x[i] * x[j])
        
        # Additional chaotic modulation with exponential and logarithmic coupling
        modulate = 0
        for i in range(self.dim):
            modulate += 0.7 * np.sin(3 * x[i]) * np.cos(7 * x[i]) * np.exp(-0.05 * x[i]**2) * np.sin(0.1 * x[i]**4)
        
        # Fractal-like self-similar structure with recursive scaling
        fractal = 0
        for i in range(self.dim):
            fractal += 0.1 * np.sin(10 * x[i]) * np.cos(10 * x[i]) * np.exp(-0.2 * x[i]**2) * np.sin(0.05 * x[i]**6)
        
        return quadratic + chaotic + saddle + cross + modulate + fractal