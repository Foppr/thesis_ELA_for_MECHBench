import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map parameters for chaos generation
        self.r_values = np.linspace(3.8, 4.0, min(dim, 20))
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced logistic map chaos component with memory effects
        chaos_term = 0.0
        x_prev = np.full(min(self.dim, 10), 0.5)
        for i in range(min(self.dim, 10)):
            if i == 0:
                x_prev[i] = 0.5
            else:
                x_prev[i] = x[i-1] / 5.0 + 0.5  # Normalize to [0,1]
            chaos_term += self.r_values[i % len(self.r_values)] * x_prev[i] * (1 - x_prev[i])
        
        # Multi-scale radial basis functions with varying widths and heights
        rbfs = 0.0
        centers = np.linspace(-4.5, 4.5, 7)
        widths = np.logspace(-1, 1, 5)
        heights = np.linspace(0.5, 2.0, 4)
        for i, center in enumerate(centers):
            for j in range(self.dim):
                width = widths[j % len(widths)]
                height = heights[i % len(heights)]
                rbfs += height * np.exp(-0.5 * ((x[j] - center) / width)**2) * \
                       np.sin(3 * np.pi * (x[j] - center) / (1.0 + 0.2 * (i % 4)))
        
        # Asymmetric saddle points with polynomial and trigonometric mix
        saddle = 0.0
        for i in range(self.dim):
            saddle += (x[i]**5 - 10*x[i]**3 + 25*x[i]) * np.cos(0.7 * x[i]) + \
                     0.05 * (x[i] - np.mean(x))**6 + \
                     0.3 * np.sin(4 * x[i]) * np.cos(2 * x[i])
        
        # High-dimensional cross-terms with complex periodic interactions
        cross_term = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 2) % self.dim
            cross_term += np.sin(5 * x[i]) * np.cos(3 * x[j]) * np.sin(2 * x[k]) * \
                         np.exp(-0.05 * (x[i]**2 + x[j]**2 + x[k]**2))
        
        # Additional coupling terms between dimensions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += 0.1 * np.sin(3 * (x[i] - x[j])) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Combine all components with adaptive weights based on dimensionality
        dim_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        result = 0.4 * np.sum(x**2) + 0.35 * chaos_term + 0.3 * rbfs + 0.25 * saddle + \
                0.15 * cross_term + 0.1 * coupling
        
        return result