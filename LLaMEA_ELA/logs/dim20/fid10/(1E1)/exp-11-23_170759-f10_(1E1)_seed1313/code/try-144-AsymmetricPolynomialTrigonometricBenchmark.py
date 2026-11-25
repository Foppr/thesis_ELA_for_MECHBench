import numpy as np

class AsymmetricPolynomialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale input to [-5, 5] domain if needed
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Polynomial base with varying exponents and asymmetric coefficients
        for i in range(self.dim):
            coeff = 1.0 + 0.3 * np.sin(i) + 0.2 * np.cos(i)
            result += coeff * (x[i] ** (3 + i % 3)) * np.exp(-0.1 * abs(x[i]))
        
        # Exponential decay with coordinate-dependent rates and modulation
        for i in range(self.dim):
            rate = 0.5 + 0.2 * np.sin(i * 0.5)
            result += 0.5 * np.exp(-rate * abs(x[i])) * (1.0 + 0.1 * x[i]**2)
        
        # Trigonometric components with dynamic frequencies and phase shifts
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(i * 0.3)
            phase = 0.5 * np.cos(i * 0.4)
            result += 0.4 * np.sin(freq * x[i] + phase) * np.cos(freq * x[i] - phase)
        
        # Cross-dimensional coupling with polynomial interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.3 * (i + 1) * (j + 1)
                result += coupling * np.sin(x[i] * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Asymmetric exponential terms with different scaling for positive and negative values
        for i in range(self.dim):
            if x[i] >= 0:
                result += 0.3 * np.exp(-0.7 * x[i]) * (1.0 + 0.2 * x[i]**2)
            else:
                result += 0.25 * np.exp(-0.9 * abs(x[i])) * (1.0 + 0.15 * x[i]**2)
        
        # High-frequency oscillatory component with amplitude modulation
        for i in range(self.dim):
            result += 0.35 * np.sin(20.0 * x[i]) * np.cos(18.0 * x[i]) * (1.0 + 0.05 * abs(x[i]))
        
        # Radial symmetry with modified frequency and amplitude
        if self.dim >= 2:
            r = np.sqrt(np.sum(x[:2]**2))
            result += 0.6 * np.sin(8.0 * r) * np.exp(-0.3 * r)
        
        # Boundary attraction with variable strength
        for i in range(self.dim):
            boundary_penalty = 0.4 * (5.0 - abs(x[i]))**2.5
            result += boundary_penalty
        
        # Additional coupling between first few dimensions
        for i in range(min(3, self.dim)):
            for j in range(i+1, min(4, self.dim)):
                result += 0.2 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        return result