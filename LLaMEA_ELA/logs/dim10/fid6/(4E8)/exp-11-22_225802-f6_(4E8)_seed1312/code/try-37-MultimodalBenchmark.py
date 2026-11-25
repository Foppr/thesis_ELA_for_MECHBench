import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_norm**2)
        
        # Add chaotic sinusoidal oscillations with multiple frequencies and dynamic scaling
        f2 = 0.3 * np.sum(np.sin(16 * np.pi * x_norm) + 0.5 * np.sin(32 * np.pi * x_norm))
        
        # Add a quartic term to increase complexity
        f3 = 0.03 * np.sum(x_norm**4)
        
        # Add a sextic term for even higher complexity
        f4 = 0.01 * np.sum(x_norm**6)
        
        # Add an octic term for maximum complexity
        f5 = 0.005 * np.sum(x_norm**8)
        
        # Add interactive cross-terms with dynamic coupling coefficients
        cross_terms = 0
        for i in range(self.dim - 1):
            cross_terms += (i + 1) * x_norm[i] * x_norm[i+1]
        f6 = 0.02 * cross_terms
        
        # Add nested valleys using a combination of sinusoidal and polynomial terms
        f7 = 0.1 * np.sum(np.sin(4 * np.pi * x_norm**2))
        
        # Combine all terms with dynamic weights
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7
        
        return result