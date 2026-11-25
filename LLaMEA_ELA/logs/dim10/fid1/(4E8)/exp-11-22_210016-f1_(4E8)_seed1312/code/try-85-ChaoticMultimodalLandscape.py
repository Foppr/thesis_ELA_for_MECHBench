import numpy as np

class ChaoticMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial component with multiple chaotic sine modulations
        r = np.sqrt(np.sum(x**2))
        radial_term = np.exp(-r / 3.0) * (1.0 + 0.7 * np.sin(r * 3.0) * np.cos(r * 0.7) * np.sin(r * 1.5))
        
        # Enhanced sinusoidal chaos with multiple frequency components and modified decay
        chaotic_term = 0.0
        for i in range(self.dim):
            freq = (i + 1) * 1.8  # Slightly increased frequencies
            chaotic_term += np.sin(x[i] * np.pi * freq) * np.exp(-x[i]**2 / 8.0) * np.cos(x[i] * 0.5)
        
        # Increased polynomial complexity with modified weights and added cross-terms
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += 1.2 * x[i]**5 + 0.6 * x[i]**7 + 0.3 * x[i]**3  # Increased weights
        
        # Stronger cross-dimensional interaction with modified coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.8 * np.sin(x[i] * x[j] * 0.5) * np.exp(-(x[i]**2 + x[j]**2) / 5.0) * (1.0 + 0.3 * (x[i]**4 + x[j]**4))
        
        # Novel angular-based symmetry breaking with higher-order trigonometric components
        angle_term = 0.0
        for i in range(self.dim):
            angle_term += np.sin(x[i] * np.pi / 1.8) * np.cos(x[i] * np.pi / 2.8) * np.sin(x[i] * np.pi / 3.8)  # Modified angles
        
        # Additional harmonic coupling and multi-modal peaks
        harmonic_term = 0.0
        for i in range(self.dim):
            harmonic_term += 0.6 * np.sin(x[i] * np.pi * 2.5) * np.cos(x[i] * np.pi * 1.5) * np.exp(-x[i]**2 / 6.0)
        
        # Combine all terms with adjusted weights for increased complexity
        result = radial_term + 0.8 * chaotic_term + 0.5 * poly_term + 0.4 * cross_term + 0.2 * angle_term + 0.3 * harmonic_term
        
        return result