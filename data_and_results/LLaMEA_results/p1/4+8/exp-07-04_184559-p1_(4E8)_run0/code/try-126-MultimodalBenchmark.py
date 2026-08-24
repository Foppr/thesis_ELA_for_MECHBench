import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced radial component with multiple exponential decays, cosine modulations, and chaotic perturbations
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.sum(np.exp(-3 * r**2) * np.cos(5 * np.pi * r) * np.sin(2 * np.pi * r) * (1 + 0.2 * np.sin(17 * r)))
        
        # Coupled spiral terms in multiple dimensions for rotational complexity
        spiral = 0.0
        if self.dim >= 2:
            theta = np.arctan2(x_norm[1], x_norm[0])
            spiral = np.sin(6 * theta) * np.cos(5 * theta) + 0.5 * np.sin(12 * theta) + 0.3 * np.sin(23 * theta)
            
        # Adaptive frequency modulation based on dimensionality with chaotic component
        freq_mod = 1.0 + 0.3 * np.sin(np.pi * self.dim / 4.0) * np.cos(0.7 * self.dim)
        oscillation = np.sum(np.sin(freq_mod * 8 * x_norm) * np.cos(freq_mod * 6 * x_norm) * np.exp(-0.5 * np.sum(x_norm**2)))
        
        # Additional quadratic and quartic penalty terms with chaotic modulation
        penalty = 0.3 * np.sum(x_norm**2) + 0.1 * np.sum(x_norm**4) + 0.05 * np.sum(np.sin(11 * x_norm) * np.cos(9 * x_norm))
        
        # Cross-term interaction with chaotic and spiral components for increased complexity
        cross_term = 0.0
        if self.dim >= 2:
            for i in range(self.dim - 1):
                cross_term += x_norm[i] * x_norm[i+1] * np.sin(3 * np.pi * (x_norm[i] + x_norm[i+1])) * np.cos(7 * x_norm[i] * x_norm[i+1])
        
        # Add a chaotic logistic map component for further enhancement
        logistic = 0.0
        if self.dim >= 3:
            logistic = np.sum(np.sin(13 * x_norm[:-2]) * np.cos(11 * x_norm[1:]))
            
        # Combine all components with adjusted weights
        return radial + 1.5 * spiral + 0.8 * oscillation + penalty + 0.2 * cross_term + 0.15 * logistic