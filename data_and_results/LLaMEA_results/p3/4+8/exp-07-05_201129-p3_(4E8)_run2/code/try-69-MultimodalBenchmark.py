import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Radial component with enhanced chaotic sinusoidal modulation
        r = np.sqrt(np.sum(x_normalized**2))
        radial = r * (1.0 + 0.7 * np.sin(12 * r) * np.cos(6 * r))
        
        # Nested sinusoidal terms with varying frequencies and amplitudes
        nested = 0.0
        for i in range(1, min(7, self.dim + 1)):
            freq = i * 2.5
            amp = 1.0 / (i * 3)
            nested += amp * np.sin(freq * np.pi * x_normalized[i-1]) * np.cos(freq * np.pi * r)
        
        # Gradient-dependent conditioning with increased nonlinearity
        grad_cond = 0.0
        for i in range(self.dim):
            grad_cond += (x_normalized[i]**2) * (1.0 + 0.2 * np.abs(x_normalized[i]) + 0.1 * x_normalized[i]**4)
        
        # Chaotic interaction term with modified exponential decay and additional sine component
        chaotic = np.sum(np.sin(25 * x_normalized) * np.cos(20 * x_normalized)) * np.exp(-r**2 * 0.3)
        
        # Additional local optima with shifted sinusoidal components and increased frequency
        local_optima = 0.0
        for i in range(self.dim):
            local_optima += 0.3 * np.sin(10 * x_normalized[i] + i) * np.cos(5 * x_normalized[i] - i)
        
        # Global minimum at origin with additional local optima
        return radial + 0.4 * nested + 0.15 * grad_cond + 0.08 * chaotic + 0.15 * local_optima + 1.0