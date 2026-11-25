import numpy as np

class AdaptivePolynomialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale input to [-5, 5] domain if needed
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Polynomial base terms with dimension-dependent coefficients
        for i in range(self.dim):
            result += 0.5 * (x[i] ** 4) + 0.3 * (x[i] ** 3) + 0.2 * (x[i] ** 2) + 0.1 * x[i]
        
        # Exponential decay with adaptive rate based on dimension
        for i in range(self.dim):
            result += 0.4 * np.exp(-0.5 * abs(x[i])) * (1.0 + 0.1 * i)
        
        # Trigonometric components with dynamic frequencies and phase shifts
        for i in range(self.dim):
            freq = 2.0 * (i + 1) * (1.0 + 0.05 * np.sin(0.5 * i))
            result += 0.3 * np.sin(freq * x[i] + 0.3 * i) * np.cos(freq * x[i] + 0.2 * i)
        
        # Radial symmetry with dynamic scaling
        if self.dim >= 2:
            r = np.sqrt(np.sum(x[:2]**2))
            result += 0.5 * np.sin(5.0 * r + 0.1 * r**2) * np.exp(-0.2 * r)
        
        # Cross-dimensional coupling with adaptive weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.2 * (1.0 + 0.05 * (i + j)) * np.cos(0.1 * (x[i] + x[j]))
                result += weight * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Asymmetric exponential terms
        for i in range(self.dim):
            if x[i] > 0:
                result += 0.3 * np.exp(-0.4 * x[i]) * (1.0 + 0.1 * x[i]**2)
            else:
                result += 0.25 * np.exp(-0.6 * abs(x[i])) * (1.0 + 0.15 * x[i]**2)
        
        # High-frequency oscillatory component
        for i in range(self.dim):
            result += 0.2 * np.sin(20.0 * x[i]) * np.cos(15.0 * x[i])
        
        # Adaptive polynomial interaction terms
        for i in range(min(self.dim, 3)):
            for j in range(i+1, min(self.dim, 4)):
                result += 0.15 * (x[i] ** 2) * (x[j] ** 3) * np.sin(x[i] + x[j])
        
        # Global modulation with dynamic phase
        sum_squares = np.sum(x**2)
        result += 0.3 * np.exp(-0.1 * sum_squares) * np.sin(2.0 * sum_squares + 0.05 * sum_squares**2)
        
        # Boundary attraction with varying strength
        for i in range(self.dim):
            boundary_term = 0.2 * (5.0 - abs(x[i]))**2
            if x[i] < -4.0 or x[i] > 4.0:
                result += boundary_term * (1.0 + 0.1 * abs(x[i]))
            else:
                result += boundary_term
        
        # Dynamic phase shift component
        for i in range(self.dim):
            phase_shift = 0.1 * np.sin(0.3 * i) * np.cos(0.2 * i)
            result += 0.15 * np.sin(3.0 * x[i] + phase_shift) * np.exp(-0.05 * x[i]**2)
        
        # Additional cross-dimensional interaction with dynamic coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if abs(x[i]) > 1.0 and abs(x[j]) > 1.0:
                    result += 0.1 * np.sin(x[i] * x[j]) * (1.0 + 0.02 * (i + j))
        
        return result