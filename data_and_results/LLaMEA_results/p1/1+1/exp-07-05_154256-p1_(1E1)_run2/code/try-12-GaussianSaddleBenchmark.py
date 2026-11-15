import numpy as np

class GaussianSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.peaks = 5
        self.gaussians = []
        self.saddles = []
        
        # Generate random peak positions and weights
        np.random.seed(42)
        for i in range(self.peaks):
            pos = np.random.uniform(-4.0, 4.0, dim)
            weight = np.random.uniform(0.5, 2.0)
            self.gaussians.append((pos, weight))
            
        # Generate saddle points
        for i in range(self.peaks):
            pos = np.random.uniform(-4.0, 4.0, dim)
            strength = np.random.uniform(0.1, 0.5)
            self.saddles.append((pos, strength))
    
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian peak components
        gaussian_sum = 0.0
        for pos, weight in self.gaussians:
            dist = np.sum((x - pos)**2)
            gaussian_sum += weight * np.exp(-dist / 2.0)
        
        # Saddle point components
        saddle_sum = 0.0
        for pos, strength in self.saddles:
            dist = np.sum((x - pos)**2)
            # Create saddle effect with cross-terms
            saddle_term = 0.0
            for i in range(self.dim):
                saddle_term += (x[i] - pos[i])**2
                if i < self.dim - 1:
                    saddle_term -= 0.5 * (x[i] - pos[i]) * (x[i+1] - pos[i+1])
            saddle_sum += strength * saddle_term * np.exp(-dist / 5.0)
        
        # Add a global quadratic term to ensure boundedness
        quadratic = 0.1 * np.sum(x**2)
        
        # Combine all components
        return gaussian_sum - saddle_sum + quadratic