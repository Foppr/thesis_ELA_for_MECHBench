import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic logistic map parameters for each dimension
        self.r_params = np.array([3.8 + 0.2 * np.sin(0.7 * np.pi * i) for i in range(dim)])
        # Precompute radial basis function centers and widths
        self.centers = np.random.uniform(-4.0, 4.0, (10, dim))
        self.widths = np.random.uniform(0.5, 2.0, 10)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic logistic map term with dynamic parameter modulation
        chaotic_term = 0.0
        for i in range(self.dim):
            r = self.r_params[i]
            # Simulate chaotic behavior using logistic map
            x_0 = np.sin(x[i]) * 0.5 + 0.5  # Normalize to [0,1]
            x_t = x_0
            for _ in range(10):  # Iterate to reach chaotic regime
                x_t = r * x_t * (1 - x_t)
            chaotic_term += x_t * np.exp(-0.1 * x[i]**2)
        chaotic_term /= self.dim
        
        # Radial basis function interpolation term
        rbf_term = 0.0
        for i in range(10):
            phi = np.exp(-np.sum(((x - self.centers[i]) ** 2) / (2 * self.widths[i]**2)))
            rbf_term += phi * np.sin(0.5 * np.pi * i)
        rbf_term /= 10.0
        
        # Adaptive penalty term based on distance to boundaries
        penalty_term = 0.0
        for i in range(self.dim):
            dist_to_bound = min(abs(x[i] - (-5.0)), abs(x[i] - 5.0))
            penalty_term += 10.0 * np.exp(-dist_to_bound)
        penalty_term /= self.dim
        
        # Cross-dimensional coupling with chaotic interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic interaction between dimensions
                interaction = np.sin(0.3 * (x[i] + x[j])) * np.cos(0.2 * (x[i] - x[j]))
                cross_term += interaction * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        cross_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Multi-scale oscillation with chaotic frequency modulation
        oscillation_term = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.5 * np.sin(0.4 * np.pi * i + 0.3 * np.sum(x))
            oscillation_term += np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i]) * np.exp(-0.08 * x[i]**2)
        oscillation_term /= self.dim
        
        # Dynamic conditioning term with time-varying weights
        dynamic_term = 0.0
        for i in range(self.dim):
            weight = 1.0 + 0.3 * np.cos(0.6 * np.pi * i + 0.2 * np.sum(x))
            dynamic_term += weight * (x[i]**4 - 2.0 * x[i]**2) * np.exp(-0.05 * x[i]**2)
        dynamic_term /= self.dim
        
        # Combine all terms with adaptive weights
        total = 0.3 * chaotic_term + 0.2 * rbf_term + 0.15 * penalty_term + \
                0.15 * cross_term + 0.1 * oscillation_term + 0.1 * dynamic_term
        
        return total