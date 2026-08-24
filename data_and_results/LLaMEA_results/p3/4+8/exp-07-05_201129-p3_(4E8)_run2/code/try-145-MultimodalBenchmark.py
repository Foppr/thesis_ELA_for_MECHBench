import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Radial component with enhanced chaotic sinusoidal modulation
        r = np.sqrt(np.sum(x_normalized**2))
        radial = r * (1.0 + 0.8 * np.sin(17 * r) * np.cos(9 * r) + 0.2 * np.sin(27 * r))
        
        # Nested sinusoidal terms with varying frequencies, amplitudes, and phase shifts
        nested = 0.0
        for i in range(1, min(7, self.dim + 1)):
            freq = i * 3.5
            amp = 1.0 / (i * 2.5)
            phase = i * np.pi / 3.5
            nested += amp * np.sin(freq * np.pi * x_normalized[i-1] + phase) * np.cos(freq * np.pi * r + phase)
        
        # Gradient-dependent conditioning with enhanced nonlinearity
        grad_cond = 0.0
        for i in range(self.dim):
            grad_cond += (x_normalized[i]**3) * (1.0 + 0.25 * np.abs(x_normalized[i]) + 0.12 * x_normalized[i]**2)
        
        # Chaotic interaction term with modified interaction kernel
        chaotic = np.sum(np.sin(27 * x_normalized) * np.cos(22 * x_normalized)) * np.exp(-r**2 * 0.35)
        
        # Additional local optima with fractal-like distribution
        local_optima = 0.0
        for i in range(self.dim):
            local_optima += 0.16 * np.sin(13 * x_normalized[i] + i * 0.55) * np.cos(6.5 * x_normalized[i] - i * 0.35)
        
        # Energy-based potential field with multiple interacting wells
        potential = 0.0
        for i in range(1, min(5, self.dim + 1)):
            potential += 0.27 * np.exp(-((x_normalized[i-1] - 0.45)**2 + (x_normalized[i-1] + 0.45)**2) * 5.5)
        
        # Global minimum at origin with enhanced local optima distribution
        return radial + 0.42 * nested + 0.16 * grad_cond + 0.09 * chaotic + 0.16 * local_optima + 0.21 * potential + 1.0