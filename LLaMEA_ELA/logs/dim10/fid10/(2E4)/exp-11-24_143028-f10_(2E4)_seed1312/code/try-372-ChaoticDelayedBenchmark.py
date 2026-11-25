import numpy as np

class ChaoticDelayedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic system parameters with higher complexity
        self.lambda_params = np.random.uniform(0.8, 1.2, dim)
        self.delay_params = np.random.randint(2, 8, dim)
        self.feedback_strength = np.random.uniform(1.0, 3.0, dim)
        self.bifurcation_points = np.random.uniform(-3.0, 3.0, dim)
        # Saddle-node bifurcation control with adaptive scaling
        self.saddle_strength = np.random.uniform(0.5, 2.0, dim)
        # Time-delayed interaction matrix with non-uniform coupling
        self.delay_matrix = np.zeros((dim, dim))
        for i in range(dim):
            for j in range(dim):
                if i != j:
                    self.delay_matrix[i, j] = np.random.uniform(-0.5, 0.5) * np.exp(-abs(i-j)/max(1, dim/4)) * (1 + 0.3 * np.sin(i*j))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize to [-1, 1] for chaotic computation
        normalized_x = x / 5.0
        
        # Compute chaotic dynamics with time delays and hyperchaos
        chaotic_sum = np.zeros(self.dim)
        for i in range(self.dim):
            # Base hyperchaotic map with delay feedback and multiple attractors
            delayed_value = 0.0
            if self.delay_params[i] <= len(normalized_x):
                delayed_index = max(0, i - self.delay_params[i])
                delayed_value = normalized_x[delayed_index]
            
            # Hyperchaotic dynamics with multiple bifurcation points
            x_i = normalized_x[i]
            chaotic_component = (
                self.lambda_params[i] * x_i * (1.0 - x_i**2) + 
                self.feedback_strength[i] * delayed_value +
                self.bifurcation_points[i] * np.sin(3.0 * x_i) +
                0.5 * self.bifurcation_points[i] * np.cos(2.0 * x_i)
            )
            
            # Add saddle-node bifurcation terms with adaptive scaling
            chaotic_component += self.saddle_strength[i] * (x_i**4 - 2.0*x_i**2 + 1.0)
            
            # Add interaction effects from other dimensions with non-linear coupling
            for j in range(self.dim):
                if i != j:
                    coupling = self.delay_matrix[i, j] * np.tanh(normalized_x[j])
                    chaotic_component += coupling * (1 + 0.2 * np.sin(0.5 * i * j))
            
            chaotic_sum[i] = chaotic_component
        
        # Compute fitness as sum of nonlinear combinations with enhanced basin interactions
        fitness = 0.0
        for i in range(self.dim):
            # Enhanced polynomial and exponential energy terms
            term1 = chaotic_sum[i]**2
            term2 = 0.3 * chaotic_sum[i]**4
            term3 = 0.15 * np.exp(-chaotic_sum[i]**2)
            term4 = 0.05 * np.sin(5.0 * chaotic_sum[i])
            
            # Add enhanced basin interaction terms with multiple basins
            basin_term = 0.0
            for j in range(self.dim):
                if i != j:
                    distance = (chaotic_sum[i] - chaotic_sum[j])**2
                    basin_term += np.exp(-distance / 0.3) * (1 + 0.1 * np.cos(0.7 * i * j))
            
            fitness += term1 + term2 + term3 + term4 + 0.4 * basin_term
        
        # Add global scaling and enhanced noise
        fitness = fitness / self.dim
        noise = np.random.uniform(-0.01, 0.01) * (1 + 0.5 * np.sin(np.sum(x)))
        return fitness + noise