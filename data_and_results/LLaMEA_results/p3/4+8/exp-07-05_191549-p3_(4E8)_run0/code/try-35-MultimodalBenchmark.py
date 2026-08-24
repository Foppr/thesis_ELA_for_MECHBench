import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Adaptive polynomial conditioning with varying exponents
        poly_term = np.sum((x_scaled**8 - 4*x_scaled**6 + 6*x_scaled**4 - 4*x_scaled**2 + 1) * (1 + 0.5 * np.sin(10 * x_scaled)))
        
        # Chaotic sinusoidal interference with non-linear frequency modulation
        sin_term = np.sum(np.sin(30 * np.pi * x_scaled + np.sin(15 * np.pi * x_scaled)) * np.cos(20 * np.pi * x_scaled + np.cos(10 * np.pi * x_scaled)))
        
        # Exponential barrier with dynamic scaling
        exp_barrier = np.sum(np.exp(-10 * np.abs(x_scaled)) * (1 + 0.3 * np.sin(25 * np.pi * x_scaled)**2))
        
        # Cross-dimensional coupling with recursive interaction
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += x_scaled[i] * x_scaled[i+1] * np.sin(12 * np.pi * (x_scaled[i] + x_scaled[i+1])) * np.cos(6 * np.pi * (x_scaled[i] - x_scaled[i+1]))
        
        # Add a global modulation factor based on the norm of the input
        norm_factor = 1 + 0.2 * np.linalg.norm(x_scaled)**2
        
        # Combine all terms with dynamic weights
        return norm_factor * (0.35 * poly_term + 0.3 * sin_term + 0.25 * exp_barrier + 0.1 * cross_term)