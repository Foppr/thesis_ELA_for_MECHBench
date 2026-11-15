import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = 0.0
        
        # Periodic trigonometric components with varying frequencies and amplitudes
        for i in range(self.dim):
            result += 0.5 * (np.sin(2.0 * np.pi * x[i]) + 
                            0.3 * np.sin(5.0 * np.pi * x[i]) + 
                            0.1 * np.sin(12.0 * np.pi * x[i]))
        
        # Gradient-based attraction fields towards multiple local minima
        for i in range(self.dim):
            # Attraction towards points in a grid pattern
            grid_points = np.arange(-4.0, 5.0, 2.0)
            attraction = 0.0
            for point in grid_points:
                attraction += np.exp(-0.5 * (x[i] - point)**2) * np.cos(0.5 * np.pi * (x[i] - point))
            result += 0.3 * attraction
        
        # Adaptive noise component that varies with dimensionality
        noise_scale = 0.05 * np.log(self.dim + 1)
        result += noise_scale * np.sum(np.sin(10.0 * x) * np.cos(7.0 * x))
        
        # Cross-dimensional interaction terms with varying coupling strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(-0.1 * (x[i] - x[j])**2) * np.sin(0.3 * (x[i] + x[j]))
                result += 0.2 * coupling
        
        # Polynomial terms with varying exponents and sign patterns
        for i in range(self.dim):
            exponent = 2 + int(4 * np.sin(i * 0.5)) % 4
            sign = (-1)**(i % 2)
            result += 0.1 * sign * x[i]**exponent
        
        # Saddle-point inducing higher-order terms
        for i in range(self.dim):
            result += 0.05 * x[i]**5 * np.cos(0.3 * x[i])
        
        # Dimensionality-dependent scaling factor
        result *= (1.0 + 0.05 * np.log(self.dim + 1))
        
        return result