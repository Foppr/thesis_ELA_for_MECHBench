import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Periodic component with varying frequencies and amplitudes
        periodic = np.sum(np.sin(2 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled) * np.sin(5 * np.pi * x_scaled))
        
        # Exponential decay barrier with varying strengths
        barriers = np.sum(np.exp(-2 * np.abs(x_scaled)) * np.cos(4 * np.pi * x_scaled)**2)
        
        # High-dimensional coupling through pairwise interactions
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += (x_scaled[i] * x_scaled[i+1] * np.sin(2 * np.pi * (x_scaled[i] + x_scaled[i+1])))
        
        # Saddle point structure with mixed polynomial terms
        saddle = np.sum(x_scaled**6 - 3 * x_scaled**4 + 2 * x_scaled**2)
        
        # Add noise-like component for increased complexity
        noise = np.sum(np.sin(13 * x_scaled) * np.cos(17 * x_scaled))
        
        # Combine all components with different weights
        return 1.5 * periodic + 0.8 * barriers + 0.2 * coupling + 0.4 * saddle + 0.1 * noise