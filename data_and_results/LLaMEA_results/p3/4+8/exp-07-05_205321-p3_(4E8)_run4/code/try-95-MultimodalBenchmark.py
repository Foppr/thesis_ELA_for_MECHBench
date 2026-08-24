import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with modified exponential decay and harmonic modulation
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.exp(-r**2.1) * (1.0 + 0.5 * np.sin(11 * r) + 0.3 * np.cos(9 * r) + 0.15 * np.sin(13 * r))
        
        # Angular components with increased frequency and interaction terms
        angular = 0.0
        for i in range(self.dim):
            angular += np.sin((i + 2.0) * np.pi * x_norm[i]) * np.cos((i + 2.0) * np.pi * x_norm[i])
            if i > 0:
                angular += 0.15 * np.sin(3.0 * np.pi * x_norm[i-1]) * np.sin(3.0 * np.pi * x_norm[i])
        
        # Additional multimodal term with shifted periodicity and amplitude
        periodic = np.sum(np.sin(5.0 * np.pi * x_norm + 0.7) * np.cos(4.0 * np.pi * x_norm - 0.5))
        
        # Cross-term interactions between dimensions with higher coupling strength
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.08 * np.sin(6.0 * np.pi * x_norm[i]) * np.cos(5.0 * np.pi * x_norm[j])
        
        # Add a new quartic polynomial component for increased complexity
        quartic = 0.05 * np.sum(x_norm**4)
        
        # Combine all components with adjusted weights
        return 0.25 * radial + 0.30 * angular + 0.25 * periodic + 0.10 * cross_term + 0.15 * quartic + 1.0