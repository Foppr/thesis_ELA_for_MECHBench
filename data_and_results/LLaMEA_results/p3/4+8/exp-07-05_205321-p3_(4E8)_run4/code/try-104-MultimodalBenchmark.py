import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced radial component with double exponential decay and nested harmonics
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.exp(-r**2.0) * (1.0 + 0.5 * np.sin(12 * r) + 0.3 * np.cos(9 * r) + 0.15 * np.sin(15 * r**2))
        
        # Angular components with nested frequency modulation and coupling
        angular = 0.0
        for i in range(self.dim):
            angular += np.sin((i + 1) * np.pi * x_norm[i]) * np.cos((i + 1) * np.pi * x_norm[i])
            angular += 0.2 * np.sin(2 * (i + 1) * np.pi * x_norm[i]) * np.cos(3 * (i + 1) * np.pi * x_norm[i])
            if i > 0:
                angular += 0.1 * np.sin(4 * np.pi * x_norm[i-1]) * np.sin(5 * np.pi * x_norm[i])
                angular += 0.08 * np.cos(6 * np.pi * x_norm[i-1]) * np.cos(7 * np.pi * x_norm[i])
        
        # Complex periodic term with multi-scale modulation and phase shifts
        periodic = np.sum(np.sin(6 * np.pi * x_norm + 0.7) * np.cos(5 * np.pi * x_norm - 0.5) + 
                         0.5 * np.sin(8 * np.pi * x_norm + 0.3) * np.cos(9 * np.pi * x_norm - 0.2))
        
        # Cross-term interactions with non-linear coupling and higher-order terms
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.1 * np.sin(7 * np.pi * x_norm[i]) * np.cos(6 * np.pi * x_norm[j]) * np.sin(3 * np.pi * x_norm[i] * x_norm[j])
                cross_term += 0.05 * np.cos(8 * np.pi * x_norm[i]) * np.sin(9 * np.pi * x_norm[j]) * np.cos(4 * np.pi * x_norm[i] * x_norm[j])
        
        # Chaotic component with fractional powers and nested sinusoids
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(8 * np.pi * x_norm[i]**2.5) * np.cos(9 * np.pi * x_norm[i]**1.7) + \
                      0.3 * np.sin(10 * np.pi * x_norm[i]**3) * np.cos(11 * np.pi * x_norm[i]**2)
        
        # Additional skewness term with asymmetric harmonic modulation
        skewness = 0.0
        for i in range(self.dim):
            skewness += 0.15 * np.sin(5 * np.pi * x_norm[i]**3) * np.cos(4 * np.pi * x_norm[i]**2) * np.sin(2 * np.pi * x_norm[i])
        
        # Combine all components with adjusted weights and add a constant offset
        return 0.25 * radial + 0.25 * angular + 0.2 * periodic + 0.15 * cross_term + 0.1 * chaotic + 0.05 * skewness + 1.0