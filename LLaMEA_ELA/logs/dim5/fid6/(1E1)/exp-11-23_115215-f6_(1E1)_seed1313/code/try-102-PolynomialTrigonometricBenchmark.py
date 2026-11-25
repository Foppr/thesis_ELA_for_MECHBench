import numpy as np

class PolynomialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute adaptive parameters for each dimension
        self.poly_orders = np.random.randint(2, 6, dim)
        self.wave_frequencies = np.random.uniform(1.0, 8.0, dim)
        self.noise_amplitudes = np.random.uniform(0.1, 0.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term with varying orders
        f_val = 0.0
        for i in range(self.dim):
            f_val += (x[i] ** self.poly_orders[i]) * (1.0 + 0.1 * np.sin(i))
        
        # Trigonometric wave components with adaptive frequencies
        for i in range(self.dim):
            f_val += 2.0 * np.sin(self.wave_frequencies[i] * x[i]) * \
                     np.cos(self.wave_frequencies[i] * x[i] * 0.7) + \
                     1.5 * np.sin(self.wave_frequencies[i] * x[i] * 3.0)
        
        # Cross-dimensional polynomial interactions
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                f_val += 0.5 * (x[i]**2) * (x[j]**3) * np.cos(x[i] + x[j])
        
        # Adaptive noise with dimension-specific amplitude
        for i in range(self.dim):
            noise = self.noise_amplitudes[i] * np.random.uniform(-1.0, 1.0)
            f_val += noise * (1.0 + 0.2 * np.sin(i * 2.0))
        
        # Coupling terms with exponential decay based on dimension distance
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(-0.5 * (j - i)) * np.sin(x[i] * x[j])
                f_val += 0.3 * coupling
        
        # Asymmetric polynomial terms with varying exponents
        for i in range(self.dim):
            f_val += 0.4 * (x[i]**(self.poly_orders[i] + 1)) * \
                     np.cos(x[i] * 0.5) + \
                     0.2 * np.sin(x[i]**2) * np.exp(-x[i]**2)
        
        # Global trigonometric modulation
        f_val += 0.6 * np.sin(np.sum(x)**2) + \
                 0.4 * np.cos(np.sum(x) * 0.3) + \
                 0.3 * np.tan(np.sum(x) * 0.1)
        
        # Dimension-specific scaling factors
        for i in range(self.dim):
            f_val *= (1.0 + 0.1 * np.sin(i * 0.5))
        
        return f_val