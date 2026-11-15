import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic basin term for global attraction
        quadratic = np.sum(x_scaled**2)
        
        # Chaotic sinusoidal component with varying frequencies
        chaotic = np.sum(np.sin(10 * np.pi * x_scaled) * np.cos(7 * np.pi * x_scaled))
        
        # Exponential barrier terms to create rugged terrain with modified weights
        barriers = np.sum(1.5 * np.exp(-4 * np.abs(x_scaled)) * np.sin(3 * np.pi * x_scaled)**2)
        
        # Saddle point structure using mixed polynomial terms
        saddle = np.sum(x_scaled**4 - 2 * x_scaled**2)
        
        # Add cross-dimensional coupling term for increased complexity
        coupling = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(5 * np.pi * x_scaled[:-1]))
        
        # Combine all components with different weights
        return 0.5 * quadratic + 2.0 * chaotic + barriers + 0.3 * saddle + 0.1 * coupling