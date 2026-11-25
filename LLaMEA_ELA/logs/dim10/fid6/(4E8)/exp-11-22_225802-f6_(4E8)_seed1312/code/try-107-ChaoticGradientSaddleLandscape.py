import numpy as np

class ChaoticGradientSaddleLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-pi, pi] for enhanced chaotic behavior
        scaled_x = x * (np.pi / 5.0)
        
        # Base chaotic gradient component with polynomial chaos
        result = 0.0
        for i in range(self.dim):
            result += (0.8 * np.sin(scaled_x[i]) * np.cos(2.5 * scaled_x[i]) * 
                      np.sin(3.7 * scaled_x[i]) + 0.4 * np.sin(6.3 * scaled_x[i]))
            
        # Add saddle point structure with alternating concavity
        for i in range(self.dim):
            result += 0.6 * (x[i]**2 - 1.8 * x[i] * np.cos(scaled_x[i]) + 
                           1.2 * np.sin(2.8 * scaled_x[i])**2)
            
        # Introduce dynamic scaling based on dimensionality
        dynamic_scale = np.sum(np.abs(x)) / self.dim
        
        # Add high-frequency chaotic oscillations
        for i in range(self.dim):
            result += 0.5 * np.sin(11.3 * scaled_x[i]) * np.cos(8.7 * scaled_x[i]) * np.sin(5.2 * scaled_x[i])
            
        # Add global minimum with penalty terms and enhanced curvature
        result += 0.4 * np.sum(x**2) + 0.2 * dynamic_scale**3
        
        # Include cross-dimension interactions with chaotic coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * np.sin(scaled_x[i] * scaled_x[j]) * np.cos(3.5 * (scaled_x[i] - scaled_x[j]))
                
        # Add a small shift to the global minimum to increase challenge
        result += 0.15 * np.sum(np.sin(0.6 * x) * np.cos(0.4 * x))
        
        # Add chaotic perturbation term for increased algorithmic difficulty
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_term += np.sin(scaled_x[i] + 0.12 * np.sin(scaled_x[(i+1) % self.dim]))
        result += 0.3 * chaos_term**2
        
        return result