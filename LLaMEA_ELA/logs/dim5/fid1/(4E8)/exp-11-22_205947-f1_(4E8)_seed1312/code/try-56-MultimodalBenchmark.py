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
            r = 3.8 + 0.2 * np.sin(0.6 * x_norm[i])
            chaotic_term += r * x_norm[i] * (1 - x_norm[i]) + 0.15 * delayed_val * (1 - delayed_val)
        
        # Enhanced saddle-point dominant polynomial with mixed signs
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += (x_norm[i]**3 - 2.5 * x_norm[i]**2 + 1.8 * x_norm[i]) * np.cos(4.5 * x_norm[i])
            
        # Radial basis function with multiple centers and varying widths
        rbf_term = 0.0
        centers = np.linspace(-0.8, 0.8, min(4, self.dim))  # Modified centers
        for i in range(self.dim):
            dist = 0.0
            for c in centers:
                dist += np.exp(-15 * (x_norm[i] - c)**2)  # Different width
            rbf_term += dist
            
        # Non-separable interaction with trigonometric coupling and variable phase shifts
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_shift = 0.25 * np.sin(0.8 * (i + j))
                interaction_term += np.sin(9 * (x_norm[i] + x_norm[j]) + phase_shift) * \
                                   np.cos(3.5 * (x_norm[i] - x_norm[j]) + phase_shift) * \
                                   (1 + 0.15 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Combine all terms with dynamic weights
        result = 0.45 * np.sum(x_norm**2) + 0.75 * chaotic_term + 0.45 * saddle_term + \
                 0.35 * rbf_term + 0.65 * interaction_term
        
        return result