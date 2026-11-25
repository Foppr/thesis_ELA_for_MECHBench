import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Logistic map parameters for chaos generation
        self.chaos_rates = np.random.uniform(3.5, 4.0, dim)
        self.chaos_initials = np.random.rand(dim) * 0.1 + 0.1
        # Radial basis function parameters
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, dim)
        self.rbf_weights = np.random.randn(dim)
        # Temporal coupling parameters
        self.time_coupling_strength = np.random.rand() * 0.5 + 0.1
        self.temporal_shifts = np.random.rand(dim) * np.pi * 2
        # Dynamic scaling factors
        self.dynamic_scale = np.random.rand() * 3.0 + 1.0
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Generate chaotic sequence for each dimension
        chaos_sequence = np.zeros_like(x_norm)
        for i in range(self.dim):
            # Initialize chaotic map
            chaos_val = self.chaos_initials[i]
            for _ in range(100):  # Discard initial transient
                chaos_val = self.chaos_rates[i] * chaos_val * (1 - chaos_val)
            # Generate a few iterations for the current point
            for _ in range(5):
                chaos_val = self.chaos_rates[i] * chaos_val * (1 - chaos_val)
            chaos_sequence[i] = chaos_val
            
        # Radial basis function component
        rbf_sum = 0.0
        for i in range(self.dim):
            dist = np.sum((x_norm - self.rbf_centers[i])**2)
            rbf_sum += self.rbf_weights[i] * np.exp(-dist / (2 * self.rbf_widths[i]**2))
        
        # Temporal coupling component with chaotic influence
        temporal_coupling = 0.0
        for i in range(self.dim):
            phase = self.temporal_shifts[i] + chaos_sequence[i] * np.pi
            temporal_coupling += np.sin(phase) * x_norm[i]
            
        # Dynamic scaling and mixed polynomial terms
        mixed_terms = 0.0
        for i in range(self.dim):
            mixed_terms += (x_norm[i]**3 + 0.5 * x_norm[i]**4 + 
                           0.3 * np.sin(3 * x_norm[i]) * np.cos(2 * x_norm[(i+1) % self.dim]))
        
        # Combine all components with dynamic scaling
        result = (self.dynamic_scale * rbf_sum + 
                 self.time_coupling_strength * temporal_coupling + 
                 0.5 * mixed_terms + 
                 1.0)
        
        return result