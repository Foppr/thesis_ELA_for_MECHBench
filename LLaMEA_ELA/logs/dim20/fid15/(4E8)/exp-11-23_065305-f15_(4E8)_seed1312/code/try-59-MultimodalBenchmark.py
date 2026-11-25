import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Polynomial base with varying exponents
        term1 = np.sum(x_norm**4)
        
        # Sinusoidal components with frequency modulation
        frequencies = np.arange(1, self.dim + 1)
        term2 = np.sum(np.sin(frequencies * np.pi * x_norm) * np.cos(frequencies * 0.5 * np.pi * x_norm))
        
        # Logarithmic barrier terms to create complex terrain
        log_terms = np.log(np.abs(x_norm) + 1e-8)
        term3 = np.sum(log_terms**2)
        
        # Asymmetric cross-dimensional interactions
        cross_interaction = 0
        for i in range(self.dim - 1):
            if i % 2 == 0:
                cross_interaction += x_norm[i] * (x_norm[i + 1]**3) * np.sin(3 * np.pi * x_norm[i])
            else:
                cross_interaction += (x_norm[i]**2) * x_norm[i + 1] * np.cos(2 * np.pi * x_norm[i + 1])
        term4 = 0.5 * cross_interaction
        
        # Chaotic exponential modulation with non-uniform shifts
        shifts = np.linspace(0.1, 0.9, self.dim)
        term5 = np.sum(np.exp(-x_norm**2) * np.sin(10 * np.pi * (x_norm + shifts)))
        
        # Non-uniform global minimum shift with higher-order polynomial
        shift_point = np.array([0.3, -0.4, 0.1] + [0.0] * (self.dim - 3))
        term6 = np.sum((x_norm - shift_point)**6)
        
        # Multi-scale trigonometric interference
        interference = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interference += np.sin(4 * np.pi * x_norm[i]) * np.cos(7 * np.pi * x_norm[j])
        term7 = 0.3 * interference
        
        # Combined result with adaptive scaling
        result = 0.8 * term1 + 0.6 * term2 + 0.4 * term3 + 0.5 * term4 + 0.7 * term5 + 0.9 * term6 + 0.5 * term7
        
        return result