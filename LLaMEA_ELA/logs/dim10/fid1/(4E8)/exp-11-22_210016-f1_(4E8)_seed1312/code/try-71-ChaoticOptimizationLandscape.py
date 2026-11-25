import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Adaptive radial component with variable decay rates and multi-scale modulations
        r = np.sqrt(np.sum(x**2))
        radial_term = np.exp(-r / (2.0 + 0.5 * np.sin(r * 0.3))) * (1.0 + 0.6 * np.sin(r * 2.0) * np.cos(r * 1.5))
        
        # Multi-frequency trigonometric interference with amplitude modulation
        trig_term = 0.0
        frequencies = [1.2, 2.8, 4.1, 5.7]
        for i, freq in enumerate(frequencies):
            trig_term += np.sum(np.sin(freq * x) * np.cos(freq * x * 0.7) * (1.0 + 0.3 * np.sin(i * r * 0.5)))
        
        # Enhanced chaotic component with nested coupling and dynamic weights
        chaotic_term = 0.0
        for i in range(self.dim):
            if i < self.dim - 2:
                chaotic_term += np.sin(x[i] * x[i+1] * x[i+2]) * np.cos(x[i] + x[i+1] - x[i+2]) * (1.0 + 0.2 * np.sin(x[i]**2))
        
        # Multi-scale cross-term interactions with variable coupling strengths
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.5 + 0.3 * np.sin((i+j) * 0.5)
                cross_term += (x[i] * x[j] * (x[i]**2 + x[j]**2)) / (1.0 + np.abs(x[i] - x[j])**4) * coupling_strength
        
        # Higher-order polynomial with adaptive coefficients and mixed symmetry
        cubic_term = 0.0
        for i in range(self.dim):
            cubic_term += (0.12 * x[i]**3 + 0.05 * x[i]**4) * np.cos(x[i] * 0.5)
        
        # Additional chaotic perturbation with time-varying parameters
        perturbation = 0.0
        for i in range(self.dim):
            perturbation += np.sin(10.0 * x[i]) * np.cos(7.0 * x[i]) * np.exp(-np.abs(x[i]) / 3.0)
        
        # Combine all terms with dynamic weighting based on dimensionality
        weight_radial = 1.0 + 0.2 * np.sin(self.dim * 0.1)
        weight_trig = 0.8 + 0.1 * np.cos(self.dim * 0.15)
        weight_chaotic = 0.4 + 0.1 * np.sin(self.dim * 0.2)
        weight_cross = 0.3 + 0.05 * np.cos(self.dim * 0.1)
        weight_cubic = 0.25 + 0.08 * np.sin(self.dim * 0.05)
        weight_perturbation = 0.1 + 0.03 * np.cos(self.dim * 0.25)
        
        result = (weight_radial * radial_term + 
                 weight_trig * trig_term + 
                 weight_chaotic * chaotic_term + 
                 weight_cross * cross_term + 
                 weight_cubic * cubic_term + 
                 weight_perturbation * perturbation)
        
        return result