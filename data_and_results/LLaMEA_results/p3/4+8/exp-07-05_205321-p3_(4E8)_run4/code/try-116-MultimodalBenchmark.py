import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal-like radial component with nested exponential decay and multiple harmonic frequencies
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.exp(-r**3.0) * (1.0 + 0.5 * np.sin(15 * r) + 0.3 * np.cos(12 * r) + 0.2 * np.sin(20 * r**2))
        
        # Angular components with nested periodicity and dimensionally coupled interactions
        angular = 0.0
        for i in range(self.dim):
            angular += np.sin((i + 1) * np.pi * x_norm[i]) * np.cos((i + 1) * np.pi * x_norm[i])
            if i > 0:
                angular += 0.2 * np.sin(5 * np.pi * x_norm[i-1]) * np.sin(5 * np.pi * x_norm[i])
                angular += 0.1 * np.cos(4 * np.pi * x_norm[i-1]) * np.cos(4 * np.pi * x_norm[i])
        
        # Multi-scale periodic term with varying amplitudes and phases
        periodic = 0.0
        for i in range(self.dim):
            periodic += np.sin(8 * np.pi * x_norm[i] + 0.5 * np.sin(3 * np.pi * x_norm[i])) * \
                       np.cos(6 * np.pi * x_norm[i] - 0.4 * np.cos(2 * np.pi * x_norm[i]))
        
        # Cross-term interactions with fractal-like scaling and chaotic modulation
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.1 * np.sin(10 * np.pi * x_norm[i] + 0.3 * np.sin(7 * np.pi * x_norm[j])) * \
                             np.cos(9 * np.pi * x_norm[j] + 0.2 * np.cos(6 * np.pi * x_norm[i]))
        
        # Chaotic component with fractional exponents and nested sinusoidal modulations
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(9 * np.pi * x_norm[i]**2.5) * np.cos(11 * np.pi * x_norm[i]**1.7) + \
                      0.1 * np.sin(13 * np.pi * x_norm[i]**3.2) * np.cos(14 * np.pi * x_norm[i]**2.8)
        
        # Additional nested harmonic term with varying frequency ratios
        nested = 0.0
        for i in range(self.dim):
            nested += 0.05 * np.sin(25 * np.pi * x_norm[i]) * np.cos(22 * np.pi * x_norm[i]) * \
                     np.sin(18 * np.pi * x_norm[i]**2)
        
        # Combine all components with adjusted weights
        return 0.25 * radial + 0.25 * angular + 0.2 * periodic + 0.15 * cross_term + 0.1 * chaotic + 0.05 * nested + 1.0