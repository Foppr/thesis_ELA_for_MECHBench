import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced radial component with logistic chaos and sine modulation
        r = np.sqrt(np.sum(x_norm**2))
        # Add chaotic logistic map component
        chaos = 0.0
        if self.dim >= 2:
            # Simple chaotic component using logistic map-like behavior
            x0 = x_norm[0] if x_norm[0] != 0 else 1e-6
            chaos = np.sin(10 * np.pi * x0) * np.exp(-r**2)
        
        radial = np.sum(np.exp(-3 * r**2) * np.sin(5 * np.pi * r) * np.cos(2 * np.pi * r) + chaos)
        
        # Modified sinusoidal spiral with adaptive frequency based on dimensionality
        spiral = 0.0
        if self.dim >= 2:
            theta = np.arctan2(x_norm[1], x_norm[0])
            # Adaptive frequency based on dimension
            freq = 3 + 0.5 * np.sin(np.pi * (self.dim / 10.0))
            spiral = np.sin(freq * theta) * np.cos(freq * theta * 0.7)
        
        # Multi-frequency oscillation with varying amplitudes
        oscillation = 0.0
        for i in range(min(self.dim, 5)):
            freq = 8 + 2 * i
            oscillation += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i] * 0.5)
        
        # Additional quadratic penalty with dimension-dependent scaling
        penalty = 0.3 * np.sum(x_norm**2) + 0.1 * np.sum(x_norm**4)
        
        # Add a global sinusoidal modulation to increase complexity
        global_mod = np.sin(0.5 * np.sum(x_norm**2))
        
        # Combine all components with adjusted weights
        return 1.5 * radial + 1.2 * spiral + 0.8 * oscillation + penalty + 0.5 * global_mod