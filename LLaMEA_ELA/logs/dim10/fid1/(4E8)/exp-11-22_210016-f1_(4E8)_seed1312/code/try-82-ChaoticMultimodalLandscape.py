import numpy as np

class ChaoticMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with enhanced chaotic sine modulation
        r = np.sqrt(np.sum(x**2))
        radial_term = np.exp(-r / 2.0) * (1.0 + 0.8 * np.sin(r * 3.0) * np.cos(r * 0.5))
        
        # Enhanced sinusoidal chaos component with multiple exponential decay rates
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(x[i] * np.pi * (i + 2.0)) * np.exp(-x[i]**2 / 6.0) * np.cos(x[i] * 0.3)
        
        # Increased polynomial complexity with higher-order terms and modified weights
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += x[i]**5 + 0.5 * x[i]**7 + 0.3 * x[i]**4 + 0.1 * x[i]**8
        
        # Stronger cross-dimensional interaction with cubic coupling and trigonometric modulation
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[i] * x[j] * 0.7) * (1.0 + 0.25 * (x[i]**3 + x[j]**3)) * np.exp(-abs(x[i] - x[j]) / 4.0)
        
        # Novel angular-based symmetry breaking with enhanced exponential terms
        angle_term = 0.0
        for i in range(self.dim):
            angle_term += np.sin(x[i] * np.pi / 2.0) * np.cos(x[i] * np.pi / 3.0) * np.exp(-x[i]**2 / 10.0)
        
        # Additional chaotic cross-dimensional coupling with modified frequency harmonics
        freq_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_term += np.sin((x[i] + x[j]) * np.pi * 1.5) * np.cos((x[i] - x[j]) * np.pi * 0.8)
        
        # Combine all terms with adjusted weights for increased complexity
        result = radial_term + 0.7 * chaotic_term + 0.5 * poly_term + 0.4 * cross_term + 0.2 * angle_term + 0.1 * freq_term
        
        return result