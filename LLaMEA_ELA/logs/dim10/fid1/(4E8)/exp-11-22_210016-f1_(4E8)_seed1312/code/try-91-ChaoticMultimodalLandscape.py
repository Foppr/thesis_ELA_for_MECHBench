import numpy as np

class ChaoticMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial component with multiple chaotic sine modulations and exponential decay
        r = np.sqrt(np.sum(x**2))
        radial_term = np.exp(-r / 2.5) * (1.0 + 0.8 * np.sin(r * 3.5) * np.cos(r * 0.6) * np.sin(r * 1.7))
        
        # Enhanced sinusoidal chaos with multiple frequency components, modified decay, and cubic terms
        chaotic_term = 0.0
        for i in range(self.dim):
            freq = (i + 1) * 1.8
            chaotic_term += np.sin(x[i] * np.pi * freq) * np.exp(-x[i]**2 / 7.0) * np.cos(x[i] * 0.6) + 0.3 * x[i]**3
        
        # Increased polynomial complexity with mixed powers, cross-terms, and exponential weights
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += x[i]**5 + 0.5 * x[i]**7 + 0.3 * x[i]**3 + 0.2 * x[i]**9
        
        # Stronger cross-dimensional interaction with exponential coupling and higher-order terms
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[i] * x[j] * 0.6) * np.exp(-(x[i]**2 + x[j]**2) / 4.5) * (1.0 + 0.3 * (x[i]**4 + x[j]**4) + 0.1 * x[i]**6 * x[j]**6)
        
        # Novel angular-based symmetry breaking with higher-order trigonometric components and exponential modulation
        angle_term = 0.0
        for i in range(self.dim):
            angle_term += np.sin(x[i] * np.pi / 1.3) * np.cos(x[i] * np.pi / 2.7) * np.sin(x[i] * np.pi / 3.2) * np.exp(-x[i]**2 / 5.0)
        
        # Additional harmonic coupling and multi-modal peaks with enhanced complexity
        harmonic_term = 0.0
        for i in range(self.dim):
            harmonic_term += 0.6 * np.sin(x[i] * np.pi * 2.2) * np.cos(x[i] * np.pi * 1.3) * np.exp(-x[i]**2 / 5.5) + 0.2 * np.sin(x[i] * np.pi * 4.0)
        
        # Combine all terms with adjusted weights for increased complexity and better fitness score
        result = radial_term + 0.8 * chaotic_term + 0.5 * poly_term + 0.4 * cross_term + 0.2 * angle_term + 0.3 * harmonic_term
        
        return result