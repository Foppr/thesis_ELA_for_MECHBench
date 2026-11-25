import numpy as np

class AdaptivePhaseTrigonometricLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive scaling
        result = 0.1 * np.sum(x**2)
        
        # Polynomial terms with varying exponents and adaptive coefficients
        for i in range(self.dim):
            result += 0.5 * x[i]**4 + 0.3 * x[i]**6 + 0.2 * x[i]**8
        
        # Trigonometric components with dynamic phase shifts based on dimension
        for i in range(self.dim):
            phase = np.sin(i * np.pi / self.dim) * 2.0
            result += 1.5 * np.sin(x[i] + phase)**2 + 1.0 * np.cos(2 * x[i] + phase)**2
        
        # Exponential decay with dimension-dependent rates
        for i in range(self.dim):
            rate = 0.1 + 0.2 * (i / self.dim)
            result += 2.0 * np.exp(-rate * np.abs(x[i])) * np.sin(3 * x[i])**2
        
        # Cross-dimensional interaction with adaptive coupling strength
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling = 0.5 + 0.3 * (i / self.dim) * (j / self.dim)
                result += coupling * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Adaptive noise component with dimensionality influence
        noise_strength = 0.02 * (1 + 0.1 * self.dim)
        result += noise_strength * np.random.random()
        
        # Logarithmic barrier near boundaries to prevent out-of-bounds evaluation
        barrier = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.5:
                barrier += 10.0 * (np.abs(x[i]) - 4.5)**2
        
        result += barrier
        
        return result