import numpy as np

class ChaoticMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logarithmic barrier terms preventing boundary crossing
        barrier = 0.0
        for i in range(self.dim):
            barrier += 1.0 / (1.0 + np.exp(-12.0 * (x[i] - 5.0))) + 1.0 / (1.0 + np.exp(12.0 * (x[i] + 5.0)))
        
        # Trigonometric coupling between dimensions with altered frequencies
        trig_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                trig_coupling += np.sin(x[i] * x[j] * 0.7) * np.cos((x[i] + x[j]) * 0.5)
        
        # Power-law decay interactions with varying exponents
        power_decay = 0.0
        for i in range(self.dim):
            power_decay += (1.0 / (1.0 + np.abs(x[i])**4.0)) * np.sin(x[i] * 2.5)**2
        
        # Multi-modal sinusoidal components with varying frequencies and amplitudes
        modal_terms = 0.0
        for i in range(self.dim):
            modal_terms += (np.sin(x[i] * 1.5) + 0.6 * np.sin(x[i] * 4.2) + 
                           0.4 * np.sin(x[i] * 8.3)) * np.cos(x[i] * 1.1)
        
        # Quadratic baseline with asymmetric weighting
        quadratic = 0.0
        for i in range(self.dim):
            if x[i] >= 0:
                quadratic += 0.6 * x[i]**2
            else:
                quadratic += 0.8 * x[i]**2
        
        # Add chaotic component with exponential weighting
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.exp(-np.abs(x[i])) * np.sin(x[i] * 3.0)
        
        # Combine all terms
        result = 1.8 * barrier + 0.9 * trig_coupling + 0.7 * power_decay + 0.5 * modal_terms + 0.4 * quadratic + 0.2 * chaotic
        
        return result