import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sinusoidal interactions with varying frequencies and amplitudes
        chaotic_terms = np.sum(np.sin(13 * x_norm) * np.cos(17 * x_norm) * np.sin(19 * x_norm))
        
        # Higher-order polynomial cross-terms with exponential coupling
        poly_cross = np.sum((x_norm[0] * x_norm[1])**7) + \
                     0.3 * np.sum(x_norm**8 * np.cos(6 * np.pi * x_norm)) + \
                     0.1 * np.sum((x_norm**2 * x_norm[0])**5)
        
        # Dynamic conditioning with logarithmic scaling
        dynamic_cond = np.sum(np.log(1 + 0.5 * x_norm**2) * np.exp(-0.3 * np.abs(x_norm)))
        
        # Fractal-like noise with multiple scales
        fractal_noise = 0.05 * np.sum(np.sin(23 * x_norm) * np.cos(29 * x_norm) * np.sin(31 * x_norm))
        
        # Adaptive coupling between dimensions with trigonometric modulation
        coupling = np.sum(np.sin(3 * x_norm) * np.cos(5 * x_norm) * np.sin(7 * x_norm)) + \
                   0.8 * np.sum(np.cos(11 * x_norm) * np.sin(13 * x_norm) * np.cos(15 * x_norm))
        
        # Add a complex structured noise term
        structured_noise = 0.03 * np.random.random() * np.sum(np.sin(37 * x_norm))
        
        # Combine all terms to create a highly complex multimodal landscape
        return chaotic_terms + poly_cross + dynamic_cond + fractal_noise + coupling + structured_noise