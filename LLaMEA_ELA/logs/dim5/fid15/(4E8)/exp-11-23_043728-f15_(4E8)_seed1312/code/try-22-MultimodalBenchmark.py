import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Base quadratic term for global attraction
        quadratic_term = np.sum(x_norm**2)
        
        # Multiple sinusoidal oscillations with varying frequencies and amplitudes
        sin_term = np.sum(np.sin(10 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm)**2)
        
        # Chaotic interference term using a modified logistic map-like function
        chaotic_term = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            chaotic_term += np.sin(7 * xi**3 + 2 * np.sin(5 * xi)) * np.cos(4 * xi**2)
        
        # Polynomial penalty with mixed exponents to create rugged terrain
        poly_term = np.sum(x_norm**8) + 0.5 * np.sum(x_norm**10) + 0.1 * np.sum(np.abs(x_norm)**12)
        
        # Dynamic scaling factor that varies with dimensionality
        scale_factor = 1.0 + 0.1 * np.sin(self.dim * 0.5)
        
        # Combine all terms with adaptive weights
        return scale_factor * (quadratic_term + 0.3 * sin_term + 0.02 * chaotic_term + 0.005 * poly_term)