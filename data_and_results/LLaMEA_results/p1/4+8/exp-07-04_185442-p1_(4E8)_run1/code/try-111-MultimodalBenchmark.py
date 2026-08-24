import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sine map component with varying parameters
        chaotic_term = np.sum(np.sin(10 * np.pi * x_norm * np.sin(5 * x_norm)))
        
        # Radial basis function with adaptive width
        rbfs = []
        for i in range(self.dim):
            center = np.sin(i * 0.5)
            width = 0.5 + 0.5 * np.sin(i * 0.3)
            rbfs.append(np.exp(-width * (x_norm - center)**2))
        rbf_term = np.sum(rbfs)
        
        # Competitive cross-dimensional interactions
        cross_interactions = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interactions += (x_norm[i] * x_norm[j]) / (1 + np.abs(x_norm[i] - x_norm[j]))
        
        # Polynomial coupling with exponential decay
        poly_exp = np.sum(x_norm**4 * np.exp(-0.5 * np.abs(x_norm)))
        
        # Saddle point enhancing term
        saddle_term = np.sum(np.sin(2 * x_norm) * np.cos(3 * x_norm) * np.tanh(x_norm))
        
        # Add noise for landscape complexity
        noise = 0.02 * np.random.random()
        
        # Combine all terms
        return chaotic_term + rbf_term + cross_interactions + poly_exp + saddle_term + noise