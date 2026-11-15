import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with modified exponential decay and harmonic modulation
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.exp(-r**1.5) * (1.0 + 0.3 * np.sin(8 * r) + 0.2 * np.cos(6 * r))
        
        # Angular components with increased frequency and interaction terms
        angular = 0.0
        for i in range(self.dim):
            angular += np.sin((i + 1) * np.pi * x_norm[i]) * np.cos((i + 1) * np.pi * x_norm[i])
            if i > 0:
                angular += 0.1 * np.sin(2 * np.pi * x_norm[i-1]) * np.sin(2 * np.pi * x_norm[i])
        
        # Additional multimodal term with shifted periodicity and amplitude
        periodic = np.sum(np.sin(4 * np.pi * x_norm + 0.5) * np.cos(3 * np.pi * x_norm - 0.3))
        
        # Cross-term interactions between dimensions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.05 * np.sin(5 * np.pi * x_norm[i]) * np.cos(4 * np.pi * x_norm[j])
        
        # Add a small perturbation to increase complexity
        perturbation = 0.02 * np.sin(10 * r) * np.cos(7 * r)
        
        # Combine all components with adjusted weights
        return 0.25 * radial + 0.35 * angular + 0.3 * periodic + 0.1 * cross_term + perturbation + 1.0