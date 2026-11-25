import numpy as np

class AsymmetricPolynomialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale input to [-5, 5] domain if needed
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Polynomial base terms with asymmetric exponents
        for i in range(self.dim):
            if x[i] >= 0:
                result += 0.5 * (x[i] ** (2.5 + 0.1 * i)) * (1.0 + 0.02 * i)
            else:
                result += 0.4 * (abs(x[i]) ** (3.0 + 0.05 * i)) * (1.0 + 0.01 * i)
        
        # Exponential decay with directional bias
        for i in range(self.dim):
            if x[i] > 0:
                result += 0.3 * np.exp(-0.5 * x[i]) * (1.0 + 0.1 * x[i]**2)
            else:
                result += 0.25 * np.exp(-0.7 * abs(x[i])) * (1.0 + 0.15 * x[i]**2)
        
        # Trigonometric components with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = 3.0 + 0.5 * i
            result += 0.4 * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7) * (1.0 + 0.03 * i)
        
        # Cross-dimensional coupling with asymmetric interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if i % 2 == 0:
                    result += 0.2 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * (1.0 + 0.05 * (i + j))
                else:
                    result += 0.15 * np.sin(x[i] * x[j]) * np.cos(x[i] / (x[j] + 1e-8)) * (1.0 + 0.03 * (i + j))
        
        # Radial symmetry with modified frequency
        if self.dim >= 2:
            r = np.sqrt(np.sum(x[:2]**2))
            result += 0.5 * np.sin(6.0 * r) * np.exp(-0.2 * r)
        
        # Directional bias terms that favor certain quadrants
        for i in range(self.dim):
            if x[i] > 0:
                result += 0.1 * np.sin(2.0 * x[i]) * (1.0 + 0.05 * i)
            else:
                result += 0.12 * np.cos(1.5 * x[i]) * (1.0 + 0.03 * i)
        
        # High-frequency oscillation with amplitude modulation
        for i in range(self.dim):
            result += 0.2 * np.sin(20.0 * x[i]) * np.cos(18.0 * x[i]) * (1.0 + 0.02 * abs(x[i]))
        
        # Boundary attraction with asymmetric penalty
        for i in range(self.dim):
            if x[i] > 0:
                result += 0.3 * (5.0 - x[i])**2.5
            else:
                result += 0.25 * (5.0 + x[i])**2.5
        
        # Additional polynomial interaction terms
        for i in range(min(self.dim, 3)):
            result += 0.15 * (x[i] ** 3) * np.sin(x[i]) * (1.0 + 0.02 * i)
        
        return result