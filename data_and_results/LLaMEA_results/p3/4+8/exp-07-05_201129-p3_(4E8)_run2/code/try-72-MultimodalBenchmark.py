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
        
        # Multiple interacting peaks with varying frequencies and amplitudes
        peaks = 0.0
        for i in range(1, min(8, self.dim + 1)):
            freq = i * 3
            amp = 1.0 / (i * 3)
            peaks += amp * np.sin(freq * np.pi * x_normalized[i-1]) * np.cos(freq * np.pi * r) * np.exp(-0.5 * (x_normalized[i-1] - 0.5)**2)
        
        # Gradient-dependent conditioning with non-separable terms
        grad_cond = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                grad_cond += (x_normalized[i]**2) * (x_normalized[j]**2) * (1.0 + 0.2 * np.abs(x_normalized[i] * x_normalized[j]))
        
        # Chaotic interaction term with multiple interacting sine waves
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(25 * x_normalized[i]) * np.cos(18 * x_normalized[i]) * np.sin(12 * r)
        
        # Deceptive fitness valleys and complex energy landscape
        valleys = 0.0
        for i in range(1, min(5, self.dim + 1)):
            valleys += 0.1 * np.sin(5 * np.pi * x_normalized[i-1]) * np.cos(7 * np.pi * r) * np.exp(-0.3 * r**2)
        
        # Global minimum at origin with additional local optima distribution
        return radial + 0.4 * peaks + 0.15 * grad_cond + 0.08 * chaotic + 0.1 * valleys + 1.0