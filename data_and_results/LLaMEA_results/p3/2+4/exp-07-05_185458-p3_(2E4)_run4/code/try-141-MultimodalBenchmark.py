import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial component with varying exponents and adaptive coefficients
        poly = 0.0
        for i in range(self.dim):
            exp = 2 + (i % 5)
            coef = 1.0 + 0.5 * np.sin(i * np.pi / 3.0)
            poly += coef * (x_norm[i] ** exp)
        
        # Trigonometric component with dynamic frequencies and amplitudes
        trig = 0.0
        for i in range(self.dim):
            freq = 2 * (i + 1) * np.pi
            amp = 1.0 + 0.3 * np.cos(i * np.pi / 4.0)
            trig += amp * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Exponential component with adaptive decay rates
        exp_comp = 0.0
        for i in range(self.dim):
            decay = 0.5 + 0.5 * np.sin(i * np.pi / 2.0)
            exp_comp += np.exp(-decay * x_norm[i]**2) * np.cos(10 * x_norm[i])
        
        # Dynamic coupling between dimensions with varying strength
        coupling = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            strength = 0.3 + 0.7 * np.sin(i * np.pi / self.dim)
            coupling += strength * np.sin(x_norm[i] + x_norm[j]) * np.cos(x_norm[i] * x_norm[j])
        
        # Adaptive noise component with dimension-dependent variance
        noise = 0.0
        for i in range(self.dim):
            variance = 0.1 + 0.2 * np.cos(i * np.pi / self.dim)
            noise += np.random.normal(0, variance) * np.sin(5 * x_norm[i])
        
        # Global shaping term with adaptive scaling
        shape = 0.0
        for i in range(self.dim):
            shape += 0.01 * x_norm[i]**4 + 0.02 * x_norm[i]**6
        
        # Final function value with weighted components
        return 0.6 * poly + 0.4 * trig + 0.3 * exp_comp + 0.2 * coupling + 0.1 * noise + 0.05 * shape