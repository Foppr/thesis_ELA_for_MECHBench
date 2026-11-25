import numpy as np

class HyperSphericalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to unit sphere for hyper-spherical behavior
        norm = np.linalg.norm(x)
        if norm == 0:
            normalized_x = x
        else:
            normalized_x = x / norm
            
        # Base hyper-spherical component with chaotic modulation
        result = 0.0
        for i in range(self.dim):
            result += (np.sin(3 * x[i]) * np.cos(2 * x[i]) * 
                      np.sin(5 * x[i]) + 0.4 * np.sin(8 * x[i]))
            
        # Add saddle point structure with alternating concavity
        for i in range(self.dim):
            result += 0.3 * (x[i]**3 - 3 * x[i] * np.cos(x[i]) + 
                           2 * np.sin(4 * x[i])**2)
            
        # Introduce dynamic scaling based on dimensionality and norm
        dynamic_scale = np.sum(np.abs(x)) / self.dim + 0.1 * norm
        
        # Add high-frequency chaotic oscillations
        for i in range(self.dim):
            result += 0.5 * np.sin(15 * x[i]) * np.cos(10 * x[i]) * np.sin(7 * x[i])
            
        # Add global minimum with penalty terms and enhanced curvature
        result += 0.2 * np.sum(x**2) + 0.1 * dynamic_scale**4
        
        # Include cross-dimension interactions with hyper-spherical coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.05 * np.sin(x[i] * x[j]) * np.cos(3 * (x[i] - x[j]))
                
        # Add a small shift to the global minimum to increase challenge
        result += 0.08 * np.sum(np.sin(0.3 * x) * np.cos(0.2 * x))
        
        # Add chaotic perturbation term for increased algorithmic difficulty
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_term += np.sin(x[i] + 0.15 * np.sin(x[(i+1) % self.dim]))
        result += 0.3 * chaos_term**2
        
        # Add hyper-spherical constraint effect
        result += 0.1 * (norm - 1.0)**2
        
        return result