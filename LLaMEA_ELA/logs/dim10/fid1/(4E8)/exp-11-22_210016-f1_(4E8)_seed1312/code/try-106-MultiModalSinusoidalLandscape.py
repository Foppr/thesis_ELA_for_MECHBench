import numpy as np

class MultiModalSinusoidalLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with sinusoidal modulation and exponential decay
        r = np.sqrt(np.sum(x**2))
        radial_term = np.exp(-r / 2.0) * (1.0 + 0.5 * np.sin(r * 2.0) + 0.3 * np.cos(r * 3.0))
        
        # Multi-modal sinusoidal components with varying frequencies and amplitudes
        modal_term = 0.0
        for i in range(self.dim):
            modal_term += (np.sin(5.0 * x[i]) + 0.7 * np.cos(3.0 * x[i]) + 
                          0.3 * np.sin(7.0 * x[i]) + 0.5 * np.cos(4.0 * x[i]))**2
        
        # Cross-dimensional coupling with exponential weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.exp(-0.5 * (x[i]**2 + x[j]**2)) * np.sin(x[i] * x[j])
        
        # Exponential interaction terms with radial symmetry breaking
        exp_interaction = 0.0
        for i in range(self.dim):
            exp_interaction += np.exp(-0.1 * x[i]**2) * (1.0 + 0.5 * np.sin(x[i])**2)
        
        # Polynomial cross-terms with mixed degrees
        poly_cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_cross += x[i]**2 * x[j]**3 + x[i]**3 * x[j]**2
        
        # Additional periodic modulation with hyperbolic tangent enhancement
        tanh_modulation = 0.0
        for i in range(self.dim):
            tanh_modulation += np.tanh(x[i]) * np.sin(2.0 * x[i])
        
        # Combine all terms with appropriate weights
        result = radial_term + 0.8 * modal_term + 0.3 * cross_term + 0.2 * exp_interaction + \
                 0.15 * poly_cross + 0.1 * tanh_modulation
        
        return result