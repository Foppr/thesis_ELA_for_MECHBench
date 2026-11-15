import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Radial component with enhanced chaotic sinusoidal modulation
        r = np.sqrt(np.sum(x_normalized**2))
        radial = r * (1.0 + 0.8 * np.sin(12 * r) * np.cos(7 * r) + 0.2 * np.sin(20 * r))
        
        # Nested sinusoidal terms with varying frequencies, amplitudes, and phase shifts
        nested = 0.0
        for i in range(1, min(6, self.dim + 1)):
            freq = i * 4
            amp = 1.0 / (i * 2)
            phase = i * np.pi / 3
            nested += amp * np.sin(freq * np.pi * x_normalized[i-1] + phase) * np.cos(freq * np.pi * r + phase)
        
        # Gradient-dependent conditioning with enhanced nonlinearity
        grad_cond = 0.0
        for i in range(self.dim):
            grad_cond += (x_normalized[i]**3) * (1.0 + 0.3 * np.abs(x_normalized[i]) + 0.15 * x_normalized[i]**2)
        
        # Chaotic interaction term with modified interaction kernel
        chaotic = np.sum(np.sin(30 * x_normalized) * np.cos(25 * x_normalized)) * np.exp(-r**2 * 0.4)
        
        # Additional local optima with fractal-like distribution
        local_optima = 0.0
        for i in range(self.dim):
            local_optima += 0.2 * np.sin(15 * x_normalized[i] + i * 0.4) * np.cos(7 * x_normalized[i] - i * 0.2)
        
        # Energy-based potential field with multiple interacting wells
        potential = 0.0
        for i in range(1, min(4, self.dim + 1)):
            potential += 0.3 * np.exp(-((x_normalized[i-1] - 0.4)**2 + (x_normalized[i-1] + 0.4)**2) * 6)
        
        # Global minimum at origin with enhanced local optima distribution
        return radial + 0.5 * nested + 0.2 * grad_cond + 0.1 * chaotic + 0.2 * local_optima + 0.25 * potential + 1.0