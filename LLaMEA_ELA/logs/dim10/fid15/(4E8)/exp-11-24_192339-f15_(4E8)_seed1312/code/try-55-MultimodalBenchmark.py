import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Enhanced multimodal component with multiple local minima and varying frequencies
        multimodal = 0
        for i in range(self.dim):
            # Combined high-frequency trigonometric modulations with polynomial interactions
            multimodal += (np.sin(7 * np.pi * x[i]) ** 6 + 
                          0.7 * np.cos(12 * np.pi * x[i]) ** 4 +
                          0.4 * np.sin(5 * np.pi * x[i]) ** 8 +
                          0.2 * np.cos(8 * np.pi * x[i]) ** 6)
        
        # Enhanced polynomial interaction terms with cross-dimensional coupling
        poly_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Introduce non-linear coupling and higher-order terms
                poly_interaction += (x[i]**3 * x[j]**2 + 
                                   x[i]**2 * x[j]**3 +
                                   0.1 * np.sin(3 * np.pi * x[i]) * np.cos(3 * np.pi * x[j]) +
                                   0.05 * x[i] * x[j] ** 4 +
                                   0.05 * x[j] * x[i] ** 4)
        
        # Radial basis function component for additional landscape complexity
        rbf = 0
        for i in range(self.dim):
            rbf += np.exp(-0.5 * (x[i] - 1.0)**2) + np.exp(-0.5 * (x[i] + 1.0)**2)
        
        # Adaptive scaling based on dimensionality and enhanced complexity factors
        adaptive_scale = 1.0 + 0.15 * self.dim + 0.02 * np.sin(self.dim * 0.5)
        
        # Combined function with refined balance of components for improved benchmark performance
        return adaptive_scale * (sphere + 0.6 * multimodal + 0.15 * poly_interaction + 0.2 * rbf)