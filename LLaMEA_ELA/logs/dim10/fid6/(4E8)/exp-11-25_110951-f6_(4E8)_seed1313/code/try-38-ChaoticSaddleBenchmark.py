import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term with adaptive conditioning
        quadratic = 0.5 * np.sum(x**2)
        
        # Chaotic saddle-point structure with exponential decay
        chaotic = 0
        for i in range(self.dim):
            # Exponentially decaying trigonometric components
            chaotic += np.exp(-0.1 * i) * np.sin(2.0 * x[i]) * np.cos(3.0 * x[i])
            chaotic += np.exp(-0.05 * i) * np.sin(5.0 * x[i])**2 * np.cos(2.0 * x[i])
            
        # Multi-scale coupling with varying frequencies
        coupling = 0
        for i in range(self.dim):
            if i < self.dim - 1:
                coupling += 0.3 * np.exp(-0.5 * x[i]**2) * np.sin(4.0 * (x[i] + x[i+1]))
            if i < self.dim - 2:
                coupling += 0.2 * np.exp(-0.3 * (x[i]**2 + x[i+1]**2)) * np.cos(3.0 * (x[i] + x[i+2]))
        
        # Asymmetric basin with varying curvature
        asymmetric = 0
        for i in range(self.dim):
            # Varying curvature based on dimension index
            curvature = 1.0 + 0.5 * np.sin(0.5 * i)
            asymmetric += curvature * np.exp(-0.2 * x[i]**2) * np.sin(0.8 * x[i])**3
        
        # Add noise-like perturbations for additional challenge
        noise = 0.01 * np.sum(np.sin(10.0 * x) * np.cos(7.0 * x))
        
        return quadratic + chaotic + coupling + asymmetric + noise