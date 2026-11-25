import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Quadratic basin term - global minimum at origin
        basin = np.sum(x_norm**2)
        
        # Multimodal periodic terms with multiple global minima
        periodic = 0.0
        for i in range(self.dim):
            periodic += np.sin(5 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[i])
        
        # Additional harmonic terms to increase complexity
        harmonic = 0.0
        for i in range(self.dim):
            harmonic += np.sin(2 * np.pi * x_norm[i])**2 + np.cos(2 * np.pi * x_norm[i])**2
        
        # Combine all terms with different weights
        return 10 * basin + 5 * periodic + 2 * harmonic + 1.0