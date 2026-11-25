import numpy as np

class ChaoticValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Exponential decay component with chaotic modulation
        exp_term = 0.0
        for i in range(self.dim):
            decay = np.exp(-0.5 * (x[i] - 1.0)**2) * (1.0 + 0.3 * np.sin(3.0 * x[i]))
            exp_term += decay
        
        # Trigonometric coupling with dynamic phase shifts
        trig_term = 0.0
        for i in range(self.dim):
            phase_shift = 0.5 * np.sin(i * 0.4 + 1.0)
            trig_term += np.cos(x[i] + phase_shift) * np.sin(2.0 * x[i] + phase_shift)
        
        # Asymmetric valley structure with dynamic depth
        valley_term = 0.0
        for i in range(self.dim):
            # Create valleys with varying depths and positions
            valley1 = (x[i] - 1.5)**2 * np.exp(-0.5 * (x[i] - 1.5)**2)
            valley2 = (x[i] + 1.5)**4 * np.exp(-0.3 * (x[i] + 1.5)**2)
            # Dynamic scaling based on dimension
            depth_scale = 1.0 + 0.2 * np.sin(self.dim * 0.2 + i * 0.1)
            valley_term += depth_scale * (valley1 + valley2)
        
        # Saddle point structure with cross-dimensional interactions
        saddle_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Create saddle points through product of sinusoids
                saddle = np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                saddle_term += saddle
        
        # Chaotic perturbation with recursive scaling
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_mod = 1.0 + 0.1 * np.sin(7.0 * x[i] + 3.0 * np.cos(x[i]))
            chaos_term += chaos_mod * np.exp(-0.2 * x[i]**2) * np.sin(5.0 * x[i])
        
        # Cross-dimensional exponential coupling
        cross_exp = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Exponential coupling with dynamic strength
                strength = 0.5 + 0.3 * np.sin(i * 0.3 + j * 0.2)
                cross_exp += strength * np.exp(-0.1 * (x[i] - x[j])**2) * (x[i]**2 + x[j]**2)
        
        # Final combination with adaptive weights
        total = 0.25 * exp_term + 0.2 * trig_term + 0.25 * valley_term + 0.15 * saddle_term + 0.1 * chaos_term + 0.1 * cross_exp
        
        # Global scaling factor with chaotic dimensionality effect
        scaling = 1.0 + 0.1 * np.sin(self.dim * 0.5) + 0.05 * np.cos(self.dim * 0.3)
        
        return total * scaling