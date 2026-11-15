import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Shift input to center the global minimum at (1,1,...,1)
        x_shifted = x - 1.0
        
        # Scale input to [-1, 1] range
        x_scaled = x_shifted / 5.0
        
        # Quadratic term for conditioning
        quadratic = np.sum(x_scaled**2)
        
        # Enhanced multimodal component with nested sine waves
        sine_nested = np.sum(np.sin(3 * np.pi * x_scaled) * np.sin(9 * np.pi * x_scaled)**2)
        
        # Exponential decay with chaotic modulation
        exp_decay = np.sum(np.exp(-x_scaled**2) * np.sin(7 * np.pi * x_scaled)**2)
        
        # Additional cosine peaks with varying frequencies and weights
        cos_peaks = np.sum(np.cos(11 * np.pi * x_scaled) * np.exp(-0.5 * x_scaled**2) + 
                          0.5 * np.cos(5 * np.pi * x_scaled) * np.exp(-0.2 * x_scaled**2))
        
        # Cross-dimensional coupling with non-linear interaction
        cross_term = 0.15 * np.sum(np.sin(x_scaled[:-1] + x_scaled[1:]) * np.exp(-0.1 * (x_scaled[:-1]**2 + x_scaled[1:]**2)))
        
        # Chaotic component for increased complexity
        chaotic = 0.05 * np.sum(np.sin(13 * np.pi * x_scaled) * np.cos(17 * np.pi * x_scaled))
        
        # Combine all terms with adjusted weights
        return quadratic + 0.7 * sine_nested + 0.5 * exp_decay + 0.3 * cos_peaks + cross_term + chaotic