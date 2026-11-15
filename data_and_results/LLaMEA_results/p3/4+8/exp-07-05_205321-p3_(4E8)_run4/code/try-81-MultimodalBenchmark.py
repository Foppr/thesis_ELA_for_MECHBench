import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with modified exponential decay and harmonic modulation
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.exp(-r**2.0) * (1.0 + 0.5 * np.sin(12 * r) + 0.3 * np.cos(8 * r))
        
        # Angular components with increased frequency and interaction terms
        angular = 0.0
        for i in range(self.dim):
            angular += np.sin((i + 1) * np.pi * x_norm[i]) * np.cos((i + 1) * np.pi * x_norm[i])
            if i > 0:
                angular += 0.2 * np.sin(4 * np.pi * x_norm[i-1]) * np.sin(4 * np.pi * x_norm[i])
        
        # Additional multimodal term with shifted periodicity and amplitude
        periodic = np.sum(np.sin(6 * np.pi * x_norm + 0.7) * np.cos(5 * np.pi * x_norm - 0.3))
        
        # Cross-term interactions between dimensions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.1 * np.sin(7 * np.pi * x_norm[i]) * np.cos(6 * np.pi * x_norm[j])
        
        # Additional chaotic component to increase complexity
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += 0.12 * np.sin(13 * np.pi * x_norm[i]) * np.cos(12 * np.pi * x_norm[i])
        
        # Combine all components with adjusted weights
        return 0.35 * radial + 0.25 * angular + 0.2 * periodic + 0.12 * cross_term + 0.08 * chaotic + 1.0