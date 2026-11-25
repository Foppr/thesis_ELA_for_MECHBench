import numpy as np

class LogBarrierTrigonometricLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logarithmic barrier terms preventing boundary crossing
        barrier = 0.0
        for i in range(self.dim):
            barrier += 1.0 / (1.0 + np.exp(-10.0 * (x[i] - 5.0))) + 1.0 / (1.0 + np.exp(10.0 * (x[i] + 5.0)))
        
        # Trigonometric coupling between dimensions
        trig_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                trig_coupling += np.sin(x[i] * x[j] * 0.5) * np.cos((x[i] + x[j]) * 0.3)
        
        # Power-law decay interactions with varying exponents
        power_decay = 0.0
        for i in range(self.dim):
            power_decay += (1.0 / (1.0 + np.abs(x[i])**3.5)) * np.sin(x[i] * 2.0)**2
        
        # Multi-modal sinusoidal components with varying frequencies and amplitudes
        modal_terms = 0.0
        for i in range(self.dim):
            modal_terms += (np.sin(x[i] * 1.2) + 0.5 * np.sin(x[i] * 3.7) + 
                           0.3 * np.sin(x[i] * 7.1)) * np.cos(x[i] * 0.8)
        
        # Quadratic baseline with asymmetric weighting
        quadratic = 0.0
        for i in range(self.dim):
            if x[i] >= 0:
                quadratic += 0.5 * x[i]**2
            else:
                quadratic += 0.7 * x[i]**2
        
        # Combine all terms
        result = 1.5 * barrier + 0.8 * trig_coupling + 0.6 * power_decay + 0.4 * modal_terms + 0.3 * quadratic
        
        return result