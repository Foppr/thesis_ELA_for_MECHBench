import numpy as np

class ChaoticMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with enhanced chaotic sine modulation
        r = np.sqrt(np.sum(x**2))
        radial_term = np.exp(-r / 3.0) * (1.0 + 0.7 * np.sin(r * 3.0) * np.cos(r * 0.7))
        
        # Enhanced sinusoidal chaos component with variable frequencies
        chaotic_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 0.5 * np.sin(i)
            chaotic_term += np.sin(x[i] * np.pi * freq) * np.exp(-x[i]**2 / 8.0)
        
        # Modified higher-order polynomial interactions with asymmetric weights
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += 1.5 * x[i]**4 + 0.2 * x[i]**6 + 0.1 * x[i]**8
        
        # Enhanced cross-dimensional interaction with nonlinear coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = (1.0 + 0.2 * np.sin(x[i] * x[j] * 0.5))
                cross_term += np.sin(x[i] * x[j]) * coupling * (x[i]**2 + x[j]**2)
        
        # Additional angular-based symmetry breaking with multiple components
        angle_term = 0.0
        for i in range(self.dim):
            angle_term += 0.5 * np.sin(x[i] * np.pi / 2.0) * np.cos(x[i] * np.pi / 3.0) + \
                         0.3 * np.sin(x[i] * np.pi / 4.0) * np.cos(x[i] * np.pi / 6.0)
        
        # Additional radial symmetry breaking component
        symmetry_term = 0.0
        for i in range(self.dim):
            symmetry_term += 0.2 * np.sin(r * 0.5) * np.cos(x[i] * 0.3)
        
        # Combine all terms with optimized weights
        result = radial_term + 0.6 * chaotic_term + 0.4 * poly_term + 0.3 * cross_term + 0.2 * angle_term + 0.1 * symmetry_term
        
        return result