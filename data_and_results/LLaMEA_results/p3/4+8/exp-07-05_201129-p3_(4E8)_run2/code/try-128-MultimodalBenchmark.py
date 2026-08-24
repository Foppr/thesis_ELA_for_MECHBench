import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Radial component with enhanced chaotic sinusoidal modulation
        r = np.sqrt(np.sum(x_normalized**2))
        radial = r * (1.0 + 0.7 * np.sin(15 * r) * np.cos(8 * r) + 0.3 * np.sin(25 * r))
        
        # Nested sinusoidal terms with varying frequencies, amplitudes, and phase shifts
        nested = 0.0
        for i in range(1, min(7, self.dim + 1)):
            freq = i * 3
            amp = 1.0 / (i * 3)
            phase = i * np.pi / 4
            nested += amp * np.sin(freq * np.pi * x_normalized[i-1] + phase) * np.cos(freq * np.pi * r + phase)
        
        # Gradient-dependent conditioning with enhanced nonlinearity
        grad_cond = 0.0
        for i in range(self.dim):
            grad_cond += (x_normalized[i]**3) * (1.0 + 0.2 * np.abs(x_normalized[i]) + 0.1 * x_normalized[i]**2)
        
        # Chaotic interaction term with modified interaction kernel
        chaotic = np.sum(np.sin(25 * x_normalized) * np.cos(20 * x_normalized)) * np.exp(-r**2 * 0.3)
        
        # Additional local optima with fractal-like distribution
        local_optima = 0.0
        for i in range(self.dim):
            local_optima += 0.15 * np.sin(12 * x_normalized[i] + i * 0.5) * np.cos(6 * x_normalized[i] - i * 0.3)
        
        # Energy-based potential field with multiple interacting wells
        potential = 0.0
        for i in range(1, min(5, self.dim + 1)):
            potential += 0.25 * np.exp(-((x_normalized[i-1] - 0.5)**2 + (x_normalized[i-1] + 0.5)**2) * 5)
        
        # Global minimum at origin with enhanced local optima distribution
        return radial + 0.4 * nested + 0.15 * grad_cond + 0.08 * chaotic + 0.15 * local_optima + 0.2 * potential + 1.0