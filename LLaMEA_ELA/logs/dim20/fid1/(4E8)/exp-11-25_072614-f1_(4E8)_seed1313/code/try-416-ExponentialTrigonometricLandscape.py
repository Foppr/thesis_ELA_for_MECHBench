import numpy as np

class ExponentialTrigonometricLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize exponential decay parameters
        self.decay_params = np.random.rand(dim) * 3.0 + 1.0
        # Initialize polynomial conditioning weights
        self.poly_weights = np.random.rand(dim) * 2.0 + 1.0
        # Initialize trigonometric coupling strengths
        self.coupling_params = np.random.rand(dim) * 4.0 + 2.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay component
        exp_term = 0.0
        for i in range(self.dim):
            exp_term += self.decay_params[i] * np.exp(-self.poly_weights[i] * np.abs(x[i]))
            
        # Polynomial conditioning component
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += (x[i] ** 4) + (x[i] ** 3) - 2 * (x[i] ** 2) + x[i]
            
        # Trigonometric coupling component
        trig_term = 0.0
        for i in range(self.dim):
            trig_term += np.sin(self.coupling_params[i] * x[i]) * np.cos(0.5 * x[i])
            
        # Cross-term interactions creating sharp ridges
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(0.3 * x[i]) * np.cos(0.7 * x[j])
                
        # Combine all components
        result = exp_term + poly_term + trig_term + cross_term
        
        return result