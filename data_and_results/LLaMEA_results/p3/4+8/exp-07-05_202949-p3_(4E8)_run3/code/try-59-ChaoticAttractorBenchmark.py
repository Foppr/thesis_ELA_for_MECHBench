import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for different dimensions
        self.chaotic_params = np.random.uniform(0.1, 0.9, dim)
        self.shifts = np.random.uniform(-2.0, 2.0, dim)
        self.frequency_mod = np.random.uniform(1.0, 5.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic with chaotic scaling
        result = 0.0
        for i in range(self.dim):
            # Chaotic scaling factor based on dimension
            scale = self.chaotic_params[i] * (1.0 + 0.1 * np.sin(x[i]))
            result += scale * (x[i] - self.shifts[i])**2
        
        # Fractional Brownian motion-like irregularities
        fbm_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x[i] - x[j])
                # Fractional scaling with Hurst exponent effect
                fbm_term += (0.5 + 0.5 * np.sin(distance * self.frequency_mod[i])) * (distance ** 1.3)
        result += 0.1 * fbm_term
        
        # Nested attractor structure with varying depths
        attractor_term = 0.0
        for i in range(self.dim):
            # Multiple nested minima with different depths
            attractor_term += 0.3 * np.sin(2.0 * x[i]) * np.cos(3.0 * x[i]) + \
                             0.2 * np.sin(5.0 * x[i]) * np.cos(7.0 * x[i]) + \
                             0.1 * np.sin(11.0 * x[i])
        result += attractor_term
        
        # Dynamic global minimum based on dimension
        dynamic_min = np.sum(np.sin(np.arange(1, self.dim + 1) * 0.5) * x)
        result += 0.05 * dynamic_min**2
        
        # Add a complex, non-separable interaction term
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
        result += 0.02 * interaction
        
        # Add a periodic modulation that changes with dimension
        periodic = 0.0
        for i in range(self.dim):
            periodic += np.sin(self.frequency_mod[i] * x[i]) * np.cos(self.frequency_mod[i] * x[i] * 0.5)
        result += 0.08 * periodic
        
        return result