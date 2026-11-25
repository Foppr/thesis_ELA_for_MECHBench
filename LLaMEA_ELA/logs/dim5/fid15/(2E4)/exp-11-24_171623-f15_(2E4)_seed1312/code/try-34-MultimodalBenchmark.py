import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial term with mixed degrees and interaction
        poly_term = np.sum(x_norm**4 + 0.5 * x_norm**3 - 0.3 * x_norm**2 + 0.1 * x_norm)
        
        # Sinusoidal component with multiple frequencies and phase shifts
        sin_term = np.sum(np.sin(2 * np.pi * x_norm) + 
                         0.5 * np.sin(4 * np.pi * x_norm) + 
                         0.3 * np.sin(6 * np.pi * x_norm))
        
        # Radial basis function with adaptive width
        rbf_term = 0
        for i in range(self.dim):
            rbf_term += np.exp(-2.0 * (x_norm[i] - 0.5)**2) + \
                       0.5 * np.exp(-1.5 * (x_norm[i] + 0.3)**2)
        
        # Cross-dimensional interaction with variable coupling strength
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                cross_term += (x_norm[i] * x_norm[i+1]) * \
                             np.sin(3 * np.pi * (x_norm[i] + x_norm[i+1]))
        
        # Adaptive dimension weighting based on position
        weight = 1.0 + 0.2 * np.sum(np.abs(x_norm))
        
        # Combine all terms with dynamic scaling
        result = weight * (0.3 * poly_term + 0.4 * sin_term + 
                          0.2 * rbf_term + 0.1 * cross_term)
        
        return result