import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for varying landscape complexity
        self.chaos_params = [0.5 + 0.5 * np.sin(i * np.pi / (dim + 1)) for i in range(dim)]
        self.asymmetry = [0.3 * np.cos(i * np.pi / (dim + 2)) for i in range(dim)]
        self.curvature_mod = [1.0 + 0.6 * np.sin(i * np.pi / (dim + 3)) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic gradient component with higher-order terms
        chaotic_grad = 0
        for i in range(self.dim):
            chaos = self.chaos_params[i]
            asym = self.asymmetry[i]
            curvature = self.curvature_mod[i]
            term = x[i]**5 + asym * x[i]**4 + chaos * np.sin(x[i]) + 0.1 * x[i]**3
            chaotic_grad += curvature * term
            
        # Enhanced saddle point structure with cross-terms
        saddle_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                saddle_term += (x[i]**2 - x[j]**2) * np.cos(0.5 * (x[i] + x[j]))
                
        # Modified curvature modulation with exponential scaling
        mod_term = 0
        for i in range(self.dim):
            mod_term += (x[i]**3 - 0.5 * x[i]**2) * np.exp(-0.1 * abs(x[i])) * (1 + self.asymmetry[i] * np.sin(x[i]))
            
        # Adaptive scaling based on dimensionality with logarithmic correction
        scale_factor = 1.0 + 0.3 * np.log(self.dim + 1) + 0.05 * np.sin(self.dim * np.pi / 4)
        
        # Combine all components with proper weighting
        return scale_factor * (chaotic_grad + saddle_term + mod_term) + 0.1 * self.dim