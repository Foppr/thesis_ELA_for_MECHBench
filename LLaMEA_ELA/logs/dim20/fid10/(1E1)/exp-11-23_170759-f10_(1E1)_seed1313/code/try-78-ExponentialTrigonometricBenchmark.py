import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale input to [-5, 5] domain if needed
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Base exponential decay term with varying coefficients and enhanced nonlinearity
        for i in range(self.dim):
            result += 0.5 * np.exp(-1.2 * (x[i] ** 2)) * (1.0 + 0.3 * i + 0.1 * x[i]**2 + 0.02 * x[i]**4)
        
        # Add multi-frequency trigonometric components with radial interaction and phase shifts
        for i in range(self.dim):
            freq = 6.0 * (i + 1)
            result += 0.5 * np.sin(freq * x[i] + 0.7 * i) * np.cos(freq * x[i] - 0.4 * i) * np.exp(-0.3 * abs(x[i]))
        
        # Add radial symmetry component with fractal-like oscillation and enhanced scaling
        if self.dim >= 2:
            r = np.sqrt(x[0]**2 + x[1]**2)
            result += 0.8 * np.sin(10.0 * r + 0.3 * r**2) * np.cos(5.0 * r) * np.exp(-0.4 * r)
        
        # Add cross-dimensional interaction terms with more complex coupling and polynomial modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * np.exp(-0.15 * (x[i]**2 + x[j]**2)) * (1.0 + 0.2 * (i + j) + 0.05 * i * j)
        
        # Add asymmetric exponential terms with coordinate-dependent scaling and enhanced nonlinearity
        for i in range(self.dim):
            if x[i] > 0:
                result += 0.45 * np.exp(-0.7 * x[i]) * (1.0 + 0.4 * x[i]**2 + 0.1 * x[i]**4 + 0.01 * x[i]**6)
            else:
                result += 0.4 * np.exp(-0.8 * abs(x[i])) * (1.0 + 0.3 * x[i]**2 + 0.05 * x[i]**4 + 0.005 * x[i]**6)
        
        # Add high-frequency oscillatory component with varying amplitudes and nested modulation
        for i in range(self.dim):
            result += 0.4 * np.sin(50.0 * x[i]) * np.cos(45.0 * x[i]) * (1.0 + 0.2 * abs(x[i]) + 0.05 * x[i]**2)
        
        # Add polynomial interaction terms with increasing degree and enhanced coupling
        for i in range(min(self.dim, 5)):
            result += 0.3 * (x[i] ** 5) * np.sin(x[i]) * (1.0 + 0.1 * i + 0.02 * i**2)
            
        # Add global modulation based on sum of squares with enhanced nonlinearity and nested exponential
        sum_squares = np.sum(x**2)
        result += 0.6 * np.exp(-0.3 * sum_squares) * np.sin(5.0 * sum_squares + 0.15 * sum_squares**2) * (1.0 + 0.05 * sum_squares)
        
        # Add boundary attraction term with enhanced penalty near boundaries and fractal-like scaling
        for i in range(self.dim):
            result += 0.4 * (5.0 - abs(x[i]))**4
        
        # Add additional complexity with modified sine-cosine products and increased coupling
        for i in range(self.dim):
            for j in range(i+1, min(self.dim, i+4)):
                result += 0.25 * np.sin(3.0 * x[i]) * np.cos(4.0 * x[j]) * np.exp(-0.15 * (x[i]**2 + x[j]**2)) * (1.0 + 0.1 * (i + j) + 0.02 * i * j)
        
        # Add modified radial component with higher frequency, stronger coupling and nested oscillations
        if self.dim >= 3:
            r = np.sqrt(np.sum(x[:3]**2))
            result += 0.7 * np.sin(15.0 * r) * np.cos(8.0 * r) * np.exp(-0.3 * r) * (1.0 + 0.1 * r)
        
        # Add enhanced cross-dimensional coupling with polynomial interactions and nested exponential
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.2 * (x[i]**2 + x[j]**2)**2 * np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2)) * (1.0 + 0.05 * i * j)
        
        # Add fractal-like nested component with multiple scales and enhanced oscillations
        if self.dim >= 4:
            r = np.sqrt(np.sum(x[:4]**2))
            result += 0.3 * np.sin(20.0 * r) * np.cos(12.0 * r) * np.sin(8.0 * r) * np.exp(-0.25 * r)
        
        return result