import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Radial basis function terms with varying widths and heights
        rbf_terms = 0.0
        centers = np.linspace(-3, 3, min(5, self.dim))
        for i in range(min(5, self.dim)):
            center = centers[i] if self.dim > 1 else 0.0
            width = 0.5 + 0.5 * np.sin(i)
            height = 1.0 + 0.5 * np.cos(i)
            rbf_terms += height * np.exp(-width * (x[0] - center)**2)
        
        # Asymmetric saddle points with varying steepness
        saddle_terms = 0.0
        for i in range(self.dim):
            if i % 2 == 0:
                saddle_terms += (x[i]**4 - 2*x[i]**2) * (1 + 0.1 * np.sin(i))
            else:
                saddle_terms += (x[i]**3 - x[i]) * (1 + 0.1 * np.cos(i))
        
        # Adaptive conditioning based on dimension
        condition_factor = 1.0 + 0.1 * self.dim
        
        # Combine all terms with proper scaling
        return condition_factor * (rbf_terms + saddle_terms) + 0.01 * np.sum(x**4)