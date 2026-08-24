import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced radial component with multiple exponential decays, cosine modulations, and chaotic perturbations
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.sum(np.exp(-2 * r**2) * np.cos(7 * np.pi * r) * np.sin(3 * np.pi * r) * (1 + 0.3 * np.sin(19 * r)))
        
        # Coupled spiral terms in multiple dimensions for rotational complexity
        spiral = 0.0
        if self.dim >= 2:
            theta = np.arctan2(x_norm[1], x_norm[0])
            spiral = np.sin(7 * theta) * np.cos(6 * theta) + 0.6 * np.sin(13 * theta) + 0.4 * np.sin(25 * theta)
            
        # Adaptive frequency modulation based on dimensionality with chaotic component
        freq_mod = 1.0 + 0.4 * np.sin(np.pi * self.dim / 5.0) * np.cos(0.8 * self.dim)
        oscillation = np.sum(np.sin(freq_mod * 9 * x_norm) * np.cos(freq_mod * 7 * x_norm) * np.exp(-0.4 * np.sum(x_norm**2)))
        
        # Additional quadratic and quartic penalty terms with chaotic modulation
        penalty = 0.4 * np.sum(x_norm**2) + 0.15 * np.sum(x_norm**4) + 0.08 * np.sum(np.sin(13 * x_norm) * np.cos(10 * x_norm))
        
        # Cross-term interaction with chaotic and spiral components for increased complexity
        cross_term = 0.0
        if self.dim >= 2:
            for i in range(self.dim - 1):
                cross_term += x_norm[i] * x_norm[i+1] * np.sin(4 * np.pi * (x_norm[i] + x_norm[i+1])) * np.cos(8 * x_norm[i] * x_norm[i+1])
        
        # Add a chaotic logistic map component for further enhancement
        logistic = 0.0
        if self.dim >= 3:
            logistic = np.sum(np.sin(15 * x_norm[:-2]) * np.cos(13 * x_norm[1:]))
            
        # Add higher-order polynomial interactions for increased complexity
        poly_interaction = 0.05 * np.sum(x_norm**6) + 0.03 * np.sum(x_norm**8)
        
        # Combine all components with adjusted weights
        return radial + 1.8 * spiral + 0.9 * oscillation + penalty + 0.25 * cross_term + 0.2 * logistic + poly_interaction