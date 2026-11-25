import numpy as np

class AdaptiveMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute scaling factors for each dimension
        self.scaling_factors = np.linspace(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Polynomial terms with varying degrees and scaling
        for i in range(self.dim):
            scaled_x = x[i] * self.scaling_factors[i]
            result += 0.1 * scaled_x**4 + 0.3 * scaled_x**3 - 0.5 * scaled_x**2 + 0.7 * scaled_x
        
        # Trigonometric components with dynamic frequencies
        for i in range(self.dim):
            result += 1.2 * np.sin(2.5 * x[i]) * np.cos(1.8 * x[i]) + 0.8 * np.sin(3.2 * x[i])
        
        # Radial basis function components with adaptive centers
        centers = np.linspace(-4, 4, min(5, self.dim))
        for i in range(self.dim):
            if i < len(centers):
                center = centers[i]
                result += 0.6 * np.exp(-0.5 * (x[i] - center)**2) * np.sin(4 * (x[i] - center))
        
        # Cross-dimensional interaction with dynamic coupling strength
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.3 * (1 + np.sin(0.5 * (x[i] + x[j])))
                result += coupling_strength * np.exp(-0.2 * (x[i] - x[j])**2) * np.cos(2 * (x[i] + x[j]))
        
        # Adaptive noise component based on position
        noise_amplitude = 0.05 * (1 + np.mean(np.abs(x)))
        result += noise_amplitude * np.random.normal()
        
        return result