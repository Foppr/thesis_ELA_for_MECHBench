import numpy as np

class ChaoticMultiModalLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with sinusoidal modulation and exponential decay
        r = np.sqrt(np.sum(x**2))
        radial_term = np.exp(-r / 2.0) * (1.0 + 0.5 * np.sin(r * 2.0) + 0.3 * np.cos(r * 4.0))
        
        # Multi-modal sinusoidal component with varying frequencies and amplitudes
        modal_term = 0.0
        for i in range(self.dim):
            modal_term += (np.sin(x[i] * 3.0) * np.cos(x[i] * 2.0) + 
                          0.7 * np.sin(x[i] * 5.0) * np.cos(x[i] * 3.0) + 
                          0.4 * np.sin(x[i] * 7.0) * np.cos(x[i] * 4.0))
        
        # Polynomial chaos component with cross-dimensional interactions
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += x[i]**6 + 0.5 * x[i]**4 + 0.3 * x[i]**2
        
        # Cross-dimensional coupling with chaotic interaction terms
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) * 
                              (1.0 + 0.2 * np.abs(x[i] - x[j])) + 
                              np.tanh(x[i] * x[j]) * np.exp(-0.5 * (x[i]**2 + x[j]**2)))
        
        # Additional chaotic component with radial symmetry breaking
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(x[i] * np.pi) * np.cos(x[i] * np.pi/2) * np.exp(-x[i]**2)
        
        # Hyperbolic tangent enhancement for gradient complexity
        tanh_enhancement = np.sum(np.tanh(x)**4)
        
        # Combine all terms with different weights
        result = 0.8 * radial_term + 0.6 * modal_term + 0.5 * poly_term + 0.3 * cross_term + 0.2 * chaotic_term + 0.1 * tanh_enhancement
        
        return result