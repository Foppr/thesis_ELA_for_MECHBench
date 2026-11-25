import numpy as np

class MultiModalRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for consistent conditioning
        x_scaled = x / 5.0
        
        # Polynomial landscape with mixed degrees
        f1 = np.sum(x_scaled**4 + 0.5 * x_scaled**3 - 0.3 * x_scaled**2 + 0.1 * x_scaled)
        
        # Trigonometric interference creating multiple local minima with exponentially increasing frequencies
        f2 = 0.0
        for i in range(self.dim):
            freq = 2 ** (i % 5 + 1)
            f2 += np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.7) * np.sin(freq * x_scaled[i] * 0.3)
        
        # Radial basis function components with varying centers, widths, and amplitudes
        centers = np.linspace(-0.8, 0.8, min(5, self.dim))
        f3 = 0.0
        for i in range(min(5, self.dim)):
            center = centers[i] if i < len(centers) else 0.0
            width = 0.1 + 0.2 * np.sin(i)
            amp = 1.0 + 0.5 * np.cos(i)
            f3 += amp * np.exp(-0.5 * ((x_scaled[i] - center) / width)**2)
        
        # Enhanced cross-dimensional interaction terms with dynamic weights based on dimension index
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = (i + j) / (self.dim * (self.dim - 1) / 2)
                f4 += np.sin(x_scaled[i]) * np.cos(x_scaled[j]) * weight + 0.1 * x_scaled[i] * x_scaled[j] * weight
        
        # Asymmetric saddle point structure with fractal-like scaling
        f5 = np.sum((x_scaled**2 - 0.5)**3)
        
        # High-frequency oscillation to increase ruggedness with exponentially increasing frequencies
        f6 = 0.0
        for i in range(self.dim):
            freq = 10 * (2 ** i)
            f6 += np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.5)
        
        # Fractal-like penalty term with recursive scaling
        f7 = 0.0
        for i in range(self.dim):
            f7 += np.abs(x_scaled[i])**3.5 + np.abs(x_scaled[i])**2.5
        
        # Additional cross-dimensional coupling with non-linear interaction
        f8 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f8 += (x_scaled[i]**2 + x_scaled[j]**2) * np.sin(x_scaled[i] * x_scaled[j])
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8