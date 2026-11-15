import numpy as np

class PolynomialGaussianModulation:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial valley terms with varying exponents
        poly_valley = 0
        for i in range(self.dim):
            poly_valley += 0.1 * (x[i]**6 - 2 * x[i]**4 + x[i]**2)
        
        # Gaussian peak terms with random centers and heights
        gaussian_peaks = 0
        num_peaks = min(5, self.dim)
        for i in range(num_peaks):
            center = np.random.uniform(-4.0, 4.0)
            height = np.random.uniform(0.5, 2.0)
            width = 0.5 + 0.5 * np.sin(i * 0.5)
            gaussian_peaks += height * np.exp(-0.5 * ((x[i % self.dim] - center) / width)**2)
        
        # Trigonometric modulation terms
        trig_mod = 0
        for i in range(self.dim):
            trig_mod += np.sin(3.0 * x[i]) * np.cos(2.0 * x[i]) + 0.3 * np.sin(7.0 * x[i])
        
        # Cross-dimensional interaction with cubic coupling
        cross_coupling = 0
        for i in range(self.dim - 1):
            cross_coupling += 0.05 * (x[i]**3 + x[i+1]**3) * (x[i] * x[i+1])
        
        # Noise term to increase complexity
        noise = 0.01 * np.sum(np.random.randn(self.dim)**2)
        
        # Combine all components
        return 1.2 * poly_valley + 0.8 * gaussian_peaks + 0.6 * trig_mod + 0.4 * cross_coupling + noise