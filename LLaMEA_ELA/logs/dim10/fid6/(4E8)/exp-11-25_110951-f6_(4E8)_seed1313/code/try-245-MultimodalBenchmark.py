import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        
        # Asymmetric elliptic components with periodic modulation
        for i in range(self.dim):
            # Elliptic term with asymmetric scaling
            ellipse_term = (x_norm[i]**2 + 0.3 * np.sin(5 * x_norm[i])**2) / (1.0 + 0.1 * np.abs(x_norm[i]))
            
            # Periodic wave interference pattern
            wave1 = np.sin(10 * x_norm[i])
            wave2 = np.cos(15 * x_norm[i])
            wave3 = np.sin(25 * x_norm[i])
            
            # Interference with dynamic amplitude
            interference = (wave1 + 0.7 * wave2 + 0.3 * wave3) / (1.0 + 0.05 * x_norm[i]**2)
            
            result += ellipse_term + interference
            
        # Cross-dimensional coupling with asymmetric interaction terms
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Asymmetric coupling with phase shift and exponential weighting
                diff = x_norm[i] - x_norm[j]
                sum_val = x_norm[i] + x_norm[j]
                
                # Different weights for positive and negative differences
                weight = 0.5 * (1 + np.tanh(diff))  # Bias towards positive differences
                
                coupling += weight * np.sin(8 * diff) * np.cos(6 * sum_val) * \
                           np.exp(-0.2 * (diff**2 + sum_val**2))
        
        # Add coupling term with scaling factor
        result += 0.3 * coupling
        
        # High-frequency noise-like component for increased complexity
        noise = 0.0
        for i in range(self.dim):
            noise += (0.5 * np.sin(40 * x_norm[i]) + 
                     0.3 * np.cos(60 * x_norm[i]) + 
                     0.2 * np.sin(80 * x_norm[i]))
        
        # Global scaling based on distance from origin
        global_scale = 1.0 + 0.5 * np.exp(-0.1 * np.sum(x_norm**2))
        
        return result * global_scale + 0.2 * noise