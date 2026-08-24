import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Quadratic basin term for global convergence
        quadratic = np.sum(x_scaled**2)
        
        # Chaotic sinusoidal interference creating multiple local minima
        chaotic = np.sum(np.sin(10 * np.pi * x_scaled) * np.cos(7 * np.pi * x_scaled))
        
        # Exponentially decaying barrier terms to increase gradient complexity
        barriers = np.sum(np.exp(-5 * np.abs(x_scaled)) * np.sin(3 * np.pi * x_scaled))
        
        # Logarithmic attraction field towards origin to guide optimization
        if np.all(x_scaled != 0):
            attraction = np.sum(np.log(1 + np.abs(x_scaled)) * np.cos(2 * np.pi * x_scaled))
        else:
            attraction = 0.0
        
        # Combine all components with varying weights
        return 0.2 * quadratic + 0.4 * chaotic + 0.3 * barriers + 0.1 * attraction + 1.0