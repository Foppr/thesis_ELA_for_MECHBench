import numpy as np

class ChaoticGradientSaddleLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-pi, pi] for chaotic behavior
        scaled_x = x * (np.pi / 5.0)
        
        # Base polynomial chaos component with chaotic interactions
        result = 0.0
        for i in range(self.dim):
            result += (x[i]**4) - 2*(x[i]**2) + np.sin(3 * scaled_x[i]) * np.cos(2 * scaled_x[i])
            
        # Add saddle point structures with varying curvature
        for i in range(self.dim):
            result += 0.5 * x[i] * np.sin(4 * scaled_x[i]) * np.cos(3 * scaled_x[i])
            
        # Introduce dynamic scaling based on dimensionality and input magnitude
        dynamic_scale = np.sum(np.abs(x)) / self.dim + 0.1
        
        # Add high-frequency chaotic oscillations
        for i in range(self.dim):
            result += 0.3 * np.sin(12 * scaled_x[i]) * np.cos(7 * scaled_x[i]) * dynamic_scale
            
        # Include cross-dimension coupling with chaotic interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * np.sin(scaled_x[i] * scaled_x[j]) * (x[i]**2 + x[j]**2)
                
        # Add global minimum shift and penalty terms
        result += 0.15 * np.sum(x**3) + 0.05 * dynamic_scale**3
        
        # Introduce a small chaotic perturbation term
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_term += np.sin(10 * scaled_x[i]) * np.cos(9 * scaled_x[i])
        result += 0.2 * chaos_term
        
        return result