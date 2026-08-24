import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal-like radial component with nested harmonic modulations
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.exp(-r**3.0) * (1.0 + 0.5 * np.sin(15 * r) + 0.3 * np.cos(12 * r) + 0.15 * np.sin(25 * r**2))
        
        # Angular components with nested frequencies and coupling
        angular = 0.0
        for i in range(self.dim):
            angular += np.sin((i + 1) * np.pi * x_norm[i]) * np.cos((i + 1) * np.pi * x_norm[i])
            angular += 0.2 * np.sin(3 * (i + 1) * np.pi * x_norm[i]) * np.cos(4 * (i + 1) * np.pi * x_norm[i])
            if i > 0:
                angular += 0.1 * np.sin(5 * np.pi * x_norm[i-1]) * np.sin(7 * np.pi * x_norm[i])
                angular += 0.08 * np.cos(6 * np.pi * x_norm[i-1]) * np.cos(8 * np.pi * x_norm[i])
        
        # Multi-scale periodic term with fractal characteristics
        periodic = 0.0
        for i in range(self.dim):
            periodic += np.sin(8 * np.pi * x_norm[i] + 0.7) * np.cos(6 * np.pi * x_norm[i] - 0.5)
            periodic += 0.25 * np.sin(12 * np.pi * x_norm[i] + 0.3) * np.cos(10 * np.pi * x_norm[i] - 0.2)
        
        # Cross-term interactions with chaotic coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.1 * np.sin(8 * np.pi * x_norm[i]) * np.cos(7 * np.pi * x_norm[j])
                cross_term += 0.05 * np.sin(10 * np.pi * x_norm[i]**2) * np.cos(9 * np.pi * x_norm[j]**2)
        
        # Chaotic component with nested non-linear transformations
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(9 * np.pi * x_norm[i]**3) * np.cos(11 * np.pi * x_norm[i]**2)
            chaotic += 0.15 * np.sin(13 * np.pi * x_norm[i]**4) * np.cos(15 * np.pi * x_norm[i]**3)
        
        # Additional nested harmonic term for increased complexity
        nested = 0.0
        for i in range(self.dim):
            nested += 0.05 * np.sin(20 * np.pi * x_norm[i]) * np.cos(18 * np.pi * x_norm[i])
            nested += 0.03 * np.sin(25 * np.pi * x_norm[i]**2) * np.cos(22 * np.pi * x_norm[i]**2)
        
        # Combine all components with adjusted weights
        return 0.25 * radial + 0.3 * angular + 0.2 * periodic + 0.15 * cross_term + 0.08 * chaotic + 0.02 * nested + 1.0