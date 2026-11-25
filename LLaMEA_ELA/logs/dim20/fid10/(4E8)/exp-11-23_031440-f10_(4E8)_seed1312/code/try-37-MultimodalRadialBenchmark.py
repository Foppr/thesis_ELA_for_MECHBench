import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Radial basis function terms with varying widths and heights
        rbf_terms = 0.0
        centers = np.linspace(-4.0, 4.0, min(5, self.dim))
        for i in range(min(5, self.dim)):
            center = centers[i] if self.dim > 1 else 0.0
            width = 1.0 + 0.5 * np.sin(i)
            height = 2.0 + 1.0 * np.cos(i)
            rbf_terms += height * np.exp(-width * (x[0] - center)**2) if self.dim > 0 else 0.0
            
        # Asymmetric saddle points with varying steepness
        saddle_terms = 0.0
        for i in range(self.dim):
            saddle_terms += (x[i]**2 - 4*x[i])**2 + 0.1 * x[i]**4
            
        # Adaptive conditioning based on dimension
        condition_factor = 1.0 + 0.1 * self.dim
        
        # Combine terms with proper scaling
        result = condition_factor * (rbf_terms + saddle_terms)
        
        return result