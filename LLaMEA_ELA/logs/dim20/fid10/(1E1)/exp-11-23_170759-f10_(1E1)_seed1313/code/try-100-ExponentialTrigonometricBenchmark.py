import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale input to [-5, 5] domain if needed
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Base exponential decay term with enhanced nonlinearity and varying coefficients
        for i in range(self.dim):
            result += 0.6 * np.exp(-1.2 * (x[i] ** 2)) * (1.0 + 0.3 * i + 0.1 * x[i]**2 + 0.02 * x[i]**4)
        
        # Multi-frequency trigonometric components with stronger radial interaction and phase shifts
        for i in range(self.dim):
            freq = 6.0 * (i + 1)
            result += 0.5 * np.sin(freq * x[i] + 0.7 * i) * np.cos(freq * x[i] - 0.4 * i) * np.exp(-0.3 * abs(x[i]))
        
        # Enhanced radial symmetry component with higher frequency and stronger coupling
        if self.dim >= 2:
            r = np.sqrt(x[0]**2 + x[1]**2)
            result += 0.8 * np.sin(9.0 * r + 0.3 * r**2) * np.exp(-0.4 * r)
        
        # Complex cross-dimensional interaction terms with higher-order coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * np.exp(-0.15 * (x[i]**2 + x[j]**2)) * (1.0 + 0.2 * (i + j) + 0.05 * i * j)
        
        # Asymmetric exponential terms with enhanced nonlinearity and coordinate-dependent scaling
        for i in range(self.dim):
            if x[i] > 0:
                result += 0.5 * np.exp(-0.7 * x[i]) * (1.0 + 0.4 * x[i]**2 + 0.1 * x[i]**4 + 0.02 * x[i]**6)
            else:
                result += 0.4 * np.exp(-0.8 * abs(x[i])) * (1.0 + 0.3 * x[i]**2 + 0.05 * x[i]**4 + 0.01 * x[i]**6)
        
        # High-frequency oscillatory component with varying amplitudes and enhanced coupling
        for i in range(self.dim):
            result += 0.4 * np.sin(40.0 * x[i]) * np.cos(35.0 * x[i]) * (1.0 + 0.2 * abs(x[i]) + 0.05 * x[i]**2)
        
        # Polynomial interaction terms with higher degrees and stronger coupling
        for i in range(min(self.dim, 5)):
            result += 0.3 * (x[i] ** 5) * np.sin(x[i]) * (1.0 + 0.1 * i + 0.02 * i**2)
            
        # Global modulation based on sum of squares with intensified nonlinearity
        sum_squares = np.sum(x**2)
        result += 0.6 * np.exp(-0.3 * sum_squares) * np.sin(4.0 * sum_squares + 0.15 * sum_squares**2)
        
        # Enhanced boundary attraction term with stronger penalty near boundaries
        for i in range(self.dim):
            result += 0.3 * (5.0 - abs(x[i]))**4
        
        # Additional complexity with modified sine-cosine products and increased coupling
        for i in range(self.dim):
            for j in range(i+1, min(self.dim, i+4)):
                result += 0.2 * np.sin(3.0 * x[i]) * np.cos(4.0 * x[j]) * np.exp(-0.15 * (x[i]**2 + x[j]**2)) * (1.0 + 0.1 * (i + j) + 0.03 * i * j)
        
        # Modified radial component with even higher frequency and stronger coupling
        if self.dim >= 3:
            r = np.sqrt(np.sum(x[:3]**2))
            result += 0.7 * np.sin(12.0 * r) * np.cos(6.0 * r) * np.exp(-0.25 * r)
        
        # Enhanced cross-dimensional coupling with polynomial interactions and higher-order terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.15 * (x[i]**3 + x[j]**3) * np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Introduce a significant mutation: highly modified radial symmetry component
        if self.dim >= 2:
            r = np.sqrt(x[0]**2 + x[1]**2)
            result += 0.9 * np.sin(11.0 * r + 0.35 * r**2) * np.exp(-0.45 * r)
        
        # Add a new component: chaotic oscillatory behavior with multiple frequencies
        for i in range(self.dim):
            result += 0.25 * np.sin(50.0 * x[i] + 10.0 * np.sin(3.0 * x[i])) * (1.0 + 0.15 * abs(x[i]) + 0.03 * x[i]**2)
        
        # Add a new component: fractal-like interaction terms with recursive-like structure
        for i in range(self.dim):
            result += 0.1 * np.sin(2.0 * x[i] + 0.5 * np.sin(4.0 * x[i])) * np.exp(-0.1 * abs(x[i]))
        
        return result