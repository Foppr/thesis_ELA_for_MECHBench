import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with modified exponential decay and harmonic modulation
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.exp(-r**1.7) * (1.0 + 0.4 * np.sin(9 * r) + 0.25 * np.cos(7 * r))
        
        # Angular components with increased frequency and interaction terms
        angular = 0.0
        for i in range(self.dim):
            angular += np.sin((i + 1.5) * np.pi * x_norm[i]) * np.cos((i + 1.5) * np.pi * x_norm[i])
            if i > 0:
                angular += 0.12 * np.sin(2.5 * np.pi * x_norm[i-1]) * np.sin(2.5 * np.pi * x_norm[i])
        
        # Additional multimodal term with shifted periodicity and amplitude
        periodic = np.sum(np.sin(4.5 * np.pi * x_norm + 0.6) * np.cos(3.5 * np.pi * x_norm - 0.4))
        
        # Cross-term interactions between dimensions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.06 * np.sin(5.5 * np.pi * x_norm[i]) * np.cos(4.5 * np.pi * x_norm[j])
        
        # Combine all components with adjusted weights
        return 0.28 * radial + 0.32 * angular + 0.28 * periodic + 0.12 * cross_term + 1.0