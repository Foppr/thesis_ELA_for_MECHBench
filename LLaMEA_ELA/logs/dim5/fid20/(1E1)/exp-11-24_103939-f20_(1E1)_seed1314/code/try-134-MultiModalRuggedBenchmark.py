import numpy as np

class MultiModalRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for consistent conditioning
        x_scaled = x / 5.0
        
        # Polynomial landscape with mixed degrees and chaotic coefficients
        f1 = np.sum(0.8 * x_scaled**6 + 0.5 * x_scaled**5 - 0.3 * x_scaled**4 + 0.2 * x_scaled**3 - 0.1 * x_scaled**2 + 0.15 * x_scaled)
        
        # Trigonometric interference creating multiple local minima with modified frequencies and chaotic phases
        f2 = np.sum(np.sin(20 * x_scaled + np.sin(7 * x_scaled)) * np.cos(18 * x_scaled + np.cos(5 * x_scaled)) * 
                   np.sin(13 * x_scaled + np.sin(9 * x_scaled)) * np.cos(11 * x_scaled + np.cos(8 * x_scaled)))
        
        # Radial basis function components with varying centers, widths, and chaotic modulation
        centers = np.linspace(-0.8, 0.8, min(7, self.dim))
        f3 = 0.0
        for i in range(min(7, self.dim)):
            center = centers[i] if i < len(centers) else 0.0
            width = 0.3 + 0.1 * np.sin(i * 1.7) + 0.05 * np.cos(i * 2.3)
            f3 += np.exp(-0.5 * ((x_scaled[i] - center) / width)**2) * (1 + 0.2 * np.sin(13 * x_scaled[i]))
        
        # Enhanced cross-dimensional interaction terms with chaotic weights and higher-order coupling
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = (i + j) / (self.dim * (self.dim - 1) / 2) * (1 + 0.15 * np.sin(i * j * 0.8))
                f4 += np.sin(x_scaled[i]) * np.cos(x_scaled[j]) * weight + 0.2 * x_scaled[i] * x_scaled[j] * np.cos(3 * (x_scaled[i] + x_scaled[j]))
        
        # Asymmetric saddle point structure with chaotic exponent and multiple peaks
        f5 = np.sum((x_scaled**2 - 0.3)**4 + 0.1 * np.sin(17 * x_scaled) * x_scaled**2)
        
        # High-frequency oscillation with chaotic modulation to increase ruggedness
        f6 = np.sum(np.sin(80 * x_scaled + np.cos(45 * x_scaled)) * np.cos(75 * x_scaled + np.sin(50 * x_scaled)))
        
        # Combined penalty for boundary avoidance with modified exponents and chaotic scaling
        f7 = 0.7 * np.sum((np.abs(x_scaled)**4.2 + np.abs(x_scaled)**2.1) * (1 + 0.3 * np.sin(19 * x_scaled)))
        
        # Additional chaotic noise component to disrupt optimization paths
        noise = np.sum(0.05 * np.random.rand(self.dim) * np.sin(100 * x_scaled))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + noise