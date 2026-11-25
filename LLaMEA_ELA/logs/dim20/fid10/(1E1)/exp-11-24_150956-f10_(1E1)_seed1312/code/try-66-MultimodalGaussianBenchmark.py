import numpy as np

class MultimodalGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate random peak positions and heights for diversity
        np.random.seed(42)
        self.peak_positions = np.random.uniform(-5.0, 5.0, (10, dim))
        self.peak_heights = np.random.uniform(0.5, 2.0, 10)
        self.widths = np.random.uniform(0.5, 2.0, 10)
        
    def f(self, x):
        # Initialize function value
        result = 0.0
        
        # Add contribution from each Gaussian peak
        for i in range(10):
            pos = self.peak_positions[i]
            height = self.peak_heights[i]
            width = self.widths[i]
            
            # Compute squared distance to peak
            dist_sq = np.sum((x - pos)**2)
            
            # Add Gaussian contribution
            result += height * np.exp(-dist_sq / (2 * width**2))
        
        # Add saddle point terms for complexity
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += x[i]**4 - 2*x[i]**2
        
        # Combine all terms with different weights
        return 1.5 * result + 0.3 * saddle_term - 10.0