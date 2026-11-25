import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic map parameters for time-delayed feedback
        self.a = 3.9
        self.b = 0.1
        self.delay = min(3, dim // 2)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map dynamics with time-delayed feedback
        chaotic = 0.0
        for i in range(self.dim):
            if i >= self.delay:
                # Time-delayed feedback term
                feedback = self.a * np.abs(x[i] - x[i - self.delay]) - self.b
                chaotic += 0.5 * (x[i]**2 + feedback**2)
            else:
                chaotic += 0.5 * x[i]**2
                
        # Saddle-point dominance with high-frequency trigonometric terms
        saddle = 0.0
        for i in range(self.dim):
            saddle += (np.sin(10.0 * x[i]) * np.cos(15.0 * x[i]) + 
                      np.sin(20.0 * x[i]) * np.cos(25.0 * x[i]) +
                      0.5 * np.sin(30.0 * x[i])**2)
        
        # Ergodic radial basis components with multi-scale widths
        rbf = 0.0
        for i in range(self.dim):
            width = 1.0 + 0.5 * np.sin(i * 0.7)
            rbf += np.exp(-0.5 * ((x[i] - np.sin(i)) / width)**2)
            
        # Non-separable high-dimensional coupling with polynomial interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling += (x[i]**2 + x[j]**2) * np.sin(5.0 * (x[i] - x[j]))
                
        # Multi-modal component with chaotic perturbations
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += 0.3 * np.sin(8.0 * x[i]) * np.cos(9.0 * x[i]) + \
                         0.2 * np.sin(12.0 * x[i]) * np.cos(13.0 * x[i])
        
        # Combine all components with adaptive weights based on dimension
        adaptive_weight = 1.0 + 0.2 * np.log(self.dim + 1)
        
        return adaptive_weight * (0.4 * chaotic + 0.3 * saddle + 0.2 * rbf + 0.1 * coupling + 0.2 * multimodal)