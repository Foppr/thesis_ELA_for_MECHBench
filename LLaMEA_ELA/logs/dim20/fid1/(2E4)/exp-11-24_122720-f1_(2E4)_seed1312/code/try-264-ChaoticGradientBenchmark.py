import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for varying landscape complexity
        self.chaos_params = [0.5 + 0.5 * np.sin(i * np.pi / (dim + 1)) for i in range(dim)]
        self.asymmetry = [0.4 * np.cos(i * np.pi / (dim + 2)) for i in range(dim)]
        self.curvature_mod = [1.2 + 0.5 * np.sin(i * np.pi / (dim + 3)) for i in range(dim)]
        # Additional multi-scale modulation for increased complexity
        self.multi_scale = [0.3 * np.sin(i * np.pi / (dim + 4)) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic gradient component with varying influence
        chaotic_grad = 0
        for i in range(self.dim):
            chaos = self.chaos_params[i]
            asym = self.asymmetry[i]
            curvature = self.curvature_mod[i]
            scale = self.multi_scale[i]
            term = x[i]**3 + asym * x[i]**2 + chaos * np.sin(x[i]) + scale * x[i]**4
            chaotic_grad += curvature * term
            
        # Saddle point structure with asymmetric basins and multi-scale features
        saddle_term = 0
        for i in range(self.dim):
            saddle_term += (x[i]**4 - 2 * x[i]**2) * (1 + 0.3 * np.cos(i) + 0.15 * np.sin(i**2))
            
        # Asymmetric curvature modulation with multi-scale effects
        mod_term = 0
        for i in range(self.dim):
            mod_term += (x[i]**2 + 0.6 * x[i]) * (1 + self.asymmetry[i] * np.sin(x[i])) * (1 + self.multi_scale[i] * np.cos(x[i]))
            
        # Adaptive scaling based on dimensionality with additional chaotic modulation
        scale_factor = 1.0 + 0.4 * np.log(self.dim + 1) + 0.15 * np.sin(self.dim * np.pi / 4)
        
        # Combine all components with proper weighting and add noise-like perturbation
        result = scale_factor * (chaotic_grad + saddle_term + mod_term) + 0.15 * self.dim
        
        # Add a small chaotic perturbation to increase landscape irregularity
        perturbation = 0.06 * np.sum([np.sin(x[i] * (i+1)) for i in range(self.dim)])
        
        # Introduce enhanced chaotic modulation and improved fitness shaping
        enhanced_term = 0
        for i in range(self.dim):
            enhanced_term += (x[i]**5 - 3*x[i]**3 + 2*x[i]) * np.cos(x[i] * (i+1)) * (1 + 0.15 * np.sin(i))
        
        return result + perturbation + 0.03 * enhanced_term