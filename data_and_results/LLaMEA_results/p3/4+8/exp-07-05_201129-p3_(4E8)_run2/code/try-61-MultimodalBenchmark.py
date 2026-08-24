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
            grad_cond += (x_normalized[i]**2) * (1.0 + 0.2 * np.exp(np.abs(x_normalized[i]) * 2))
        
        # Chaotic interaction term with multiple exponential decays and fractal scaling
        chaotic = np.sum(np.sin(25 * x_normalized) * np.cos(20 * x_normalized)) * np.exp(-r**2 * 0.3) * np.sin(7 * r)
        
        # Additional local optima with shifted fractal sinusoidal components and cross-terms
        local_optima = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(self.dim, i+3)):
                local_optima += 0.15 * np.sin(10 * x_normalized[i] + 2 * x_normalized[j]) * np.cos(5 * x_normalized[i] - 3 * x_normalized[j])
        
        # Fractal energy landscape with multiple interacting peaks and valleys
        fractal_energy = 0.0
        for i in range(1, min(5, self.dim + 1)):
            fractal_energy += 0.25 * np.sin(12 * x_normalized[i-1]) * np.cos(9 * x_normalized[i-1]) * np.exp(-0.5 * (x_normalized[i-1] - 0.5)**2)
        
        # Global minimum at origin with enhanced local optima distribution
        return radial + 0.4 * nested + 0.15 * grad_cond + 0.08 * chaotic + 0.15 * local_optima + 0.2 * fractal_energy + 1.0