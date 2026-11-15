import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Radial component with fractal-like chaotic modulation
        r = np.sqrt(np.sum(x_normalized**2))
        radial = r * (1.0 + 0.3 * np.sin(15 * r) * np.cos(8 * r) * np.sin(3 * r))
        
        # Multiple interacting peaks with varying frequencies and amplitudes
        peaks = 0.0
        for i in range(1, min(8, self.dim + 1)):
            freq = i * 3
            amp = 1.0 / (i * 3)
            peaks += amp * np.sin(freq * np.pi * x_normalized[i-1]) * np.cos(freq * np.pi * r) * np.exp(-0.5 * (x_normalized[i-1] - 0.5)**2)
        
        # Enhanced gradient-dependent conditioning with non-separability
        grad_cond = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                grad_cond += (x_normalized[i] * x_normalized[j]) * (1.0 + 0.2 * np.abs(x_normalized[i]) * np.abs(x_normalized[j]))
        
        # Chaotic interaction term with multiple deceptive valleys
        chaotic = np.sum(np.sin(25 * x_normalized) * np.cos(20 * x_normalized)) * np.exp(-r**2) * (1.0 + 0.1 * np.sin(50 * r))
        
        # Additional fractal-like local optima distribution
        fractal = 0.0
        for i in range(self.dim):
            fractal += 0.05 * np.sin(50 * x_normalized[i]) * np.cos(30 * x_normalized[i]) * np.exp(-0.1 * r**2)
        
        # Global minimum at origin with additional local optima
        return radial + 0.4 * peaks + 0.15 * grad_cond + 0.08 * chaotic + 0.03 * fractal + 1.5