import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic component using logistic map dynamics
        chaotic_term = 0.0
        for i in range(self.dim):
            # Use delayed feedback with varying delay
            if i >= 2:
                delayed_val = x_norm[i-2]
            else:
                delayed_val = x_norm[i] * 0.5
            
            # Logistic map with parameter control
            r = 3.9 + 0.1 * np.sin(0.5 * x_norm[i])
            chaotic_term += r * x_norm[i] * (1 - x_norm[i]) + 0.2 * delayed_val * (1 - delayed_val)
        
        # Saddle-point dominant polynomial with mixed signs
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += (x_norm[i]**3 - 3 * x_norm[i]**2 + 2 * x_norm[i]) * np.cos(5 * x_norm[i])
            
        # Radial basis function with multiple centers and varying widths
        rbf_term = 0.0
        centers = np.linspace(-1, 1, min(5, self.dim))
        for i in range(self.dim):
            dist = 0.0
            for c in centers:
                dist += np.exp(-20 * (x_norm[i] - c)**2)
            rbf_term += dist
            
        # Non-separable interaction with trigonometric coupling and variable phase shifts
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_shift = 0.3 * np.sin(0.7 * (i + j))
                interaction_term += np.sin(8 * (x_norm[i] + x_norm[j]) + phase_shift) * \
                                   np.cos(4 * (x_norm[i] - x_norm[j]) + phase_shift) * \
                                   (1 + 0.2 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Combine all terms with dynamic weights
        result = 0.5 * np.sum(x_norm**2) + 0.7 * chaotic_term + 0.4 * saddle_term + \
                 0.3 * rbf_term + 0.6 * interaction_term
        
        return result