import numpy as np

class ChaoticSinusoidalRBFMixture:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic radial basis functions with dynamic centers and widths
        rbf_sum = 0
        for i in range(min(12, self.dim)):
            center = 5.0 * np.sin(i * 0.7) * np.cos(i * 0.3)
            width = 0.3 + 0.7 * np.sin(i * 0.5) ** 2
            rbf_sum += np.exp(-0.5 * np.sum((x - center)**2) / width**2)
        
        # Chaotic sinusoidal oscillations with varying frequencies
        sin_sum = 0
        for i in range(self.dim):
            freq = 1.0 + 2.0 * np.sin(i * 0.4)
            sin_sum += np.sin(freq * x[i]) + 0.3 * np.sin(3.0 * freq * x[i]) + 0.1 * np.sin(7.0 * freq * x[i])
        
        # High-order polynomial coupling with chaotic interaction terms
        poly_coupling = 0
        for i in range(self.dim - 1):
            poly_coupling += (x[i] * x[i+1])**3 + 0.2 * (x[i]**2 + x[i+1]**2)**2 + 0.05 * np.sin(x[i] * x[i+1])
        
        # Complex polynomial terms with chaotic coefficients
        poly_terms = 0
        for i in range(self.dim):
            coeff = 0.02 * np.sin(i * 0.6) + 0.05
            poly_terms += coeff * x[i]**9 - 0.08 * x[i]**8 + 0.15 * x[i]**7 - 0.1 * x[i]**6
        
        # Dynamic cross-dimensional coupling with chaotic modulation
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += np.sin(x[i] * x[j] * (i + j + 1)) * np.cos(0.5 * (x[i] + x[j]))
        
        # Global chaotic modulation
        chaotic_mod = np.sin(0.5 * np.sum(x**2)) * np.cos(0.3 * np.sum(x)) * np.sin(0.1 * np.sum(x**3))
        
        # Combine all components with dynamic weights
        return 2.0 * rbf_sum + 1.2 * sin_sum + 0.5 * poly_coupling + 0.3 * poly_terms + 0.2 * cross_coupling + 0.15 * chaotic_mod