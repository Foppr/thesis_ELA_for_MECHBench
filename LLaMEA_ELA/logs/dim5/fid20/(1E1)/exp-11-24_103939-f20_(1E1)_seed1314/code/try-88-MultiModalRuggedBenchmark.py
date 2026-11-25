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
            freq = 2**(i+1)
            f2 += np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i]) * np.sin(freq/2 * x_scaled[i])
        
        # Radial basis function components with varying centers and widths
        centers = np.linspace(-0.8, 0.8, min(5, self.dim))
        f3 = 0.0
        for i in range(min(5, self.dim)):
            center = centers[i] if i < len(centers) else 0.0
            width = 0.2 + 0.1 * np.sin(i)
            f3 += np.exp(-0.5 * ((x_scaled[i] - center) / width)**2)
        
        # Chaotic cross-dimensional interaction terms using logistic map-like coupling
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x_scaled[i]) * np.cos(x_scaled[j]) * (i + j) / (self.dim * (self.dim - 1) / 2)
                chaotic_factor = 0.5 + 0.5 * np.sin(10 * x_scaled[i] * x_scaled[j])
                f4 += coupling * chaotic_factor
        
        # Asymmetric saddle point structure with fractal-like behavior
        f5 = np.sum((x_scaled**2 - 0.5)**3)
        
        # High-frequency oscillation with exponentially growing amplitude to increase ruggedness
        f6 = 0.0
        for i in range(self.dim):
            amp = 2**(i+1)
            freq = 30 * (i+1)
            f6 += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i])
        
        # Combined penalty for boundary avoidance with non-linear scaling
        f7 = 0.5 * np.sum(np.abs(x_scaled)**3 + np.abs(x_scaled)**1.5 + 0.2 * np.abs(x_scaled)**4)
        
        # Fractal basin structure component
        f8 = 0.0
        for i in range(self.dim):
            f8 += np.sin(100 * x_scaled[i]**2) * np.cos(50 * x_scaled[i]**3) * (i+1) / self.dim
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8