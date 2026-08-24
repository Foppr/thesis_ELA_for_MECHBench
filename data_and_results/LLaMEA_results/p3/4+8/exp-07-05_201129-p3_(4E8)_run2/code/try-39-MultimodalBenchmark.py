import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Radial component with chaotic sinusoidal modulation
        r = np.sqrt(np.sum(x_normalized**2))
        radial = r * (1.0 + 0.3 * np.sin(15 * r) * np.cos(8 * r) * np.exp(-0.5 * r))
        
        # Nested sinusoidal terms with varying frequencies and amplitudes
        nested = 0.0
        for i in range(1, min(8, self.dim + 1)):
            freq = i * 3
            amp = 1.0 / (i * 3)
            nested += amp * np.sin(freq * np.pi * x_normalized[i-1]) * np.cos(freq * np.pi * r) * np.exp(-0.1 * i)
        
        # Gradient-dependent conditioning with polynomial terms
        grad_cond = 0.0
        for i in range(self.dim):
            grad_cond += (x_normalized[i]**4) * (1.0 + 0.2 * np.abs(x_normalized[i]) + 0.1 * x_normalized[i]**2)
        
        # Chaotic interaction term with exponential decay
        chaotic = np.sum(np.sin(25 * x_normalized) * np.cos(20 * x_normalized)) * np.exp(-r**3)
        
        # Additional polynomial correlation terms
        poly_corr = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(self.dim, i+3)):
                poly_corr += 0.05 * x_normalized[i] * x_normalized[j] * np.sin(5 * (x_normalized[i] + x_normalized[j]))
        
        # Global minimum at origin with additional local optima
        return radial + 0.4 * nested + 0.15 * grad_cond + 0.08 * chaotic + 0.03 * poly_corr + 1.5