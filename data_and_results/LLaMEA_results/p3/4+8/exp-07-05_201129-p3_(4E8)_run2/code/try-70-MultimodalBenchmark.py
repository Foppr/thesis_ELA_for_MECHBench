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
        
        # Chaotic interaction term with multiple interacting peaks and fractal structure
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(25 * x_normalized[i]) * np.cos(18 * x_normalized[i]) * np.exp(-0.5 * (x_normalized[i] - 0.5)**2)
        chaotic *= np.exp(-r**2 * 0.3)
        
        # Additional local optima with fractal-like distribution and deceptive valleys
        local_optima = 0.0
        for i in range(self.dim):
            local_optima += 0.15 * np.sin(12 * x_normalized[i] + i * np.pi/3) * np.cos(6 * x_normalized[i] - i * np.pi/6) * np.exp(-0.1 * (x_normalized[i] - 0.3)**2)
        
        # Fractal energy landscape with multiple interacting peaks and valleys
        fractal_energy = 0.0
        for i in range(1, min(5, self.dim + 1)):
            fractal_energy += (1.0 / i) * np.sin(20 * x_normalized[i-1] + i * np.pi/5) * np.cos(15 * x_normalized[i-1] - i * np.pi/4) * np.exp(-0.2 * r**2)
        
        # Global minimum at origin with enhanced local optima distribution
        return radial + 0.4 * nested + 0.15 * grad_cond + 0.08 * chaotic + 0.12 * local_optima + 0.05 * fractal_energy + 1.5