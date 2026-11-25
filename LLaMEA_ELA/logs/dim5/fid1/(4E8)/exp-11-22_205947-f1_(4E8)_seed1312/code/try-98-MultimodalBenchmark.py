import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic map parameters for time-delayed feedback
        self.a = 4.5
        self.b = 0.2
        self.delay = min(5, dim // 3)
        
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
            saddle += (np.sin(15.0 * x[i]) * np.cos(20.0 * x[i]) + 
                      np.sin(30.0 * x[i]) * np.cos(40.0 * x[i]) +
                      0.7 * np.sin(50.0 * x[i])**2)
        
        # Ergodic radial basis components with multi-scale widths
        rbf = 0.0
        for i in range(self.dim):
            width = 1.5 + 0.4 * np.sin(i * 1.2)
            rbf += np.exp(-0.5 * ((x[i] - np.sin(i * 0.7)) / width)**2)
            
        # Non-separable high-dimensional coupling with polynomial interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                coupling += (x[i]**4 + x[j]**4) * np.sin(8.0 * (x[i] - x[j]))
                
        # Multi-modal component with chaotic perturbations
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += 0.5 * np.sin(12.0 * x[i]) * np.cos(13.0 * x[i]) + \
                         0.4 * np.sin(18.0 * x[i]) * np.cos(19.0 * x[i]) + \
                         0.3 * np.sin(25.0 * x[i])**3
            
        # Quaternion-inspired terms for enhanced complexity
        quaternion = 0.0
        for i in range(0, self.dim - 3, 4):
            if i + 3 < self.dim:
                q1, q2, q3, q4 = x[i], x[i+1], x[i+2], x[i+3]
                quaternion += (q1**2 + q2**2 + q3**2 + q4**2) * np.sin(5.0 * (q1 + q2 + q3 + q4))
                
        # Combine all components with adaptive weights based on dimension
        adaptive_weight = 1.2 + 0.4 * np.log(self.dim + 1)
        
        return adaptive_weight * (0.3 * chaotic + 0.3 * saddle + 0.15 * rbf + 0.2 * coupling + 0.2 * multimodal + 0.15 * quaternion)