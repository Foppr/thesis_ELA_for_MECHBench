import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basis function component with adaptive width
        f1 = np.sum(np.exp(-np.sum((x_norm[:, np.newaxis] - x_norm[np.newaxis, :])**2, axis=2)) * 
                    np.cos(2 * np.pi * np.sum((x_norm[:, np.newaxis] - x_norm[np.newaxis, :])**2, axis=2)))
        
        # Periodic modulation with varying frequencies
        f2 = np.sum(np.cos(10 * np.pi * x_norm) * np.sin(5 * np.pi * x_norm)**2)
        
        # Saddle-point inducing cross-terms
        f3 = np.sum(x_norm[:-1] * x_norm[1:] * np.sin(np.pi * (x_norm[:-1] + x_norm[1:])**2))
        
        # Adaptive polynomial coupling with mixed exponents
        f4 = np.sum((x_norm**3 + 0.5 * x_norm**5 + 0.1 * x_norm**7) * 
                    np.cos(3 * np.pi * x_norm)**2)
        
        # Chaotic interference pattern using logistic map modulation
        logistic_map = np.array([0.5])
        for _ in range(self.dim):
            logistic_map = np.append(logistic_map, 4 * logistic_map[-1] * (1 - logistic_map[-1]))
        f5 = np.sum(np.sin(logistic_map[1:self.dim+1] * x_norm)**2)
        
        # Combined fitness with optimized weights
        return 0.5 * f1 + 0.3 * f2 + 0.2 * f3 + 0.1 * f4 + 0.15 * f5