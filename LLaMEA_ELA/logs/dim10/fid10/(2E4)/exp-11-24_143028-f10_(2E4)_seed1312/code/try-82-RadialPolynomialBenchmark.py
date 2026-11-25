import numpy as np

class RadialPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive conditioning
        result = 0.05 * np.sum(x**2)
        
        # Radial basis functions with varying widths and centers
        for i in range(self.dim):
            # Gaussian RBF with adaptive width
            width = 1.0 + 0.5 * np.abs(x[i])
            center = np.sin(i * 0.5) * 3.0
            result += 2.0 * np.exp(-0.5 * ((x[i] - center)**2) / (width**2))
        
        # Polynomial cross-terms with varying degrees
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Adaptive polynomial interaction
                degree = 2 + (i + j) % 3
                result += 0.5 * (x[i]**degree) * (x[j]**(degree + 1)) * np.cos(0.5 * (x[i] + x[j]))
        
        # Sine-based multimodal structure with frequency modulation
        for i in range(self.dim):
            freq = 3.0 + 2.0 * np.sin(i * 0.3)
            result += 1.5 * np.sin(freq * x[i]) * np.cos(2 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Adaptive conditioning with distance from origin
        dist = np.sqrt(np.sum(x**2))
        condition_factor = 1.0 + 0.3 * np.exp(-0.2 * dist)
        result *= condition_factor
        
        # Boundary penalty with polynomial scaling
        boundary_penalty = 0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.5:
                boundary_penalty += 3.0 * (np.abs(x[i]) - 4.5)**3
        result += boundary_penalty
        
        # Cubic nonlinearity to increase condition number
        for i in range(self.dim):
            result += 0.1 * x[i]**3
        
        return result