import numpy as np

class CorrelatedBarrierSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize correlation matrix with exponential decay
        self.correlation_matrix = np.zeros((dim, dim))
        for i in range(dim):
            for j in range(dim):
                self.correlation_matrix[i, j] = np.exp(-0.5 * (i - j)**2 / (0.5 * dim)**2)
        
        # Barrier parameters
        self.barrier_heights = np.random.uniform(1.0, 3.0, dim)
        self.barrier_widths = np.random.uniform(0.5, 2.0, dim)
        
        # Saddle parameters
        self.saddle_strengths = np.random.uniform(0.5, 2.0, dim)
        self.saddle_positions = np.random.uniform(-3.0, 3.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Correlated multimodal component
        correlated_multimodal = 0
        for i in range(self.dim):
            # Exponentially decaying correlation with other dimensions
            corr_term = 0
            for j in range(self.dim):
                corr_term += self.correlation_matrix[i, j] * (x[j] - self.saddle_positions[j])**2
            
            # Add multimodal behavior with barrier regions
            barrier = self.barrier_heights[i] * np.exp(-0.5 * ((x[i] - self.saddle_positions[i]) / self.barrier_widths[i])**2)
            multimodal = 0.5 * (x[i] - self.saddle_positions[i])**4 + corr_term
            
            correlated_multimodal += barrier + multimodal
            
        # Logarithmic barrier component
        log_barrier = 0
        for i in range(self.dim):
            log_barrier += 0.3 * np.log(np.abs(x[i]) + 1) + 0.2 * np.sin(x[i])
            
        # Saddle-point attractor component
        saddle_attractor = 0
        for i in range(self.dim):
            saddle_attractor += self.saddle_strengths[i] * (x[i]**3 - 3*x[i]) + 0.1 * x[i]**5
            
        # Cross-dimension interaction with logarithmic scaling
        cross_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += np.log(np.abs(x[i] - x[j]) + 1) * np.sin(2.0 * (x[i] + x[j]))
                
        # Combine all components with configurable weights
        result = 1.5 * correlated_multimodal + 1.0 * log_barrier + 0.8 * saddle_attractor + 0.6 * cross_interaction
        
        return result