import numpy as np

class AdaptiveMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for adaptive scaling
        self.scale_factors = np.linspace(1.0, 3.0, dim) if dim > 1 else np.array([2.0])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Polynomial terms with varying degrees and adaptive scaling
        for i in range(self.dim):
            scaled_x = x[i] * self.scale_factors[i]
            result += 0.1 * scaled_x**4 + 0.3 * scaled_x**3 - 0.5 * scaled_x**2 + 0.7 * scaled_x
        
        # Trigonometric components with frequency modulation
        for i in range(self.dim):
            result += 1.5 * np.sin(2.5 * x[i]) * np.cos(1.8 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Radial basis function components with dynamic centers
        centers = np.linspace(-4, 4, min(5, self.dim))
        for i in range(len(centers)):
            if i < self.dim:
                result += 0.8 * np.exp(-0.5 * (x[i] - centers[i])**2) * np.sin(3 * x[i])
        
        # Cross-dimensional interaction with dynamic coupling strength
        coupling_strength = 0.5 + 0.3 * np.sin(self.dim)
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = x[i] - x[j]
                result += coupling_strength * np.exp(-0.2 * diff**2) * np.cos(2 * (x[i] + x[j]))
        
        # Adaptive noise component
        noise_amp = 0.02 * (1 + 0.5 * np.sin(self.dim))
        result += noise_amp * np.random.randn()
        
        # Asymmetric penalty for out-of-bounds regions
        penalty = 0.0
        for i in range(self.dim):
            if x[i] < -4.5 or x[i] > 4.5:
                penalty += 2.0 * (abs(x[i]) - 4.5)**2
        result += penalty
        
        return result