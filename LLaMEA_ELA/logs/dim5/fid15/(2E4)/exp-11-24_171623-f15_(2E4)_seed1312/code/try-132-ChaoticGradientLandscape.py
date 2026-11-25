import numpy as np

class ChaoticGradientLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay components with chaotic modulation
        exp_sum = 0.0
        for i in range(self.dim):
            exp_sum += np.exp(-np.abs(x_norm[i]) * (1 + 0.5 * np.sin(x_norm[i] * 10.0)))
        
        # Trigonometric coupling between dimensions with dynamic phase shifts
        trig_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                phase_shift = np.sin(x_norm[i] * x_norm[j] * 7.0)
                trig_coupling += np.cos(x_norm[i] * x_norm[j] * 5.0 + phase_shift) * \
                                (1 + 0.3 * np.sin(x_norm[i] * 2.0)) * \
                                (1 + 0.3 * np.sin(x_norm[j] * 2.0))
        
        # Adaptive gradient modulation with polynomial conditioning
        grad_mod = 0.0
        for i in range(self.dim):
            grad_mod += (x_norm[i]**3) * (1 + 0.2 * np.cos(x_norm[i] * 8.0)) * \
                       np.exp(-0.5 * x_norm[i]**2)
        
        # Sharp ridge structure with hyperbolic tangent smoothing
        ridge_sum = 0.0
        for i in range(self.dim):
            ridge_sum += np.tanh(x_norm[i] * 3.0) * (x_norm[i]**2 - 1)**2
        
        # Chaotic scaling factor based on global input configuration
        chaos_scale = 1.0 + 0.4 * np.sin(np.sum(x_norm**3) * 3.0)
        
        # Combine all components with varying weights
        result = 0.25 * exp_sum + 0.3 * trig_coupling + 0.25 * grad_mod + 0.2 * ridge_sum
        
        return result * chaos_scale * (1 + 0.15 * np.sum(np.abs(x_norm)))