import numpy as np

class PolynomialTrigonometricNoise:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial potential terms
        poly_potential = 0
        for i in range(self.dim):
            poly_potential += 0.1 * x[i]**6 - 0.5 * x[i]**4 + 0.3 * x[i]**2
        
        # Trigonometric coupling between dimensions
        trig_coupling = 0
        for i in range(self.dim - 1):
            trig_coupling += np.sin(x[i]) * np.cos(x[i+1]) + 0.5 * np.sin(x[i] + x[i+1])
        
        # Adaptive noise component based on position
        noise = 0
        for i in range(self.dim):
            noise += 0.05 * np.sin(10 * x[i]) * np.cos(5 * x[i]) * (1 + 0.1 * np.abs(x[i]))
        
        # Cross-dimensional interaction with Gaussian-like peaks
        peak_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                peak_interaction += np.exp(-0.5 * ((x[i] - x[j])**2 + (x[i] + x[j])**2) / 2.0)
        
        # Global scaling and modulation
        global_mod = 1.0 + 0.2 * np.sin(0.1 * np.sum(x**2))
        
        # Combine all components
        return global_mod * (poly_potential + 0.5 * trig_coupling + 0.3 * peak_interaction + noise)