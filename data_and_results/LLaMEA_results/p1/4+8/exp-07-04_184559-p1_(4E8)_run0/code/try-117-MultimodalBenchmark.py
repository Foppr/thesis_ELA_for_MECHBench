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
        
        # Modified sinusoidal spiral with adaptive frequency based on dimensionality
        spiral = 0.0
        if self.dim >= 2:
            theta = np.arctan2(x_norm[1], x_norm[0])
            # Adaptive frequency based on dimension
            freq = 4 + 0.7 * np.sin(np.pi * (self.dim / 8.0))
            spiral = np.sin(freq * theta) * np.cos(freq * theta * 0.6)
        
        # Multi-frequency oscillation with varying amplitudes and chaotic modulation
        oscillation = 0.0
        for i in range(min(self.dim, 6)):
            freq = 6 + 1.5 * i
            # Add chaotic modulation to frequency
            chaotic_factor = 1 + 0.3 * np.sin(10 * x_norm[i])
            oscillation += np.sin(chaoic_factor * freq * x_norm[i]) * np.cos(chaoic_factor * freq * x_norm[i] * 0.4)
        
        # Additional quadratic penalty with dimension-dependent scaling and chaotic component
        penalty = 0.4 * np.sum(x_norm**2) + 0.15 * np.sum(x_norm**4) + 0.05 * np.sum(np.sin(10 * x_norm))
        
        # Add a global sinusoidal modulation to increase complexity
        global_mod = np.sin(0.3 * np.sum(x_norm**2))
        
        # Add novel chaotic cross-terms between dimensions
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += np.sin(5 * x_norm[i] * x_norm[j]) * np.cos(3 * x_norm[i] + 2 * x_norm[j])
        
        # Combine all components with adjusted weights
        return 1.3 * radial + 1.1 * spiral + 0.9 * oscillation + penalty + 0.6 * global_mod + 0.4 * cross_terms