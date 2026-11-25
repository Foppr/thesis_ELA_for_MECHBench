import numpy as np

class MultiModalRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for consistent conditioning
        x_scaled = x / 5.0
        
        # Polynomial landscape with mixed degrees and exponential coefficients
        f1 = np.sum(0.8 * x_scaled**6 + 0.5 * x_scaled**5 - 0.3 * x_scaled**4 + 0.2 * x_scaled**3 + 0.1 * x_scaled**2)
        
        # Trigonometric interference with exponentially increasing frequencies and chaotic modulation
        f2 = 0.0
        for i in range(self.dim):
            freq = 2**(i+1) + 0.5 * np.sin(i)
            f2 += np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 1.3) * np.sin(freq * x_scaled[i] * 0.7)
        
        # Radial basis function components with chaotic center placement and dynamic widths
        f3 = 0.0
        for i in range(min(7, self.dim)):
            center = 0.8 * np.sin(i * 1.7) * np.cos(i * 2.3)
            width = 0.3 + 0.1 * np.sin(i * 0.9) + 0.05 * np.cos(i * 1.2)
            f3 += np.exp(-0.5 * ((x_scaled[i] - center) / width)**4)
        
        # Dynamic cross-dimensional interaction terms with exponentially varying weights
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.exp((i + j) / (self.dim * 2)) * (0.5 + 0.3 * np.sin(i * j))
                f4 += weight * np.sin(x_scaled[i]) * np.cos(x_scaled[j]) * np.tan((x_scaled[i] + x_scaled[j]) / 2)
        
        # Chaotic saddle point structure with multiple exponential terms
        f5 = np.sum(0.7 * (x_scaled**2 - 0.3)**4 + 0.3 * (x_scaled**2 - 0.6)**3)
        
        # Ultra-high frequency oscillation with chaotic modulation to increase ruggedness
        f6 = 0.0
        for i in range(self.dim):
            freq_mod = 100 + 50 * np.sin(i * 1.5) + 25 * np.cos(i * 0.8)
            f6 += np.sin(freq_mod * x_scaled[i]) * np.cos(freq_mod * x_scaled[i] * 1.1)
        
        # Combined penalty for boundary avoidance with ultra-high order exponents
        f7 = 0.8 * np.sum(np.abs(x_scaled)**5.2 + np.abs(x_scaled)**3.7 + np.abs(x_scaled)**2.1)
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7