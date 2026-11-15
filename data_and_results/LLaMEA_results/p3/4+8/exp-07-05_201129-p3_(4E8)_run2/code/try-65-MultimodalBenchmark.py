import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Radial component with chaotic sinusoidal modulation
        r = np.sqrt(np.sum(x_normalized**2))
        radial = r * (1.0 + 0.5 * np.sin(10 * r) * np.cos(5 * r))
        
        # Nested sinusoidal terms with varying frequencies and amplitudes
        nested = 0.0
        for i in range(1, min(6, self.dim + 1)):
            freq = i * 2
            amp = 1.0 / (i * 2)
            nested += amp * np.sin(freq * np.pi * x_normalized[i-1]) * np.cos(freq * np.pi * r)
        
        # Gradient-dependent conditioning
        grad_cond = 0.0
        for i in range(self.dim):
            grad_cond += (x_normalized[i]**2) * (1.0 + 0.1 * np.abs(x_normalized[i]))
        
        # Chaotic interaction term
        chaotic = np.sum(np.sin(20 * x_normalized) * np.cos(15 * x_normalized)) * np.exp(-r**2)
        
        # Global minimum at origin with additional local optima
        return radial + 0.3 * nested + 0.1 * grad_cond + 0.05 * chaotic + 1.0