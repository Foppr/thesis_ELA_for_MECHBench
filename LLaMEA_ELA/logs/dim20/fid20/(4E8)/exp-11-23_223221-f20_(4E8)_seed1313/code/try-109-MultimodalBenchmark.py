import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Self-similar Gaussian peak components with fractal scaling
        peak_term = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.3 * np.sin(i * 0.5) + 0.2 * np.cos(i * 0.3)
            peak_term += scale * np.exp(-0.5 * ((x[i] - np.sin(i)) / (0.5 + 0.2 * np.cos(i)))**2)
        
        # Complex gradient interactions with multi-scale sinusoidal modulation
        grad_term = 0.0
        for i in range(self.dim):
            grad_term += (np.sin(x[i])**3 + np.cos(2.0 * x[i]) * np.tan(0.5 * x[i])) * \
                        (1.0 + 0.1 * np.sin(3.0 * x[i]) + 0.05 * np.cos(5.0 * x[i]))
        
        # Adaptive noise component that varies with dimension
        noise_term = 0.0
        for i in range(self.dim):
            noise_scale = 0.5 + 0.3 * np.sin(i * 0.8)
            noise_term += noise_scale * np.random.normal(0, 0.1) * np.exp(-0.1 * x[i]**2)
        
        # Multi-scale fractal energy interactions
        energy_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-8)
                energy_term += (np.sin(10.0 * dist) / (dist + 1.0)) * \
                              (np.cos(x[i]) + np.sin(x[j])) * \
                              np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Polynomial fractal basin with varying exponents
        basin_term = 0.0
        for i in range(self.dim):
            exponent = 2.0 + 0.5 * np.sin(i * 0.4)
            basin_term += (x[i]**exponent) * np.exp(-0.1 * x[i]**2) * \
                         (1.0 + 0.2 * np.cos(4.0 * x[i]))
        
        # Combined function with regularization
        return peak_term + grad_term + noise_term + energy_term + basin_term + 0.001 * np.sum(x**2)