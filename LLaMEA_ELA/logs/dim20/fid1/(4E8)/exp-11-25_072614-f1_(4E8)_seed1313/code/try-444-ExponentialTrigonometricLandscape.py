import numpy as np

class ExponentialTrigonometricLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic exponential decay parameters
        self.decay_params = np.random.rand(dim) * 5.0 + 2.0
        # Initialize higher-order polynomial conditioning weights
        self.poly_weights = np.random.rand(dim) * 3.0 + 1.0
        # Initialize complex trigonometric coupling strengths
        self.coupling_params = np.random.rand(dim) * 6.0 + 3.0
        # Initialize adaptive scaling factors
        self.scaling_factors = np.random.rand(dim) * 4.0 + 1.0
        # Initialize interaction coupling coefficients
        self.interaction_coeffs = np.random.rand(dim, dim) * 2.0 + 1.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic exponential decay component with adaptive scaling
        exp_term = 0.0
        for i in range(self.dim):
            exp_term += self.decay_params[i] * np.exp(-self.poly_weights[i] * np.abs(x[i])) * np.sin(2.0 * x[i])
            
        # Higher-order polynomial conditioning component with adaptive scaling
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += (x[i] ** 6) + (x[i] ** 5) - 3 * (x[i] ** 4) + 2 * (x[i] ** 3) - x[i] ** 2 + 0.5 * x[i]
            
        # Complex trigonometric coupling component
        trig_term = 0.0
        for i in range(self.dim):
            trig_term += np.sin(self.coupling_params[i] * x[i]) * np.cos(0.3 * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Novel cross-dimensional interaction terms with adaptive coefficients
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += self.interaction_coeffs[i,j] * np.sin(0.5 * x[i]) * np.cos(0.8 * x[j]) * np.exp(-0.2 * (x[i]**2 + x[j]**2))
                
        # Additional chaotic coupling term
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_term += np.sin(3.0 * x[i] + np.cos(1.5 * x[i])) * self.scaling_factors[i]
            
        # Combine all components with dynamic weighting
        result = exp_term + poly_term + trig_term + cross_term + chaos_term
        
        return result