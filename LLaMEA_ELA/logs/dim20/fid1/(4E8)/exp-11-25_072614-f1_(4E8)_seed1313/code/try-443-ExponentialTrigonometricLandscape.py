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
        # Initialize chaotic momentum parameters
        self.momentum_params = np.random.rand(dim) * 0.5 + 0.1
        
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
                
        # Chaotic momentum component adding non-linearity and complexity
        momentum_term = 0.0
        for i in range(self.dim):
            momentum_term += self.momentum_params[i] * np.sin(x[i] * np.pi) * np.cos(x[i] * np.pi / 2)
            
        # Additional high-frequency oscillation component
        high_freq_term = 0.0
        for i in range(self.dim):
            high_freq_term += np.sin(10 * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Combine all components
        result = exp_term + poly_term + trig_term + cross_term + momentum_term + high_freq_term
        
        return result