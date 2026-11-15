import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with modified exponential decay and harmonic modulation
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.exp(-r**2.0) * (1.0 + 0.4 * np.sin(10 * r) + 0.25 * np.cos(7 * r))
        
        # Angular components with increased frequency and interaction terms
        angular = 0.0
        for i in range(self.dim):
            angular += np.sin((i + 1) * np.pi * x_norm[i]) * np.cos((i + 1) * np.pi * x_norm[i])
            if i > 0:
                angular += 0.15 * np.sin(3 * np.pi * x_norm[i-1]) * np.sin(3 * np.pi * x_norm[i])
        
        # Additional multimodal term with shifted periodicity and amplitude
        periodic = np.sum(np.sin(5 * np.pi * x_norm + 0.6) * np.cos(4 * np.pi * x_norm - 0.4))
        
        # Cross-term interactions between dimensions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.07 * np.sin(6 * np.pi * x_norm[i]) * np.cos(5 * np.pi * x_norm[j])
        
        # Add a new chaotic component to increase complexity
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(12 * x_norm[i]) * np.cos(11 * x_norm[i]) * np.sin(9 * x_norm[i])
        
        # Combine all components with adjusted weights
        return 0.3 * radial + 0.3 * angular + 0.25 * periodic + 0.1 * cross_term + 0.05 * chaotic + 1.0