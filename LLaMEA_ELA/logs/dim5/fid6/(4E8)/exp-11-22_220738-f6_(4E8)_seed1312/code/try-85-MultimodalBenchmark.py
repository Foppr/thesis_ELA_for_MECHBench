import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Adaptive conditioning parameters
        self.conditioning_factors = np.linspace(1.0, 10.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term with varying exponents
        f_val = np.sum(self.conditioning_factors * (x**4 + 0.5 * x**3 + 0.2 * x**2))
        
        # Trigonometric oscillations with adaptive frequencies and amplitudes
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * 0.7)
            amp = 0.8 + 0.2 * np.cos(i * 0.9)
            f_val += amp * np.sin(freq * x[i]) * np.cos(0.3 * x[i])
            
        # Exponential modulation with Gaussian-like peaks
        for i in range(self.dim):
            center = -4.0 + 8.0 * (i / (self.dim - 1) if self.dim > 1 else 0)
            width = 0.5 + 0.5 * np.sin(i * 0.6)
            height = 1.0 + 0.5 * np.cos(i * 0.4)
            f_val += height * np.exp(-0.5 * ((x[i] - center) / width)**2)
            
        # Cross-dimensional interaction with adaptive coupling strength
        if self.dim >= 2:
            for i in range(self.dim - 1):
                coupling = 0.3 + 0.7 * np.sin(i * 0.5)
                f_val += coupling * x[i] * x[i+1] * np.cos(0.2 * (x[i] + x[i+1]))
                
        # Saddle point structure with non-linear transformation
        if self.dim >= 3:
            for i in range(self.dim - 2):
                f_val += 0.25 * (x[i]**2 - x[i+1]**2) * np.tanh(x[i+2])
                
        # High-frequency noise component to increase optimization challenge
        noise_freq = 10.0 + 5.0 * np.sin(self.dim)
        f_val += 0.1 * np.sum(np.sin(noise_freq * x))
        
        return f_val