import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Radial component with fractal-like chaotic sinusoidal modulation
        r = np.sqrt(np.sum(x_normalized**2))
        radial = r * (1.0 + 0.3 * np.sin(15 * r) * np.cos(8 * r) * np.sin(3 * r))
        
        # Nested sinusoidal terms with varying frequencies, amplitudes, and phase shifts
        nested = 0.0
        for i in range(1, min(8, self.dim + 1)):
            freq = i * 3
            amp = 1.0 / (i * 3)
            phase = i * np.pi / 4
            nested += amp * np.sin(freq * np.pi * x_normalized[i-1] + phase) * np.cos(freq * np.pi * r + phase)
        
        # Gradient-dependent conditioning with exponential scaling
        grad_cond = 0.0
        for i in range(self.dim):
            grad_cond += (x_normalized[i]**2) * (1.0 + 0.2 * np.abs(x_normalized[i]) + 0.1 * x_normalized[i]**4)
        
        # Chaotic interaction term with fractal-like exponential decay and multiple peaks
        chaotic = np.sum(np.sin(25 * x_normalized) * np.cos(20 * x_normalized)) * np.exp(-r**3 * 0.3) + \
                  0.5 * np.sin(50 * r) * np.cos(30 * r)
        
        # Additional local optima with shifted sinusoidal components and fractal-like structure
        local_optima = 0.0
        for i in range(self.dim):
            local_optima += 0.3 * np.sin(12 * x_normalized[i] + i * np.pi/6) * np.cos(6 * x_normalized[i] - i * np.pi/3) + \
                           0.1 * np.sin(24 * x_normalized[i]) * np.cos(18 * x_normalized[i])
        
        # Deceptive fitness valleys and strong conditioning
        valley = 0.0
        for i in range(self.dim):
            valley += 0.4 * np.sin(30 * x_normalized[i])**2 * np.cos(15 * x_normalized[i])**2
        
        # Global minimum at origin with additional local optima and fractal complexity
        return radial + 0.4 * nested + 0.15 * grad_cond + 0.1 * chaotic + 0.15 * local_optima + 0.2 * valley + 1.5