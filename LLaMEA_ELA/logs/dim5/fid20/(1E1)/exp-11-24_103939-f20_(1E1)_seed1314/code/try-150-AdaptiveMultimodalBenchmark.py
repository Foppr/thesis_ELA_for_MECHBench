import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for consistent conditioning
        x_scaled = x / 5.0
        
        # Polynomial base with variable exponents based on dimension
        exponents = np.linspace(2, 6, self.dim)
        f1 = np.sum((x_scaled ** exponents) * (1 + 0.1 * np.sin(np.arange(self.dim))))
        
        # Trigonometric interference creating multiple local minima with dynamic frequencies
        frequencies = np.linspace(5, 20, self.dim)
        f2 = np.sum(np.sin(frequencies * x_scaled) * np.cos(frequencies * x_scaled))
        
        # Radial basis function components with adaptive centers and widths
        centers = np.linspace(-0.8, 0.8, min(7, self.dim))
        widths = 0.3 + 0.1 * np.sin(np.arange(min(7, self.dim)))
        f3 = 0.0
        for i in range(min(7, self.dim)):
            center = centers[i] if i < len(centers) else 0.0
            width = widths[i] if i < len(widths) else 0.3
            f3 += np.exp(-0.5 * ((x_scaled[i] - center) / width)**2)
        
        # Dynamic cross-dimensional interaction terms that change with dimension
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction range
                weight = (i + j) / (self.dim * (self.dim - 1) / 2)
                f4 += weight * np.sin(x_scaled[i]) * np.cos(x_scaled[j]) * np.exp(-0.5 * (x_scaled[i] - x_scaled[j])**2)
        
        # Asymmetric saddle point structure with dimension-dependent bias
        f5 = np.sum((x_scaled**2 - 0.3)**3 + 0.1 * x_scaled**4)
        
        # High-frequency oscillation to increase ruggedness with dimension scaling
        f6 = np.sum(np.sin(50 * x_scaled) * np.cos(45 * x_scaled) * (1 + 0.2 * np.cos(self.dim)))
        
        # Boundary avoidance penalty with adaptive exponent
        boundary_exponent = 2.5 + 0.5 * np.sin(self.dim)
        f7 = np.sum(np.abs(x_scaled)**boundary_exponent)
        
        # Dimensionality-based scaling factor for overall function magnitude
        scale_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7)