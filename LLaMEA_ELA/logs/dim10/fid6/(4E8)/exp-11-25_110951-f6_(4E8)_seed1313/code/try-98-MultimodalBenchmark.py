import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Fractal-like component using recursive sine waves
        fractal_term = np.sum(np.sin(2 ** (self.dim + 1) * np.pi * x_normalized) * 
                              np.cos(2 ** self.dim * np.pi * x_normalized))
        
        # Directional bias term with varying orientation
        direction_bias = np.sum(x_normalized * np.sin(3 * np.pi * x_normalized))
        
        # Polynomial conditioning with exponential scaling
        poly_conditioning = np.sum((x_normalized ** 3) * np.exp(-0.5 * np.sum(x_normalized**2)))
        
        # Chaotic component using logistic map-inspired modulation
        chaotic_component = 0.5 * np.sum(
            np.sin(10 * np.pi * x_normalized) * 
            np.cos(8 * np.pi * x_normalized) * 
            np.sin(6 * np.pi * np.sqrt(np.sum(x_normalized**2)))
        )
        
        # Cross-dimensional coupling with asymmetric interaction
        cross_coupling = 0.3 * np.sum(
            (x_normalized[:-1] ** 2) * 
            np.cos(5 * np.pi * x_normalized[1:]) * 
            np.sin(4 * np.pi * x_normalized[:-1])
        )
        
        # Scale-invariant noise term
        noise_term = 0.1 * np.sum(np.random.uniform(-1, 1, self.dim) * np.sin(15 * np.pi * x_normalized))
        
        # Global scaling factor based on dimensionality
        scale_factor = 1.0 + 0.1 * (self.dim - 1) + 0.02 * np.cos(self.dim)
        
        # Combine all components
        return scale_factor * (fractal_term + direction_bias + poly_conditioning + chaotic_component + cross_coupling + noise_term)