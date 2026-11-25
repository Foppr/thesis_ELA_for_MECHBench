import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Multiple chaotic sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            result += 0.3 * np.sin(13 * x[i]) * np.cos(9 * x[i]) * np.sin(5 * x[i])
            
        # Multiple global minimum clusters with different offsets
        cluster_offsets = [0.0, 1.2, -1.8, 2.5, -2.1]
        for offset in cluster_offsets:
            result += 0.05 * np.sum((x - offset)**6)
            
        # High-order polynomial penalties with shifted roots
        for i in range(self.dim):
            result += 0.01 * (x[i] - 3.0)**8 + 0.005 * (x[i] + 3.0)**10
            
        # Complex cross-dimensional interactions with chaotic coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited range for complexity
                result += 0.04 * np.sin(3 * x[i] + 2 * x[j]) * np.cos(4 * x[i] - x[j])
                
        # Add a chaotic component that depends on all dimensions
        result += 0.1 * np.sin(np.sum(x) * 7) * np.cos(np.prod(x) * 3)
        
        # Additional noise-like perturbations for increased complexity
        for i in range(self.dim):
            result += 0.002 * np.sin(50 * x[i]) * np.cos(30 * x[i])
            
        return result