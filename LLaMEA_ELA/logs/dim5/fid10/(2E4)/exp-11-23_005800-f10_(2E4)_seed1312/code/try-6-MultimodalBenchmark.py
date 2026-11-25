import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Base quadratic term with conditioning
        f_val = np.sum(x_normalized**2)
        
        # Add asymmetric periodic terms with varying frequencies
        for i in range(self.dim):
            f_val += 0.3 * np.sin(2 * np.pi * x_normalized[i]) * np.cos(4 * np.pi * x_normalized[i])
            f_val += 0.2 * np.sin(3 * np.pi * x_normalized[i])**2
        
        # Add saddle point structure through cross-terms
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction for sparsity
                f_val += 0.1 * (x_normalized[i]**2 - x_normalized[j]**2) * np.sin(np.pi * (x_normalized[i] + x_normalized[j]))
        
        # Add a global minimum at origin with penalty terms
        f_val += 0.05 * np.sum(np.abs(x_normalized)**4)
        
        # Introduce irregularity with non-smooth components
        f_val += 0.1 * np.sum(np.sin(10 * x_normalized) * np.cos(5 * x_normalized))
        
        return f_val