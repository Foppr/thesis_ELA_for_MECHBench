import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic basin term for global attraction
        quadratic = np.sum(x_scaled**2)
        
        # Chaotic sinusoidal component with varying frequencies and dynamic coupling
        chaotic = np.sum(np.sin(15 * np.pi * x_scaled) * np.cos(11 * np.pi * x_scaled) * np.sin(5 * np.pi * x_scaled))
        
        # Exponential barrier terms with dynamic weights and adaptive decay
        barriers = np.sum(np.exp(-8 * np.abs(x_scaled)) * np.sin(5 * np.pi * x_scaled)**3)
        
        # Saddle point structure with higher-order polynomial and cross-dimensional coupling
        saddle = np.sum(x_scaled**6 - 3 * x_scaled**4 + 2 * x_scaled**2)
        
        # Coupled cross-dimensional terms to increase complexity
        cross_coupling = np.sum((x_scaled[:-1] + x_scaled[1:])**2 * np.sin(10 * np.pi * x_scaled[:-1]) * np.cos(10 * np.pi * x_scaled[1:]))
        
        # Combine all components with different weights
        return 0.3 * quadratic + 2.5 * chaotic + 2.0 * barriers + 0.4 * saddle + 0.2 * cross_coupling