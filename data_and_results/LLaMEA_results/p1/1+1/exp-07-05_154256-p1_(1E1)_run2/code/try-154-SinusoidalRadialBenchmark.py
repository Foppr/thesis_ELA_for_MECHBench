import numpy as np

class SinusoidalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.frequencies = np.random.uniform(1.0, 10.0, dim)
        self.exponents = np.random.uniform(2.0, 6.0, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        # Radial polynomial barrier
        r = np.sqrt(np.sum(x**2))
        barrier = 1.0 / (1.0 + r**4)
        
        # Sinusoidal components with varying frequencies and amplitudes
        sin_component = 0
        for i in range(self.dim):
            sin_component += self.amplitudes[i] * np.sin(self.frequencies[i] * x[i]) * np.cos(self.frequencies[i] * x[i] * 0.5)
        
        # Radial polynomial terms with varying exponents
        poly_radial = 0
        for i in range(self.dim):
            poly_radial += x[i]**self.exponents[i]
        
        # Cross-dimensional interaction terms
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[i] * x[j]) * np.cos(x[i] * x[j] * 0.3)
        
        # Combine all components
        return (0.5 * sin_component + 
                0.3 * poly_radial + 
                0.2 * cross_term + 
                0.1 * barrier)