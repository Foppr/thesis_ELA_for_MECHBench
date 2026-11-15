import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Fractal-like radial component with self-similar sinusoidal structure
        r = np.sqrt(np.sum(x_normalized**2))
        fractal_radial = r * (1.0 + 0.3 * np.sin(15 * r) * np.cos(7 * r) * np.sin(3 * r))
        
        # Quantum interference pattern with multiple interacting waves
        quantum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_normalized[i] - x_normalized[j])
                quantum += np.sin(10 * dist) * np.cos(5 * dist) * np.exp(-dist**2 * 0.1)
        
        # Adaptive gradient conditioning with dimension-dependent scaling
        adaptive_grad = 0.0
        for i in range(self.dim):
            adaptive_grad += (x_normalized[i]**2) * (1.0 + 0.2 * np.sin(self.dim * x_normalized[i]))
        
        # Multi-scale nested sinusoidal interactions with chaotic frequency modulation
        nested = 0.0
        for i in range(1, min(8, self.dim + 1)):
            freq = i * 3 + np.sin(i * 0.5)
            amp = 1.0 / (i * 3 + np.cos(i * 0.3))
            nested += amp * np.sin(freq * np.pi * x_normalized[i-1]) * np.cos(freq * np.pi * r)
        
        # Enhanced local optima with polynomial and trigonometric mixing
        local_optima = 0.0
        for i in range(self.dim):
            local_optima += 0.15 * np.sin(12 * x_normalized[i] + i * 0.5) * np.cos(6 * x_normalized[i] - i * 0.3) + \
                           0.05 * x_normalized[i]**4 * np.sin(8 * x_normalized[i])
        
        # Fractal-based chaotic interaction with exponential decay
        chaotic = np.sum(np.sin(25 * x_normalized) * np.cos(20 * x_normalized)) * np.exp(-r**2 * 0.3)
        
        # Global minimum at origin with additional fitness landscape complexity
        return fractal_radial + 0.25 * quantum + 0.15 * adaptive_grad + 0.2 * nested + 0.08 * chaotic + 0.12 * local_optima + 1.5