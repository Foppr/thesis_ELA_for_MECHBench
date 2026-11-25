import numpy as np

class RadialChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic frequencies and adaptive parameters
        self.frequencies = 2.0 + 3.0 * np.random.rand(dim)
        self.adaptive_factors = 1.0 + 2.0 * np.random.rand(dim)
        self.penalty_weights = 0.5 + 1.5 * np.random.rand(dim)
        self.center_offsets = np.random.uniform(-1.0, 1.0, dim)
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Radial basis function component with chaotic modulation
        rbf_sum = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Chaotic modulation of RBF centers
            center = np.sin(self.frequencies[i] * xi + self.center_offsets[i])
            rbf_sum += np.exp(-self.adaptive_factors[i] * (xi - center)**2)
        
        # Gradient-based component with adaptive scaling
        grad_term = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Adaptive gradient scaling based on chaotic factors
            grad_scale = 1.0 + 0.5 * np.sin(self.frequencies[i] * xi)
            grad_term += grad_scale * xi**3
        
        # Chaotic frequency coupling between dimensions
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_coupling = np.sin(self.frequencies[i] * x_scaled[j] + 
                                     self.frequencies[j] * x_scaled[i])
                coupling_term += freq_coupling * (x_scaled[i]**2 + x_scaled[j]**2)
        
        # Dynamic penalty component with chaotic weight adjustment
        penalty_term = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Chaotic adjustment of penalty weights
            weight_adjust = 1.0 + 0.3 * np.sin(self.frequencies[i] * xi)
            penalty_term += self.penalty_weights[i] * weight_adjust * \
                           np.exp(-0.5 * (xi - 0.5)**2) * (xi**4)
        
        # Multi-scale oscillatory component with adaptive amplitude
        oscillatory_term = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Adaptive amplitude based on chaotic modulation
            amp = 1.0 + 0.8 * np.sin(self.frequencies[i] * xi)
            oscillatory_term += amp * np.sin(8 * xi) * np.cos(5 * xi)
        
        # Cross-dimensional interaction with hyperbolic tangent coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.tanh(x_scaled[i] * x_scaled[j]) * \
                             np.sin(self.frequencies[i] * x_scaled[j])
        
        # Add a global conditioning component with chaotic scaling
        condition_term = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Chaotic scaling factor
            scale_factor = 1.0 + 0.7 * np.sin(self.frequencies[i] * xi)
            condition_term += scale_factor * xi**4
        
        # Combine all components with carefully tuned weights
        return 0.3 * rbf_sum + 0.25 * grad_term + 0.2 * coupling_term + \
               0.15 * penalty_term - 0.1 * oscillatory_term + 0.08 * cross_term + \
               0.07 * condition_term