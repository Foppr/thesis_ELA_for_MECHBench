import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic map parameters for time-delayed feedback
        self.a = 4.0
        self.b = 0.15
        self.delay = min(4, dim // 2)
        
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
            saddle += (np.sin(12.0 * x[i]) * np.cos(18.0 * x[i]) + 
                      np.sin(24.0 * x[i]) * np.cos(30.0 * x[i]) +
                      0.6 * np.sin(36.0 * x[i])**2)
        
        # Ergodic radial basis components with multi-scale widths
        rbf = 0.0
        for i in range(self.dim):
            width = 1.2 + 0.3 * np.sin(i * 0.8)
            rbf += np.exp(-0.5 * ((x[i] - np.sin(i)) / width)**2)
            
        # Non-separable high-dimensional coupling with polynomial interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling += (x[i]**3 + x[j]**3) * np.sin(6.0 * (x[i] - x[j]))
                
        # Multi-modal component with chaotic perturbations
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += 0.4 * np.sin(10.0 * x[i]) * np.cos(11.0 * x[i]) + \
                         0.3 * np.sin(15.0 * x[i]) * np.cos(16.0 * x[i])
        
        # Combine all components with adaptive weights based on dimension
        adaptive_weight = 1.0 + 0.3 * np.log(self.dim + 1)
        
        return adaptive_weight * (0.35 * chaotic + 0.35 * saddle + 0.2 * rbf + 0.15 * coupling + 0.25 * multimodal)