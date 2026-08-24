import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Base quadratic term for conditioning
        quadratic = np.sum(x_scaled**2)
        
        # Exponential barrier terms to create steep gradients near boundaries
        barriers = np.sum(np.exp(1.0 / (1.0 - np.abs(x_scaled)**2 + 1e-8)))
        
        # Sinusoidal perturbations to introduce chaos and multiple local optima
        perturbations = np.sum(np.sin(10 * np.pi * x_scaled) * np.cos(5 * np.pi * x_scaled))
        
        # Chaotic component using logistic map-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            if i > 0:
                chaotic += np.sin(3 * np.pi * x_scaled[i-1] * x_scaled[i])
        
        # Combine all components
        return quadratic + 5 * barriers + 2 * perturbations + 0.5 * chaotic