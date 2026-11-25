import numpy as np

class ChaoticDelayedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic system parameters
        self.lambda_params = np.random.uniform(0.1, 0.9, dim)
        self.delay_params = np.random.randint(1, 6, dim)
        self.feedback_strength = np.random.uniform(0.5, 2.0, dim)
        self.bifurcation_points = np.random.uniform(-2.0, 2.0, dim)
        # Saddle-node bifurcation control
        self.saddle_strength = np.random.uniform(0.1, 1.0, dim)
        # Time-delayed interaction matrix
        self.delay_matrix = np.zeros((dim, dim))
        for i in range(dim):
            for j in range(dim):
                if i != j:
                    self.delay_matrix[i, j] = np.random.uniform(-0.3, 0.3) * np.exp(-abs(i-j)/max(1, dim/3))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize to [-1, 1] for chaotic computation
        normalized_x = x / 5.0
        
        # Compute chaotic dynamics with time delays
        chaotic_sum = np.zeros(self.dim)
        for i in range(self.dim):
            # Base chaotic map with delay feedback
            delayed_value = 0.0
            if self.delay_params[i] <= len(normalized_x):
                delayed_index = max(0, i - self.delay_params[i])
                delayed_value = normalized_x[delayed_index]
            
            # Logistic-like chaotic dynamics with bifurcation control
            x_i = normalized_x[i]
            chaotic_component = (
                self.lambda_params[i] * x_i * (1.0 - x_i) + 
                self.feedback_strength[i] * delayed_value +
                self.bifurcation_points[i] * np.sin(x_i)
            )
            
            # Add saddle-node bifurcation terms
            chaotic_component += self.saddle_strength[i] * (x_i**2 - 1.0)**2
            
            # Add interaction effects from other dimensions
            for j in range(self.dim):
                if i != j:
                    chaotic_component += self.delay_matrix[i, j] * np.tanh(normalized_x[j])
            
            chaotic_sum[i] = chaotic_component
        
        # Compute fitness as sum of nonlinear combinations
        fitness = 0.0
        for i in range(self.dim):
            # Polynomial and exponential energy terms
            term1 = chaotic_sum[i]**2
            term2 = 0.5 * chaotic_sum[i]**3
            term3 = 0.1 * np.exp(-chaotic_sum[i]**2)
            
            # Add basin interaction terms
            basin_term = 0.0
            for j in range(self.dim):
                if i != j:
                    basin_term += np.exp(-((chaotic_sum[i] - chaotic_sum[j])**2) / 0.5)
            
            fitness += term1 + term2 + term3 + 0.3 * basin_term
        
        # Add global scaling and noise
        fitness = fitness / self.dim
        noise = np.random.uniform(-0.005, 0.005)
        return fitness + noise