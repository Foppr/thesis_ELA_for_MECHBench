import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Spherical component with dynamic radius
        sphere_term = np.sum(x_norm**2) * (1 + 0.1 * np.sin(10 * np.sum(x_norm**2)))
        
        # Elliptic component with varying condition numbers
        elliptic_term = 0.0
        for i in range(self.dim):
            # Dynamic conditioning based on position
            cond_factor = 1 + 2 * abs(x_norm[i]) + 0.5 * np.sin(5 * x_norm[i])
            elliptic_term += cond_factor * x_norm[i]**2
        
        # Sinusoidal component with multiple frequencies and amplitudes
        sin_term = 0.0
        for i in range(self.dim):
            freq = 2 + i % 5
            amp = 1 + 0.3 * np.cos(3 * x_norm[i])
            sin_term += amp * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Cross-dimensional interaction with implicit constraint
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Implicit constraint: avoid regions where |x_i + x_j| < 0.1
                constraint_penalty = 1 + 10 * max(0, 0.1 - abs(x_norm[i] + x_norm[j]))
                cross_term += constraint_penalty * (x_norm[i]**2 + x_norm[j]**2) * \
                             np.sin(3 * np.pi * (x_norm[i] - x_norm[j])) * \
                             np.cos(2 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Multi-modal component with dynamic centers and varying heights
        modal_term = 0.0
        centers = np.linspace(-0.8, 0.8, min(5, self.dim))
        for i in range(self.dim):
            modal_sum = 0.0
            for center in centers:
                dist = abs(x_norm[i] - center)
                height = 1 + 0.5 * np.sin(4 * center)
                modal_sum += height * np.exp(-dist**2 / (2 * 0.1**2))
            modal_term += modal_sum
        
        # Asymmetric component with exponential weighting
        asym_term = 0.0
        for i in range(self.dim):
            if x_norm[i] > 0:
                asym_term += x_norm[i]**3 * np.exp(-x_norm[i]**2)
            else:
                asym_term += x_norm[i]**4 * np.exp(x_norm[i]**2)
        
        # Global modulation with periodic behavior
        global_mod = np.sin(5 * np.sum(x_norm**3)) * np.cos(3 * np.prod(x_norm))
        
        # Combine all terms with adaptive weights
        result = 0.6 * sphere_term + 0.4 * elliptic_term + 0.3 * sin_term + \
                 0.2 * cross_term + 0.5 * modal_term + 0.1 * asym_term + global_mod
        
        return result