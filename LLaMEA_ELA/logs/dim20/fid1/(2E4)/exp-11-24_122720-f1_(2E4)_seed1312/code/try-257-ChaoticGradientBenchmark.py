import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Slight mutation in chaotic parameters for varied landscape behavior
        self.chaos_params = [0.6 + 0.4 * np.sin(i * np.pi / (dim + 1.5)) for i in range(dim)]
        self.asymmetry = [0.3 * np.cos(i * np.pi / (dim + 2.5)) for i in range(dim)]
        self.curvature_mod = [1.1 + 0.5 * np.sin(i * np.pi / (dim + 2.2)) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic gradient component with varying influence
        chaotic_grad = 0
        for i in range(self.dim):
            chaos = self.chaos_params[i]
            asym = self.asymmetry[i]
            curvature = self.curvature_mod[i]
            term = x[i]**3 + asym * x[i]**2 + chaos * np.sin(x[i])
            chaotic_grad += curvature * term
            
        # Enhanced saddle point structure with stronger nonlinearity
        saddle_term = 0
        for i in range(self.dim):
            saddle_term += (x[i]**5 - 3 * x[i]**3 + 2 * x[i]) * (1 + 0.3 * np.cos(i))
            
        # Modified curvature modulation with cross-dimension interactions
        mod_term = 0
        for i in range(self.dim):
            mod_term += (x[i]**2 + 0.6 * x[i] + 0.1 * x[(i+1) % self.dim]**2) * (1 + self.asymmetry[i] * np.sin(x[i]))
            
        # Additional cross-dimension interaction term to increase conditioning
        cross_term = 0
        for i in range(self.dim):
            cross_term += 0.2 * x[i] * x[(i+1) % self.dim] * (1 + 0.1 * np.sin(i))
            
        # Adaptive scaling based on dimensionality
        scale_factor = 1.0 + 0.4 * np.log(self.dim + 1)
        
        # Combine all components with proper weighting
        return scale_factor * (chaotic_grad + saddle_term + mod_term + cross_term) + 0.15 * self.dim