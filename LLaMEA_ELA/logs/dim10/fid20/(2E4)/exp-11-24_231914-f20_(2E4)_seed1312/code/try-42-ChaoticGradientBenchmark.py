import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base term
        quadratic = np.sum(x**2) / self.dim
        
        # Chaotic gradient component with sine-modulated coefficients
        chaotic_grad = 0.0
        for i in range(self.dim):
            coeff = 1.0 + 0.5 * np.sin(3.0 * x[i])
            chaotic_grad += coeff * np.sin(2.0 * x[i]) * np.cos(1.5 * x[i])
        
        # Saddle-point structure with alternating signs
        saddle = 0.0
        for i in range(self.dim):
            saddle += (-1)**i * (x[i]**4 - 2*x[i]**2)
        
        # Sinusoidal modulation with varying frequencies and amplitudes
        sinusoidal = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.3 * np.sin(0.5 * i)
            amp = 0.8 + 0.2 * np.cos(0.7 * i)
            sinusoidal += amp * np.sin(freq * x[i])
        
        # Dimension-adaptive difficulty factor
        diff_factor = 1.0 + 0.1 * self.dim
        
        # Combined function with exponential scaling
        return diff_factor * (quadratic + 0.3 * chaotic_grad + 0.2 * saddle + 0.4 * sinusoidal)