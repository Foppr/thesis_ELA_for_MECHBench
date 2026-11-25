import numpy as np

class ExponentialTrigonometricLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize exponential decay parameters with wider range
        self.decay_params = np.random.rand(dim) * 5.0 + 2.0
        # Initialize polynomial conditioning weights with higher degree terms
        self.poly_weights = np.random.rand(dim) * 3.0 + 1.5
        # Initialize trigonometric coupling strengths with irregular spacing
        self.coupling_params = np.random.rand(dim) * 6.0 + 3.0
        # Add chaotic interaction parameters
        self.chaotic_params = np.random.rand(dim) * 0.5 + 0.25
        # Add basin shaping parameters
        self.basin_params = np.random.rand(dim) * 4.0 + 1.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay component with chaotic modulation
        exp_term = 0.0
        for i in range(self.dim):
            exp_term += self.decay_params[i] * np.exp(-self.poly_weights[i] * np.abs(x[i])) * \
                       (1.0 + 0.3 * np.sin(self.chaotic_params[i] * x[i]))
            
        # Polynomial conditioning component with basin shaping
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += (x[i] ** 5) + (x[i] ** 4) - 3 * (x[i] ** 3) + 2 * (x[i] ** 2) - x[i] + \
                        self.basin_params[i] * np.sin(0.1 * x[i]) * np.cos(0.2 * x[i])
            
        # Trigonometric coupling component with enhanced complexity
        trig_term = 0.0
        for i in range(self.dim):
            trig_term += np.sin(self.coupling_params[i] * x[i]) * np.cos(0.5 * x[i]) + \
                        0.5 * np.sin(2.0 * self.coupling_params[i] * x[i]) * np.cos(1.5 * x[i])
            
        # Cross-term interactions creating extremely sharp ridges and flat regions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (np.sin(0.3 * x[i]) * np.cos(0.7 * x[j]) + 
                              0.2 * np.sin(0.5 * x[i]) * np.cos(1.2 * x[j]) * 
                              np.exp(-0.1 * (x[i]**2 + x[j]**2)))
                
        # Additional chaotic cross-interactions
        chaotic_cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic_cross += 0.3 * np.sin(0.8 * x[i] + 0.6 * x[j]) * \
                               np.cos(0.4 * x[i] - 0.9 * x[j]) * \
                               np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Combine all components
        result = exp_term + poly_term + trig_term + cross_term + chaotic_cross
        
        return result