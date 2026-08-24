import numpy as np

class ChaoticModulatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Exponential barrier terms to create rugged landscape
        barrier = np.sum(np.exp(-10 * np.abs(x_scaled)))
        
        # Sinusoidal modulation with varying frequencies
        modulation = np.sum(np.sin(10 * np.pi * x_scaled) * np.cos(5 * np.pi * x_scaled))
        
        # Quadratic term with chaotic scaling factor
        quadratic = np.sum(x_scaled**2 * (1 + 0.1 * np.sin(20 * np.pi * x_scaled)))
        
        # Add a small chaotic component
        chaotic = 0.01 * np.sum(np.sin(np.exp(x_scaled)) * np.cos(np.exp(-x_scaled)))
        
        # Combine all components
        return barrier + 0.5 * modulation + quadratic + chaotic