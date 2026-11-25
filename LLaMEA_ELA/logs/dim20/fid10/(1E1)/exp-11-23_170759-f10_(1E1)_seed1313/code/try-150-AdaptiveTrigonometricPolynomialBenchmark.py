import numpy as np

class AdaptiveTrigonometricPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale input to [-5, 5] domain if needed
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Polynomial base with dimension-dependent coefficients
        for i in range(self.dim):
            result += 0.1 * (x[i] ** 4) + 0.3 * (x[i] ** 3) + 0.5 * (x[i] ** 2) + 0.7 * x[i]
        
        # Adaptive exponential decay with dynamic scaling
        for i in range(self.dim):
            scale = 1.0 + 0.1 * np.sin(0.5 * i)
            result += 0.4 * np.exp(-scale * abs(x[i])) * (1.0 + 0.2 * x[i]**2)
        
        # Trigonometric components with dynamic frequencies and phase shifts
        for i in range(self.dim):
            freq = 3.0 + 0.5 * np.cos(0.3 * i)
            phase = 0.2 * np.sin(0.4 * i)
            result += 0.3 * np.sin(freq * x[i] + phase) * np.cos(freq * x[i] - phase)
        
        # Cross-dimensional interaction with dynamic coupling strength
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.2 * (1.0 + 0.1 * np.sin(0.2 * (i + j)))
                result += coupling * np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Radial symmetry with varying amplitude and frequency
        if self.dim >= 2:
            r = np.sqrt(np.sum(x[:2]**2))
            result += 0.5 * np.sin(5.0 * r) * np.cos(3.0 * r) * np.exp(-0.15 * r)
        
        # Asymmetric exponential terms with coordinate-dependent scaling
        for i in range(self.dim):
            if x[i] >= 0:
                result += 0.25 * np.exp(-0.7 * x[i]) * (1.0 + 0.3 * x[i]**2)
            else:
                result += 0.3 * np.exp(-0.8 * abs(x[i])) * (1.0 + 0.25 * x[i]**2)
        
        # High-frequency oscillatory component with amplitude modulation
        for i in range(self.dim):
            result += 0.2 * np.sin(20.0 * x[i]) * (1.0 + 0.1 * np.cos(5.0 * x[i]))
        
        # Adaptive polynomial interaction terms
        for i in range(min(self.dim, 3)):
            result += 0.15 * (x[i] ** 5) * np.sin(x[i])
        
        # Global modulation with dynamic nonlinearity
        sum_squares = np.sum(x**2)
        result += 0.3 * np.exp(-0.3 * sum_squares) * np.sin(4.0 * sum_squares + 0.05 * sum_squares**2)
        
        # Boundary attraction with adaptive penalty
        for i in range(self.dim):
            boundary_penalty = 0.15 * (5.0 - abs(x[i]))**2.5
            result += boundary_penalty
        
        # Dynamic phase-shifted trigonometric terms
        for i in range(self.dim):
            phase_shift = 0.3 * np.sin(0.2 * i)
            result += 0.2 * np.cos(6.0 * x[i] + phase_shift) * np.sin(4.0 * x[i] - phase_shift)
        
        # Additional cross-dimensional polynomial coupling
        for i in range(self.dim):
            for j in range(i+1, min(self.dim, i+3)):
                result += 0.1 * (x[i]**2 + x[j]**2) * np.cos(x[i] + x[j])
        
        return result