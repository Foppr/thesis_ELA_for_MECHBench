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
            result += 0.4 * np.exp(-0.8 * (x[i] ** 2)) * (1.0 + 0.2 * i + 0.05 * x[i]**2)
        
        # Add multi-frequency trigonometric components with radial interaction and phase shifts
        for i in range(self.dim):
            freq = 4.0 * (i + 1)
            result += 0.35 * np.sin(freq * x[i] + 0.5 * i) * np.cos(freq * x[i] - 0.3 * i) * np.exp(-0.2 * abs(x[i]))
        
        # Add radial symmetry component with varying scale and enhanced oscillation
        if self.dim >= 2:
            r = np.sqrt(x[0]**2 + x[1]**2)
            result += 0.6 * np.sin(7.0 * r + 0.2 * r**2) * np.exp(-0.3 * r)
        
        # Add cross-dimensional interaction terms with more complex coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.2 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2)) * (1.0 + 0.1 * (i + j))
        
        # Add asymmetric exponential terms with coordinate-dependent scaling and enhanced nonlinearity
        for i in range(self.dim):
            if x[i] > 0:
                result += 0.35 * np.exp(-0.5 * x[i]) * (1.0 + 0.3 * x[i]**2 + 0.05 * x[i]**4)
            else:
                result += 0.3 * np.exp(-0.6 * abs(x[i])) * (1.0 + 0.25 * x[i]**2 + 0.03 * x[i]**4)
        
        # Add high-frequency oscillatory component with varying amplitudes
        for i in range(self.dim):
            result += 0.25 * np.sin(30.0 * x[i]) * np.cos(25.0 * x[i]) * (1.0 + 0.1 * abs(x[i]))
        
        # Add polynomial interaction terms with increasing degree and enhanced coupling
        for i in range(min(self.dim, 4)):
            result += 0.2 * (x[i] ** 4) * np.sin(x[i]) * (1.0 + 0.05 * i)
            
        # Add global modulation based on sum of squares with enhanced nonlinearity
        sum_squares = np.sum(x**2)
        result += 0.4 * np.exp(-0.2 * sum_squares) * np.sin(3.0 * sum_squares + 0.1 * sum_squares**2)
        
        # Add boundary attraction term with enhanced penalty near boundaries
        for i in range(self.dim):
            result += 0.2 * (5.0 - abs(x[i]))**3
        
        # Add additional complexity with modified sine-cosine products and increased coupling
        for i in range(self.dim):
            for j in range(i+1, min(self.dim, i+3)):
                result += 0.15 * np.sin(2.0 * x[i]) * np.cos(3.0 * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2)) * (1.0 + 0.05 * (i + j))
        
        # Add modified radial component with higher frequency and stronger coupling
        if self.dim >= 3:
            r = np.sqrt(np.sum(x[:3]**2))
            result += 0.5 * np.sin(10.0 * r) * np.cos(5.0 * r) * np.exp(-0.2 * r)
        
        # Add enhanced cross-dimensional coupling with polynomial interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Introduce a small mutation: slightly modify the radial symmetry component
        if self.dim >= 2:
            r = np.sqrt(x[0]**2 + x[1]**2)
            result += 0.65 * np.sin(7.5 * r + 0.2 * r**2) * np.exp(-0.3 * r)
        
        # Add a new twist: introduce a small perturbation to the exponential decay term
        for i in range(self.dim):
            result += 0.05 * np.exp(-1.0 * (x[i] ** 2)) * np.sin(2.0 * x[i])
            
        return result