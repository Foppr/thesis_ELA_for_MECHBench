import numpy as np

class CorrelatedBarrierSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize correlation matrix with exponential decay
        self.correlation_matrix = np.zeros((dim, dim))
        for i in range(dim):
            for j in range(dim):
                self.correlation_matrix[i, j] = np.exp(-0.5 * (i - j)**2 / (0.3 * dim)**2)
        
        # Barrier parameters
        self.barrier_heights = np.random.uniform(1.5, 3.5, dim)
        self.barrier_widths = np.random.uniform(0.3, 1.8, dim)
        
        # Saddle parameters
        self.saddle_strengths = np.random.uniform(0.7, 2.5, dim)
        self.saddle_positions = np.random.uniform(-4.0, 4.0, dim)
        
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
            multimodal = 0.7 * (x[i] - self.saddle_positions[i])**4 + 0.3 * corr_term
            
            correlated_multimodal += barrier + multimodal
            
        # Logarithmic barrier component
        log_barrier = 0
        for i in range(self.dim):
            log_barrier += 0.4 * np.log(np.abs(x[i]) + 1) + 0.15 * np.sin(1.5 * x[i])
            
        # Saddle-point attractor component with higher-order terms
        saddle_attractor = 0
        for i in range(self.dim):
            saddle_attractor += self.saddle_strengths[i] * (x[i]**3 - 4*x[i]) + 0.12 * x[i]**5
            
        # Cross-dimension interaction with modified logarithmic scaling
        cross_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += np.log(np.abs(x[i] - x[j]) + 0.5) * np.sin(1.5 * (x[i] + x[j]))
                
        # Combine all components with updated weights
        result = 1.3 * correlated_multimodal + 1.2 * log_barrier + 0.9 * saddle_attractor + 0.7 * cross_interaction
        
        return result