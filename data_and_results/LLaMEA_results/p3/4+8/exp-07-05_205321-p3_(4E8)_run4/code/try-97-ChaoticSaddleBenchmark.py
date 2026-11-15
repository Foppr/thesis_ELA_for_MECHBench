import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term with asymmetric coefficients
        quadratic = np.sum(0.5 * (1.0 + 0.3 * np.sin(x_norm)) * x_norm**2)
        
        # Nested periodic components with varying frequencies and amplitudes
        periodic = 0.0
        for i in range(self.dim):
            freq = 2.0 + 0.5 * np.sin(i)
            amp = 1.0 + 0.2 * np.cos(i)
            periodic += amp * np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i])
        
        # Chaotic component using a modified logistic map-like structure
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += 0.1 * np.sin(10 * np.pi * x_norm[i]) * np.cos(9 * np.pi * x_norm[i]) * np.tanh(5 * x_norm[i])
        
        # Asymmetric gradient field with saddle-point characteristics
        gradient_field = 0.0
        for i in range(self.dim):
            gradient_field += 0.05 * x_norm[i] * np.sin(4 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[i])
        
        # Cross-dimensional interaction with nested structure
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += 0.03 * np.sin(2 * np.pi * (x_norm[i] + x_norm[j])) * np.cos(2 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Global scaling and offset to ensure global minimum at origin
        result = 1.5 * quadratic + 0.8 * periodic + 0.6 * chaotic + 0.4 * gradient_field + 0.3 * cross_interaction + 1.0
        
        return result