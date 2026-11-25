import numpy as np

class AdaptiveNeuralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize adaptive parameters for each dimension
        self.adaptive_params = np.random.uniform(0.5, 2.0, dim)
        self.neural_weights = np.random.normal(0, 1, (dim, dim))
        self.bias = np.random.normal(0, 0.5, dim)
        self.dimensionality_reduction = np.random.uniform(0.1, 0.9, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Neural network-inspired fitness shaping
        neural_output = np.tanh(np.dot(self.neural_weights, x) + self.bias)
        neural_term = np.sum(neural_output**2) / self.dim
        
        # Self-adaptive genetic algorithm components
        adaptive_term = 0.0
        for i in range(self.dim):
            adaptive_factor = self.adaptive_params[i]
            adaptive_term += (x[i]**4 - adaptive_factor * x[i]**2 + adaptive_factor**2) * np.exp(-0.1 * x[i]**2)
        adaptive_term /= self.dim
        
        # Dynamic dimensionality reduction effect
        reduced_dim = int(np.ceil(self.dim * np.mean(self.dimensionality_reduction)))
        if reduced_dim < self.dim:
            # Apply dimensionality reduction with varying importance
            dim_weights = np.sort(np.abs(x))[::-1][:reduced_dim]
            dim_term = np.sum(dim_weights**2) / reduced_dim
        else:
            dim_term = np.sum(x**2) / self.dim
            
        # Multi-scale oscillation with neural feedback
        feedback_term = 0.0
        for i in range(self.dim):
            feedback_freq = 1.5 + 0.5 * np.sin(0.3 * np.pi * i)
            feedback_term += np.sin(feedback_freq * x[i]) * np.cos(feedback_freq * x[i]) * np.exp(-0.05 * x[i]**2)
        feedback_term /= self.dim
        
        # Cross-dimensional coupling with adaptive strength
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.6 + 0.4 * np.sin(0.5 * np.pi * (i + j))
                cross_term += coupling_strength * np.sin(x[i] + x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        cross_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Evolving basin structure with time-varying parameters
        basin_term = 0.0
        for i in range(self.dim):
            basin_factor = 2.0 + 0.8 * np.cos(0.4 * np.pi * i + 0.1 * np.sum(x))
            basin_term += (basin_factor * x[i]**3 - 3.0 * x[i]) * np.exp(-0.1 * x[i]**2)
        basin_term /= self.dim
        
        # Fitness shaping with dynamic scaling
        scaling = np.mean(np.abs(x)) + 1.0
        total = (neural_term + adaptive_term + dim_term + feedback_term + 
                cross_term + basin_term) / scaling
        
        return total