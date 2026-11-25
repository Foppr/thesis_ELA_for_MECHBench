import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for each dimension
        self.chaotic_params = np.random.uniform(0.1, 0.9, dim)
        
    def f(self, x):
        x = np.array(x)
        
        # Chaotic sine map component
        chaotic = 0
        for i in range(self.dim):
            # Logistic-like chaotic behavior with parameter modulation
            chaotic += np.sin(np.pi * self.chaotic_params[i] * np.sin(x[i]))
            
        # Radial Basis Function component with multiple centers
        rbf = 0
        num_centers = min(10, 2 + self.dim)
        centers = np.random.uniform(-4.0, 4.0, (num_centers, self.dim))
        
        for i in range(num_centers):
            dist = np.sum((x - centers[i])**2)
            rbf += np.exp(-dist / (2 * 0.5**2)) * np.sin(3 * np.pi * dist)
            
        # Adaptive noise component that changes with input values
        noise = 0
        for i in range(self.dim):
            # Noise magnitude depends on the distance from the center
            dist_from_center = np.abs(x[i] - np.mean(x))
            noise += np.random.normal(0, 0.1 * (1 + dist_from_center**2)) * np.sin(x[i])
            
        # Cross-dimensional coupling with exponential decay
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += np.exp(-0.5 * (x[i] - x[j])**2) * np.cos(x[i] + x[j])
                
        # Global shaping term with polynomial and trigonometric components
        shape = np.sum(x**4) + 0.5 * np.sum(np.sin(5 * x)**2)
        
        # Combine all components with different weights
        return 0.3 * chaotic + 0.4 * rbf + 0.1 * noise + 0.1 * coupling + 0.1 * shape