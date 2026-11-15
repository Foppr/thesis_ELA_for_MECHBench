import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced radial component with multiple exponential decays, cosine modulations, and chaotic perturbations
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.sum(np.exp(-2.5 * r**2) * np.cos(4 * np.pi * r) * np.sin(1.5 * np.pi * r) * (1 + 0.15 * np.sin(19 * r)))
        
        # Coupled spiral terms in multiple dimensions for rotational complexity
        spiral = 0.0
        if self.dim >= 2:
            theta = np.arctan2(x_norm[1], x_norm[0])
            spiral = np.sin(5 * theta) * np.cos(4 * theta) + 0.4 * np.sin(10 * theta) + 0.25 * np.sin(20 * theta)
            
        # Adaptive frequency modulation based on dimensionality with chaotic component
        freq_mod = 1.0 + 0.25 * np.sin(np.pi * self.dim / 4.0) * np.cos(0.6 * self.dim)
        oscillation = np.sum(np.sin(freq_mod * 7 * x_norm) * np.cos(freq_mod * 5 * x_norm) * np.exp(-0.4 * np.sum(x_norm**2)))
        
        # Additional quadratic and quartic penalty terms with chaotic modulation
        penalty = 0.25 * np.sum(x_norm**2) + 0.08 * np.sum(x_norm**4) + 0.04 * np.sum(np.sin(10 * x_norm) * np.cos(8 * x_norm))
        
        # Cross-term interaction with chaotic and spiral components for increased complexity
        cross_term = 0.0
        if self.dim >= 2:
            for i in range(self.dim - 1):
                cross_term += x_norm[i] * x_norm[i+1] * np.sin(2.5 * np.pi * (x_norm[i] + x_norm[i+1])) * np.cos(6 * x_norm[i] * x_norm[i+1])
        
        # Add a chaotic logistic map component for further enhancement
        logistic = 0.0
        if self.dim >= 3:
            logistic = np.sum(np.sin(12 * x_norm[:-2]) * np.cos(10 * x_norm[1:]))
            
        # New dynamic phase shift component to increase landscape complexity
        phase_shift = np.sum(np.sin(1.5 * np.pi * x_norm) * np.cos(2.5 * np.pi * x_norm) * np.exp(-0.25 * np.sum(x_norm**2)))
        
        # Higher-order polynomial interactions for increased multimodality
        poly_interaction = 0.04 * np.sum(x_norm**6) + 0.025 * np.sum(x_norm**8) + 0.015 * np.sum(x_norm**10)
        
        # Additional sinusoidal modulation with varying frequencies based on dimension
        sin_mod = np.sum(np.sin(14 * x_norm) * np.cos(12 * x_norm) * np.sin(10 * x_norm))
        
        # Combine all components with adjusted weights
        return radial + 1.4 * spiral + 0.7 * oscillation + penalty + 0.18 * cross_term + 0.13 * logistic + 0.22 * phase_shift + 0.09 * poly_interaction + 0.04 * sin_mod