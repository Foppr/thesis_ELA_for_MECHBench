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
            result += 0.4 * np.exp(-0.8 * (x[i] ** 2)) * (1.0 + 0.2 * i)
        
        # Add multi-frequency trigonometric components with radial interaction and phase shifts
        for i in range(self.dim):
            freq = 4.0 * (i + 1)
            result += 0.5 * np.sin(freq * x[i] + 0.5 * i) * np.cos(freq * x[i] - 0.3 * i) * np.exp(-0.2 * abs(x[i]))
        
        # Add radial symmetry component with enhanced oscillation and scaling
        if self.dim >= 2:
            r = np.sqrt(x[0]**2 + x[1]**2)
            result += 0.6 * np.sin(8.0 * r) * np.exp(-0.3 * r) * (1.0 + 0.1 * r)
        
        # Add cross-dimensional interaction terms with higher-order coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.2 * np.sin(2.0 * (x[i] + x[j])) * np.cos(1.5 * (x[i] - x[j])) * (1.0 + 0.1 * (i + j) + 0.05 * i * j)
        
        # Add asymmetric exponential terms with more complex coordinate-dependent scaling
        for i in range(self.dim):
            if x[i] > 0:
                result += 0.35 * np.exp(-0.5 * x[i]) * (1.0 + 0.3 * x[i]**2 + 0.05 * x[i]**4)
            else:
                result += 0.3 * np.exp(-0.6 * abs(x[i])) * (1.0 + 0.25 * x[i]**2 + 0.03 * x[i]**4)
        
        # Add high-frequency oscillatory component with amplitude modulation
        for i in range(self.dim):
            result += 0.25 * np.sin(30.0 * x[i]) * np.cos(25.0 * x[i]) * (1.0 + 0.1 * abs(x[i]))
        
        # Add polynomial interaction terms with increasing degree and mixed signs
        for i in range(min(self.dim, 4)):
            result += 0.2 * (x[i] ** 4) * np.sin(2.0 * x[i]) + 0.1 * (x[i] ** 3) * np.cos(x[i])
            
        # Add global modulation based on sum of squares with additional harmonic component
        sum_squares = np.sum(x**2)
        result += 0.4 * np.exp(-0.2 * sum_squares) * np.sin(3.0 * sum_squares) * (1.0 + 0.05 * sum_squares)
        
        # Add boundary attraction term with variable strength
        for i in range(self.dim):
            result += 0.2 * (5.0 - abs(x[i]))**2 * (1.0 + 0.1 * i)
        
        return result