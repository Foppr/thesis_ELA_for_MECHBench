import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced radial component with chaotic exponential modulation and fractal-like structure
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.exp(-r**3.0) * (1.0 + 0.5 * np.sin(15 * r) + 0.3 * np.cos(11 * r) + 0.1 * np.sin(23 * r**1.5))
        
        # Angular components with nested harmonic interactions and fractal coupling
        angular = 0.0
        for i in range(self.dim):
            angular += np.sin((i + 1) * np.pi * x_norm[i]) * np.cos((i + 1) * np.pi * x_norm[i])
            if i > 0:
                angular += 0.2 * np.sin(5 * np.pi * x_norm[i-1]) * np.sin(5 * np.pi * x_norm[i])
                angular += 0.1 * np.cos(7 * np.pi * x_norm[i-1]) * np.cos(7 * np.pi * x_norm[i])
        
        # Nested periodic term with multi-scale fractal characteristics
        periodic = 0.0
        for i in range(self.dim):
            periodic += np.sin(7 * np.pi * x_norm[i] + 0.5 * np.sin(13 * np.pi * x_norm[i])) * \
                       np.cos(6 * np.pi * x_norm[i] - 0.4 * np.cos(11 * np.pi * x_norm[i]))
        
        # Cross-term interactions with fractal coupling and chaotic modulation
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.1 * np.sin(8 * np.pi * x_norm[i]) * np.cos(7 * np.pi * x_norm[j]) * \
                             np.sin(3 * np.pi * (x_norm[i] + x_norm[j])**2)
        
        # Chaotic component with nested sine-cosine fractal structure
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(9 * np.pi * x_norm[i]**3) * np.cos(10 * np.pi * x_norm[i]**2) * \
                      np.sin(4 * np.pi * x_norm[i]**1.7)
        
        # Additional fractal-like term with self-similar harmonic structure
        fractal = 0.0
        for i in range(self.dim):
            fractal += 0.05 * np.sin(12 * np.pi * x_norm[i] + 0.3 * np.sin(20 * np.pi * x_norm[i])) * \
                      np.cos(14 * np.pi * x_norm[i] - 0.2 * np.cos(18 * np.pi * x_norm[i]))
        
        # Combine all components with adjusted weights
        return 0.25 * radial + 0.25 * angular + 0.2 * periodic + 0.15 * cross_term + 0.1 * chaotic + 0.05 * fractal + 1.0