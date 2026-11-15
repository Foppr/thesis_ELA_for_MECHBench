import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Hyperbolic tangent radial component with fractal-like scaling
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.tanh(r) * (1.0 + 0.3 * np.sin(15 * r) + 0.2 * np.cos(11 * r))
        
        # Angular component with hyperbolic tangent and cross-dimensional coupling
        angular = 0.0
        for i in range(self.dim):
            angular += np.tanh((i + 1) * x_norm[i]) * np.cos((i + 1) * x_norm[i])
            if i > 0:
                angular += 0.1 * np.tanh(3 * x_norm[i-1]) * np.sin(4 * x_norm[i])
        
        # Fractal-like periodic component with varying frequencies
        periodic = 0.0
        for i in range(self.dim):
            freq = 2**(i % 4 + 1)
            periodic += np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i])
        
        # Cross-dimensional interaction with chaotic scaling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling for complexity control
                cross_term += 0.05 * np.tanh(7 * x_norm[i]) * np.tanh(6 * x_norm[j])
        
        # Chaotic component with logistic map-inspired modulation
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += 0.08 * np.tanh(10 * x_norm[i]) * np.sin(9 * x_norm[i])
        
        # Combine all components with adjusted weights
        return 0.25 * radial + 0.3 * angular + 0.2 * periodic + 0.15 * cross_term + 0.1 * chaotic + 1.0