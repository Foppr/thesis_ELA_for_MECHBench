import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale input to [-5, 5] domain if needed
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Polynomial base terms with adaptive coefficients
        for i in range(self.dim):
            coef = 1.0 + 0.1 * np.sin(0.5 * i)
            result += coef * (x[i] ** 4) - 2.0 * (x[i] ** 2) + 0.5 * x[i]
        
        # Exponential decay with dynamic rate and amplitude
        for i in range(self.dim):
            rate = 0.3 + 0.2 * np.cos(0.3 * i)
            amp = 1.5 + 0.5 * np.sin(0.4 * i)
            result += amp * np.exp(-rate * abs(x[i])) * np.cos(2.0 * x[i])
        
        # Sinusoidal components with phase shifts and frequency modulation
        for i in range(self.dim):
            freq = 3.0 + 1.5 * np.sin(0.2 * i)
            phase = 0.5 * np.cos(0.3 * i)
            result += 0.8 * np.sin(freq * x[i] + phase) * np.exp(-0.1 * x[i]**2)
        
        # Cross-dimensional interaction with adaptive coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.5 + 0.3 * np.sin(0.1 * (i + j))
                result += coupling * np.sin(x[i] * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Radial symmetry with dynamic frequency and amplitude
        if self.dim >= 2:
            r = np.sqrt(np.sum(x[:2]**2))
            freq = 5.0 + 2.0 * np.sin(0.2 * self.dim)
            amp = 1.0 + 0.3 * np.cos(0.1 * self.dim)
            result += amp * np.sin(freq * r) * np.exp(-0.2 * r)
        
        # Asymmetric exponential terms with dynamic scaling
        for i in range(self.dim):
            if x[i] >= 0:
                scale = 1.2 + 0.2 * np.sin(0.5 * i)
                result += scale * np.exp(-0.8 * x[i]) * (1.0 + 0.2 * x[i]**2)
            else:
                scale = 1.0 + 0.3 * np.cos(0.4 * i)
                result += scale * np.exp(-0.6 * abs(x[i])) * (1.0 + 0.15 * x[i]**2)
        
        # High-frequency oscillatory component with dynamic amplitude
        for i in range(self.dim):
            amp = 0.5 + 0.3 * np.sin(0.6 * i)
            result += amp * np.sin(20.0 * x[i]) * np.cos(15.0 * x[i])
        
        # Boundary attraction with adaptive strength
        for i in range(self.dim):
            boundary_strength = 0.8 + 0.2 * np.sin(0.3 * i)
            result += boundary_strength * (5.0 - abs(x[i]))**2
        
        # Dynamic polynomial interactions
        if self.dim >= 3:
            for i in range(min(3, self.dim)):
                for j in range(i+1, min(3, self.dim)):
                    result += 0.3 * (x[i]**3 + x[j]**3) * np.sin(x[i] + x[j])
        
        return result