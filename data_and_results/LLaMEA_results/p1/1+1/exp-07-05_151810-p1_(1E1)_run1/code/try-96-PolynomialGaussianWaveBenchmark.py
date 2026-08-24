import numpy as np

class PolynomialGaussianWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute Gaussian mixture weights and centers
        self.gauss_centers = np.random.uniform(-4.0, 4.0, (10, dim))
        self.gauss_weights = np.random.dirichlet(np.ones(10))
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component with mixed monomials
        poly_chaos = 0.0
        for i in range(self.dim):
            poly_chaos += (x[i]**4 + 0.5 * x[i]**3 - 0.3 * x[i]**2 + 0.1 * x[i]) * np.cos(0.5 * i)
        
        # Gaussian mixture model component
        gauss_component = 0.0
        for i in range(10):
            diff = x - self.gauss_centers[i]
            gauss_component += self.gauss_weights[i] * np.exp(-0.5 * np.sum(diff**2) / (0.5 + 0.2 * np.sin(i)))
        
        # Trigonometric wave interference pattern
        wave_interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                wave_interference += np.sin(2.0 * x[i] + 1.5 * x[j]) * np.cos(1.0 * x[i] - 0.8 * x[j])
        
        # Multi-scale harmonic modulation with spatial coupling
        harmonic_mod = 0.0
        for i in range(self.dim):
            harmonic_mod += (1.0 + 0.5 * np.sin(3.0 * x[i])) * (1.0 + 0.3 * np.cos(2.0 * x[i])) * np.exp(-0.1 * x[i]**2)
        
        # Add coupling between dimensions through a chaotic logistic map
        logistic_coupling = 0.0
        r = 3.9
        for i in range(self.dim):
            if i == 0:
                logistic_coupling += r * x[i] * (1.0 - x[i])
            else:
                logistic_coupling += r * x[i-1] * (1.0 - x[i-1])
        
        # Combine all components
        result = poly_chaos + gauss_component + wave_interference + harmonic_mod + logistic_coupling
        
        return result