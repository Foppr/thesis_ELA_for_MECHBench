import numpy as np

class AdaptiveRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term with exponential decay
        quadratic_term = np.sum(x**2)
        exp_decay = np.exp(-0.1 * quadratic_term)
        
        # Sinusoidal modulations with adaptive frequencies
        sin_modulation = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(x[i] * 0.5)
            sin_modulation += np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Adaptive ridge structure with dynamic width
        ridge_term = 0.0
        for i in range(self.dim):
            # Dynamic width based on coordinate value
            width = 1.0 + 0.5 * np.tanh(x[i])
            ridge_term += (x[i] - np.sin(x[i]))**2 / (width**2 + 1e-8)
        
        # Multi-scale correlation structure with exponentially decaying weights
        corr_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Exponentially decaying correlation weight
                decay_weight = np.exp(-0.2 * abs(i - j))
                corr_term += decay_weight * (x[i] - x[j])**2
        
        # Non-separable interaction terms with polynomial coupling
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j])
        
        # Chaotic phase modulation with time-delayed feedback
        phase_term = 0.0
        for i in range(self.dim):
            delayed_idx = (i + self.dim//3) % self.dim
            phase_term += np.sin(x[i] + 0.5 * np.sin(x[delayed_idx])) * np.cos(x[i])
        
        # Dimensionality-dependent scaling factor
        dim_scale = 1.0 + 0.2 * np.log(self.dim + 1)
        
        return dim_scale * (0.3 * exp_decay * quadratic_term + 
                           0.2 * sin_modulation + 
                           0.2 * ridge_term + 
                           0.15 * corr_term + 
                           0.1 * poly_interaction + 
                           0.05 * phase_term)