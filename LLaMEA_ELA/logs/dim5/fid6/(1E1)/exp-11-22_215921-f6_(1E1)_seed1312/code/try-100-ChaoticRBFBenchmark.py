import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic logistic map component with parameter modulation
        chaotic = 0.0
        r = 3.95  # chaotic regime parameter
        for i in range(self.dim - 1):
            if i < len(x_norm) - 1:
                chaotic += (r * x_norm[i] * (1 - x_norm[i]) + 
                           r * x_norm[i+1] * (1 - x_norm[i+1]))
        
        # Radial basis function with dynamic centers and varying widths
        rbf = 0.0
        centers = np.linspace(-1, 1, min(5, self.dim))
        for i in range(min(5, self.dim)):
            if i < len(x_norm):
                width = 0.5 + 0.3 * np.sin(i)
                rbf += np.exp(-0.5 * ((x_norm[i] - centers[i % len(centers)]) / width)**2)
        
        # Cross-dimensional coupling with exponential decay
        coupling = 0.0
        for i in range(self.dim - 1):
            if i < len(x_norm) - 1:
                coupling += np.exp(-0.3 * (x_norm[i]**2 + x_norm[i+1]**2)) * \
                           np.sin(5 * np.pi * (x_norm[i] + x_norm[i+1]))
        
        # Multi-modal oscillation with adaptive frequency
        oscillation = 0.0
        for i in range(self.dim):
            if i < len(x_norm):
                freq = 2 + 3 * np.sin(i)
                oscillation += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Asymmetric saddle points with polynomial interactions
        saddle = 0.0
        for i in range(self.dim - 1):
            if i < len(x_norm) - 1:
                saddle += (x_norm[i]**3 - x_norm[i+1]**2) * \
                         np.exp(-0.1 * (x_norm[i]**2 + x_norm[i+1]**2))
        
        # Dimension-dependent conditioning factor
        condition_factor = 1.0 + 0.8 * np.log(self.dim + 1)
        
        # Combine all terms with appropriate scaling
        return condition_factor * (0.5 * chaotic + 2.0 * rbf + 1.5 * coupling + 
                                 1.0 * oscillation + 0.7 * saddle)