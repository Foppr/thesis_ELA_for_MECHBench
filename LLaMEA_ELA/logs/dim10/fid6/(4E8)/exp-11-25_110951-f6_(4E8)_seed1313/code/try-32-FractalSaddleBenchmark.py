import numpy as np

class FractalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term for conditioning
        quadratic = 0.05 * np.sum(x**2)
        
        # Fractal-like sinusoidal structure with multiple scales
        fractal = 0
        for i in range(self.dim):
            # Multiple frequency components creating self-similarity
            fractal += np.sin(x[i]) * np.cos(2 * x[i]) * np.sin(4 * x[i])
            fractal += 0.5 * np.sin(0.5 * x[i]) * np.cos(x[i])**2
            fractal += 0.3 * np.sin(3 * x[i]) * np.cos(0.7 * x[i])
            
        # Saddle point structure with alternating curvature
        saddle = 0
        for i in range(self.dim):
            # Create saddle points by combining positive and negative terms
            saddle += (x[i]**2 - 1)**2 * np.sin(x[i])**2
            if i < self.dim - 1:
                saddle += 0.2 * x[i] * x[i+1] * np.cos(x[i] + x[i+1])
        
        # Adaptive conditioning based on dimensionality
        adaptive = 0
        for i in range(self.dim):
            adaptive += (i + 1) * np.sin((i + 1) * x[i])**2
        
        # Cross-dimension coupling with fractal properties
        coupling = 0
        for i in range(0, self.dim - 2, 2):
            coupling += np.sin(x[i] + x[i+1]) * np.cos(x[i+2])
        
        # Add noise-like perturbations for additional challenge
        noise = 0.01 * np.sum(np.sin(10 * x) + np.cos(15 * x))
        
        return quadratic + fractal + saddle + adaptive + coupling + noise