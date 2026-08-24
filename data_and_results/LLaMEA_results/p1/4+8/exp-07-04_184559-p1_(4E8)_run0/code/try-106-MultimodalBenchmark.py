import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced radial component with multiple exponential decays and cosine modulations
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.sum(np.exp(-2 * r**2) * np.cos(4 * np.pi * r) * np.sin(3 * np.pi * r))
        
        # Coupled spiral terms in multiple dimensions for rotational complexity
        spiral = 0.0
        if self.dim >= 2:
            theta = np.arctan2(x_norm[1], x_norm[0])
            spiral = np.sin(7 * theta) * np.cos(6 * theta) + 0.4 * np.sin(14 * theta)
            
        # Adaptive frequency modulation based on dimensionality
        freq_mod = 1.0 + 0.4 * np.sin(np.pi * self.dim / 5.0)
        oscillation = np.sum(np.sin(freq_mod * 9 * x_norm) * np.cos(freq_mod * 7 * x_norm))
        
        # Additional quadratic and quartic penalty terms for better conditioning
        penalty = 0.2 * np.sum(x_norm**2) + 0.15 * np.sum(x_norm**4)
        
        # Cross-term interaction for increased complexity
        if self.dim >= 2:
            cross_term = np.sum(x_norm[:-1] * x_norm[1:] * np.sin(4 * np.pi * (x_norm[:-1] + x_norm[1:])))
        else:
            cross_term = 0.0
            
        # Additional high-frequency oscillation component for increased complexity
        high_freq = np.sum(np.sin(15 * x_norm) * np.cos(13 * x_norm))
        
        # Combine all components with adjusted weights
        return radial + 1.2 * spiral + 0.9 * oscillation + penalty + 0.3 * cross_term + 0.1 * high_freq