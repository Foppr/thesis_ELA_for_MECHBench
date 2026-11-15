import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.r = 3.95
        self.x0 = 0.5
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Initialize chaotic sequence
        chaotic_seq = np.zeros(self.dim)
        x_current = self.x0
        
        # Generate chaotic sequence using logistic map
        for i in range(self.dim):
            x_current = self.r * x_current * (1 - x_current)
            chaotic_seq[i] = x_current
            
        # Create multimodal landscape using chaotic sequence and trigonometric terms
        result = 0.0
        for i in range(self.dim):
            # Chaotic modulation
            modulator = 1.0 + 0.5 * np.sin(10 * chaotic_seq[i])
            
            # Quadratic term with chaotic modulation
            result += modulator * (x_norm[i] ** 2)
            
            # Add sinusoidal interaction terms
            for j in range(i+1, min(i+4, self.dim)):
                result += 0.3 * np.sin(5 * x_norm[i]) * np.cos(3 * x_norm[j])
                
        # Add coupling between dimensions
        coupling = 0.1 * np.sum(np.sin(x_norm) * np.cos(2 * x_norm))
        
        # Add a global shift to increase complexity
        shift = 0.05 * np.sum(x_norm ** 3)
        
        return result + coupling + shift