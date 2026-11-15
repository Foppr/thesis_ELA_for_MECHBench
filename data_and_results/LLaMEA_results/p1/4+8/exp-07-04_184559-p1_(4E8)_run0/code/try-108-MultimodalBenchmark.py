import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced radial component with multiple exponential decays and cosine modulations
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.sum(np.exp(-2.5 * r**2) * np.cos(6 * np.pi * r) * np.sin(2.5 * np.pi * r))
        
        # Modified sinusoidal spiral with adaptive frequency based on dimensionality
        spiral = 0.0
        if self.dim >= 2:
            theta = np.arctan2(x_norm[1], x_norm[0])
            # Adaptive frequency based on dimension
            freq = 3.5 + 0.3 * np.sin(np.pi * (self.dim / 8.0))
            spiral = np.sin(freq * theta) * np.cos(freq * theta * 0.6)
        
        # Multi-frequency oscillation with varying amplitudes
        oscillation = 0.0
        for i in range(min(self.dim, 5)):
            freq = 7 + 2.5 * i
            oscillation += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i] * 0.4)
        
        # Additional quadratic penalty with dimension-dependent scaling
        penalty = 0.35 * np.sum(x_norm**2) + 0.12 * np.sum(x_norm**4)
        
        # Add a global sinusoidal modulation to increase complexity
        global_mod = np.sin(0.4 * np.sum(x_norm**2))
        
        # Add chaotic modulation component
        chaotic = 0.0
        for i in range(min(self.dim, 4)):
            chaotic += np.sin(10 * x_norm[i] + np.sin(7 * x_norm[i])) * 0.1
        
        # Shifted radial component for increased complexity
        shifted_radial = np.sum(np.exp(-3.2 * (r - 0.3)**2) * np.cos(4.5 * np.pi * (r - 0.2)))
        
        # Combine all components with adjusted weights
        return 1.6 * radial + 1.3 * spiral + 0.9 * oscillation + penalty + 0.6 * global_mod + 0.2 * chaotic + 0.3 * shifted_radial