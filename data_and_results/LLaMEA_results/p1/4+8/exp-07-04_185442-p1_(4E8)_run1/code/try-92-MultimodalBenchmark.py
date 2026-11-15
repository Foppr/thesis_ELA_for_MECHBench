import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced sinusoidal frequency interactions with multiple harmonics
        sin_freq = np.sum(np.sin(6 * x_norm) * np.cos(8 * x_norm)) + \
                   0.8 * np.sum(np.sin(10 * x_norm) * np.cos(12 * x_norm)) + \
                   0.6 * np.sum(np.sin(14 * x_norm) * np.cos(16 * x_norm))
        
        # Modified polynomial cross-terms with higher degree interactions
        poly_cross = np.sum((x_norm[0] * x_norm[1])**5) + \
                     0.4 * np.sum(x_norm**7 * np.sin(5 * np.pi * x_norm)) + \
                     0.3 * np.sum(x_norm**3 * np.cos(3 * np.pi * x_norm))
        
        # Adaptive conditioning with exponential decay and dimensionality scaling
        conditioning = np.sum((x_norm**2) * np.exp(-0.3 * np.abs(x_norm))) + \
                       0.5 * np.sum(np.exp(-0.5 * x_norm**2) * np.sin(3 * np.pi * x_norm))
        
        # Mixed trigonometric-expponential terms for increased complexity
        mixed_terms = np.sum(np.exp(-0.2 * x_norm**2) * np.sin(7 * np.pi * x_norm)) + \
                      0.7 * np.sum(np.exp(-0.1 * x_norm**2) * np.cos(9 * np.pi * x_norm))
        
        # Additional non-separable structure with coupled polynomial and trigonometric components
        coupled_structure = 0.3 * np.sum((x_norm[0] + x_norm[1])**6 * np.sin(4 * np.pi * (x_norm[0] - x_norm[1])))
        
        # Add structured noise to improve discrimination
        noise = 0.015 * np.random.random()
        
        # Combine all terms to create a highly multimodal and challenging landscape
        return sin_freq + poly_cross + conditioning + mixed_terms + coupled_structure + noise