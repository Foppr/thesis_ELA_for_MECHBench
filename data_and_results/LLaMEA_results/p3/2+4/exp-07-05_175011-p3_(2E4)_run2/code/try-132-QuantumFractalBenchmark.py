import numpy as np

class QuantumFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quantum interference term with complex amplitude
        quantum = np.sum(np.sin(3 * x_norm) * np.cos(5 * x_norm) + 
                         np.sin(7 * x_norm) * np.cos(11 * x_norm))
        
        # Fractal-like self-similar structure with recursive scaling
        fractal = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x_norm[i] - x_norm[j])
                fractal += np.sin(10 * distance) * np.exp(-0.5 * distance**2) * np.cos(3 * distance)
        
        # Adaptive conditioning based on dimensionality
        conditioning = np.sum((1 + 0.1 * self.dim) * x_norm**4)
        
        # Multi-scale periodic components with varying wavelengths
        periodic = 0.0
        scales = np.arange(1, min(6, self.dim + 1))
        for scale in scales:
            periodic += np.sum(np.sin(scale * x_norm) * np.cos(scale * x_norm))
        
        # Entangled pair interactions with phase coupling
        entanglement = 0.0
        for i in range(0, self.dim - 1, 2):
            if i + 1 < self.dim:
                entanglement += np.sin(x_norm[i] + x_norm[i+1]) * np.cos(x_norm[i] - x_norm[i+1])
        
        # Chaotic logistic map component for additional complexity
        logistic = 0.0
        r = 3.9  # Chaos parameter
        for i in range(self.dim):
            logistic += np.sin(r * x_norm[i] * (1 - x_norm[i]))
        
        # Combine all components with dynamic weights
        return 1.2 * quantum + 0.8 * fractal + 1.5 * conditioning + 1.0 * periodic + 0.6 * entanglement + 0.9 * logistic