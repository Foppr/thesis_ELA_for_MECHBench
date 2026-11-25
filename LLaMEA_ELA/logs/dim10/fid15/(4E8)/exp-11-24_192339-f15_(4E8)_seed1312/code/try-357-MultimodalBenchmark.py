import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.omega = np.random.uniform(0.5, 2.0, dim)
        self.alpha = np.random.uniform(0.1, 0.5, dim)
        self.beta = np.random.uniform(0.3, 1.0, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal oscillation component with adaptive frequency
        sin_component = 0
        for i in range(self.dim):
            freq = self.omega[i] * (1 + 0.2 * np.sin(0.3 * x[i]))
            sin_component += np.sin(freq * x[i]) * np.cos(freq * x[i]**2)
        
        # Adaptive polynomial potential with dimension-dependent exponents
        poly_component = 0
        for i in range(self.dim):
            exp = 2 + 2 * np.sin(0.4 * x[i] + i)
            poly_component += (x[i]**exp) * np.exp(-0.1 * x[i]**2)
        
        # Cross-dimensional interference with dynamic coupling
        cross_component = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling = 0.5 + 0.3 * np.cos(0.5 * (x[i] + x[j]))
                cross_component += coupling * np.sin(x[i] * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Gaussian ridge structure with variable width
        ridge_component = 0
        for i in range(self.dim):
            width = 1.0 + 0.5 * np.sin(0.6 * x[i] + self.dim * 0.2)
            ridge_component += (x[i]**2) * np.exp(-0.5 * (x[i]**2) / (width**2))
        
        # Multi-scale harmonic modulation
        harmonic_component = 0
        for i in range(self.dim):
            mod_freq = 1.0 + 0.3 * np.sin(0.7 * x[i])
            harmonic_component += np.sin(mod_freq * x[i]) * np.cos(mod_freq * x[i]**3)
        
        # Final combined landscape with weighted components
        return (0.3 * sin_component + 
                0.25 * poly_component + 
                0.2 * cross_component + 
                0.15 * ridge_component + 
                0.1 * harmonic_component)