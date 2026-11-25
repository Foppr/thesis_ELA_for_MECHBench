import numpy as np

class ChaoticMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial component with multiple chaotic sine modulations and exponential decay
        r = np.sqrt(np.sum(x**2))
        radial_term = np.exp(-r / 3.0) * (1.0 + 0.9 * np.sin(r * 4.0) * np.cos(r * 0.7) * np.sin(r * 2.0))
        
        # Enhanced sinusoidal chaos with multiple frequency components, modified decay, and cubic terms
        chaotic_term = 0.0
        for i in range(self.dim):
            freq = (i + 1) * 2.0
            chaotic_term += np.sin(x[i] * np.pi * freq) * np.exp(-x[i]**2 / 8.0) * np.cos(x[i] * 0.7) + 0.35 * x[i]**3
        
        # Increased polynomial complexity with mixed powers, cross-terms, and exponential weights
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += x[i]**5 + 0.6 * x[i]**7 + 0.35 * x[i]**3 + 0.25 * x[i]**9
        
        # Stronger cross-dimensional interaction with exponential coupling and higher-order terms
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[i] * x[j] * 0.7) * np.exp(-(x[i]**2 + x[j]**2) / 5.0) * (1.0 + 0.35 * (x[i]**4 + x[j]**4) + 0.15 * x[i]**6 * x[j]**6)
        
        # Novel angular-based symmetry breaking with higher-order trigonometric components and exponential modulation
        angle_term = 0.0
        for i in range(self.dim):
            angle_term += np.sin(x[i] * np.pi / 1.4) * np.cos(x[i] * np.pi / 2.8) * np.sin(x[i] * np.pi / 3.5) * np.exp(-x[i]**2 / 6.0)
        
        # Additional harmonic coupling and multi-modal peaks with enhanced complexity
        harmonic_term = 0.0
        for i in range(self.dim):
            harmonic_term += 0.7 * np.sin(x[i] * np.pi * 2.5) * np.cos(x[i] * np.pi * 1.5) * np.exp(-x[i]**2 / 6.0) + 0.25 * np.sin(x[i] * np.pi * 4.5)
        
        # Combine all terms with adjusted weights for increased complexity and better fitness score
        result = radial_term + 0.85 * chaotic_term + 0.55 * poly_term + 0.45 * cross_term + 0.25 * angle_term + 0.35 * harmonic_term
        
        return result