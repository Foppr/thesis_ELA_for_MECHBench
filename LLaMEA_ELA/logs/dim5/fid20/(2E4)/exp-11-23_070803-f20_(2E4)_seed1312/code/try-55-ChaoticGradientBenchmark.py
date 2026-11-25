import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] 
        x_norm = x / 5.0
        
        # Chaotic gradient component using logistic map modulation
        chaotic_term = 0
        r = 3.9  # Chaos parameter
        for i in range(self.dim):
            # Logistic map for chaotic behavior
            x_log = 0.5
            for _ in range(10):  # Iterate to stabilize
                x_log = r * x_log * (1 - x_log)
            # Use chaotic value as modulation factor
            mod_factor = 1 + 0.3 * np.sin(10 * x_norm[i]) * x_log
            chaotic_term += (x_norm[i]**2) * mod_factor
        
        # Composite sinusoidal modulation with frequency coupling
        sin_term = 0
        for i in range(self.dim):
            freq = 2 + 3 * np.sin(x_norm[i] * 0.5)
            amp = 1 + 0.5 * np.cos(x_norm[i])
            sin_term += amp * np.sin(freq * x_norm[i]) * \
                       (1 + 0.2 * np.sin(3 * x_norm[i]))
        
        # Adaptive basin structure with dynamic depth
        basin_term = 0
        for i in range(self.dim):
            # Dynamic basin depth based on position
            depth = 1 + 0.5 * np.cos(x_norm[i] * 2)
            basin_term += depth * (x_norm[i]**4 - 2 * x_norm[i]**2) * \
                         (1 + 0.3 * np.sin(5 * x_norm[i]))
        
        # Cross-dimensional interaction with time-delayed feedback
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Extended coupling
                # Time-delayed interaction with phase shift
                delay = np.sin(x_norm[i] + x_norm[j])
                coupling = (x_norm[i]**2 + x_norm[j]**2) * \
                          np.cos(3 * x_norm[i] - 2 * x_norm[j] + delay)
                cross_term += coupling
        
        # Combine all components with dynamic weights
        result = 1.5 * chaotic_term + 1.3 * sin_term + 1.1 * basin_term + 0.8 * cross_term
        
        # Add small random noise for non-determinism
        noise = np.random.normal(0, 0.001)
        
        return result + noise