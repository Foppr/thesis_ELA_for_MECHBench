import numpy as np

class MultiModalRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for consistent conditioning
        x_scaled = x / 5.0
        
        # Polynomial landscape with mixed degrees and chaotic coefficients
        coeffs = np.sin(np.arange(self.dim) * np.pi / 4)
        f1 = np.sum(coeffs * (x_scaled**5 + 0.7 * x_scaled**4 - 0.4 * x_scaled**3 + 0.2 * x_scaled**2 - 0.1 * x_scaled))
        
        # Chaotic trigonometric interference with non-uniform frequencies
        f2 = 0.0
        for i in range(self.dim):
            freq = 15 + 10 * np.sin(i * np.pi / self.dim)
            f2 += np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.7) * np.sin(freq * x_scaled[i] * 0.3)
        f2 = np.sum(f2)
        
        # Exponential repulsion fields with random centers and variable strengths
        f3 = 0.0
        for i in range(min(7, self.dim)):
            center = np.random.uniform(-0.9, 0.9)
            strength = 0.5 + 0.5 * np.sin(i * 2 * np.pi / self.dim)
            width = 0.1 + 0.2 * np.cos(i * np.pi / self.dim)
            f3 += strength * np.exp(-0.5 * ((x_scaled[i] - center) / width)**2)
        
        # Adaptive cross-dimensional coupling with dynamic weights
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.3 + 0.7 * np.sin((i + j) * np.pi / (self.dim + 1))
                f4 += weight * np.sin(x_scaled[i]) * np.cos(x_scaled[j]) * np.tan(0.5 * (x_scaled[i] + x_scaled[j]))
        
        # Asymmetric saddle point structure with variable exponents
        f5 = np.sum((x_scaled**2 - 0.3)**4 + 0.5 * (x_scaled**2 - 0.7)**3)
        
        # High-frequency chaotic oscillation with dynamic amplitude modulation
        f6 = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(i * 3 * np.pi / self.dim)
            freq = 80 + 20 * np.cos(i * 2 * np.pi / self.dim)
            f6 += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.9)
        f6 = np.sum(f6)
        
        # Combined penalty for boundary avoidance with adaptive exponents
        exponents = 2 + 2 * np.sin(np.arange(self.dim) * np.pi / self.dim)
        f7 = np.sum(0.3 * np.abs(x_scaled)**exponents + 0.2 * np.abs(x_scaled)**(exponents * 0.5))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7