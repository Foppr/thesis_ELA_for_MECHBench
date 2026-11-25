import numpy as np

class MultiModalRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for consistent conditioning
        x_scaled = x / 5.0
        
        # Polynomial landscape with mixed degrees and chaotic coefficients
        f1 = np.sum(0.9 * x_scaled**6 + 0.3 * x_scaled**5 - 0.2 * x_scaled**4 + 0.15 * x_scaled**3 + 0.08 * x_scaled**2 + 0.03 * x_scaled)
        
        # Nested trigonometric interference creating fractal-like local minima
        f2 = np.sum(np.sin(25 * np.sin(18 * x_scaled)) * np.cos(20 * np.cos(15 * x_scaled)) * 
                   np.sin(15 * np.sin(10 * x_scaled)) * np.cos(12 * np.cos(8 * x_scaled)))
        
        # Radial basis function components with fractal-like centers and widths
        centers = np.array([np.sin(i * 1.4) * 0.7 for i in range(min(7, self.dim))])
        f3 = 0.0
        for i in range(min(7, self.dim)):
            center = centers[i] if i < len(centers) else 0.0
            width = 0.12 + 0.06 * np.sin(i * 2.3)
            f3 += np.exp(-0.5 * ((x_scaled[i] - center) / width)**4)
        
        # Adaptive cross-dimensional interaction terms with chaotic weights
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.25 + 0.15 * np.sin(i * j * 0.8) * np.cos((i + j) * 0.6)
                f4 += weight * np.sin(x_scaled[i]) * np.cos(x_scaled[j]) * (x_scaled[i]**2 + x_scaled[j]**2)
        
        # Saddle point structure with chaotic exponent and multiple inflection points
        f5 = np.sum((x_scaled**3 - 0.25 * x_scaled)**2)
        
        # High-frequency oscillation with adaptive frequency modulation
        f6 = np.sum(np.sin(90 * x_scaled + np.sin(45 * x_scaled)) * np.cos(80 * x_scaled + np.cos(40 * x_scaled)))
        
        # Combined penalty for boundary avoidance with chaotic exponents
        f7 = 0.9 * np.sum(np.abs(x_scaled)**4.5 + np.abs(x_scaled)**2.3)
        
        # Fractal-like self-similarity component
        f8 = 0.0
        for i in range(self.dim):
            f8 += np.sin(35 * x_scaled[i]) * np.cos(30 * x_scaled[i]) * np.sin(25 * x_scaled[i]) * np.cos(20 * x_scaled[i])
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + 0.12 * f8