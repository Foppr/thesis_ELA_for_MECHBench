import numpy as np

class PolynomialRadialHyperbolicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale input to [-5, 5] domain if needed
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Polynomial chaos component with varying exponents and coefficients
        for i in range(self.dim):
            result += (i + 1) * (x[i]**4 + 0.5 * x[i]**3 + 0.2 * x[i]**2 + 0.1 * x[i] + 0.05)
        
        # Radial basis function with Gaussian-like shape and varying widths
        if self.dim >= 2:
            r = np.sqrt(x[0]**2 + x[1]**2)
            result += 2.0 * np.exp(-0.5 * r**2) * (1.0 + 0.3 * r * np.sin(r))
        
        # Asymmetric hyperbolic sine components with different scaling factors
        for i in range(self.dim):
            if x[i] >= 0:
                result += 1.5 * np.sinh(0.5 * x[i]) * (1.0 + 0.1 * x[i]**2)
            else:
                result += 1.2 * np.sinh(0.7 * x[i]) * (1.0 + 0.05 * x[i]**2)
        
        # Cross-dimensional coupling with polynomial interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * (x[i]**2 + x[j]**2) * np.exp(-0.1 * abs(x[i] - x[j]))
        
        # Multimodal sine-cosine combination with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = 2.0 * (i + 1)
            result += 0.5 * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7) * (1.0 + 0.2 * abs(x[i]))
        
        # Radial component with high-frequency oscillations and exponential decay
        r = np.sqrt(np.sum(x**2))
        result += 1.0 * np.sin(15.0 * r) * np.exp(-0.3 * r)
        
        # Asymmetric penalty terms near boundaries with varying strengths
        for i in range(self.dim):
            if abs(x[i]) > 4.0:
                result += 2.0 * (abs(x[i]) - 4.0)**2
            elif abs(x[i]) > 3.0:
                result += 1.0 * (abs(x[i]) - 3.0)**3
        
        # Additional high-order polynomial interaction terms
        for i in range(min(self.dim, 3)):
            for j in range(i+1, min(self.dim, i+3)):
                result += 0.2 * x[i]**3 * x[j]**2 * np.sin(x[i] + x[j])
        
        # Global modulation with inverse distance and exponential scaling
        sum_squares = np.sum(x**2)
        if sum_squares > 0:
            result += 0.8 * np.exp(-sum_squares / 10.0) * np.cos(5.0 * np.sqrt(sum_squares))
        
        return result