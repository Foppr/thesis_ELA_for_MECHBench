import numpy as np

class ChaoticValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Exponential decay component with chaotic modulation - modified coefficients
        exp_term = 0.0
        for i in range(self.dim):
            decay = np.exp(-0.3 * (x[i] - 1.0)**2) * (1.0 + 0.4 * np.sin(4.0 * x[i]))
            exp_term += decay
        
        # Trigonometric coupling with dynamic phase shifts - modified frequencies
        trig_term = 0.0
        for i in range(self.dim):
            phase_shift = 0.6 * np.sin(i * 0.5 + 1.2)
            trig_term += np.cos(x[i] + phase_shift) * np.sin(3.0 * x[i] + phase_shift)
        
        # Asymmetric valley structure with dynamic depth - modified depths
        valley_term = 0.0
        for i in range(self.dim):
            # Create valleys with varying depths and positions
            valley1 = (x[i] - 1.2)**2 * np.exp(-0.4 * (x[i] - 1.5)**2)
            valley2 = (x[i] + 1.8)**4 * np.exp(-0.2 * (x[i] + 1.5)**2)
            # Dynamic scaling based on dimension
            depth_scale = 1.0 + 0.3 * np.sin(self.dim * 0.25 + i * 0.15)
            valley_term += depth_scale * (valley1 + valley2)
        
        # Saddle point structure with cross-dimensional interactions
        saddle_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Create saddle points through product of sinusoids
                saddle = np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.15 * (x[i]**2 + x[j]**2))
                saddle_term += saddle
        
        # Chaotic perturbation with recursive scaling - modified amplitude
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_mod = 1.0 + 0.15 * np.sin(8.0 * x[i] + 3.5 * np.cos(x[i]))
            chaos_term += chaos_mod * np.exp(-0.25 * x[i]**2) * np.sin(6.0 * x[i])
        
        # Cross-dimensional exponential coupling - modified strength
        cross_exp = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Exponential coupling with dynamic strength
                strength = 0.6 + 0.2 * np.sin(i * 0.35 + j * 0.25)
                cross_exp += strength * np.exp(-0.12 * (x[i] - x[j])**2) * (x[i]**2 + x[j]**2)
        
        # Final combination with adaptive weights
        total = 0.3 * exp_term + 0.18 * trig_term + 0.28 * valley_term + 0.12 * saddle_term + 0.12 * chaos_term + 0.08 * cross_exp
        
        # Global scaling factor with chaotic dimensionality effect
        scaling = 1.0 + 0.12 * np.sin(self.dim * 0.55) + 0.06 * np.cos(self.dim * 0.35)
        
        return total * scaling