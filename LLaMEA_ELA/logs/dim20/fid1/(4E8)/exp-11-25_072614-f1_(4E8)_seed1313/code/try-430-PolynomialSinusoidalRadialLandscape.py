import numpy as np

class PolynomialSinusoidalRadialLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize polynomial conditioning parameters
        self.poly_exponents = np.array([2.0 + 1.5 * np.sin(0.5 * np.pi * i) for i in range(dim)])
        # Initialize sinusoidal modulation frequencies and amplitudes
        self.freqs = np.array([1.0 + 0.5 * np.cos(0.3 * np.pi * i) for i in range(dim)])
        self.amps = np.array([0.8 + 0.4 * np.sin(0.4 * np.pi * i) for i in range(dim)])
        # Initialize radial basis function centers and widths
        self.centers = np.random.uniform(-4.5, 4.5, dim)
        self.widths = np.array([1.0 + 0.3 * np.cos(0.6 * np.pi * i) for i in range(dim)])
        # Dynamic adaptation factor for centers
        self.adapt_factor = 0.1 + 0.2 * np.random.rand()
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial conditioning component
        poly_component = 0.0
        for i in range(self.dim):
            poly_component += (x[i] ** self.poly_exponents[i]) * np.exp(-0.1 * x[i]**2)
        poly_component /= self.dim
        
        # Sinusoidal modulation component
        sin_component = 0.0
        for i in range(self.dim):
            sin_component += self.amps[i] * np.sin(self.freqs[i] * x[i]) * np.exp(-0.05 * x[i]**2)
        sin_component /= self.dim
        
        # Radial basis function component with dynamic center adaptation
        rbf_component = 0.0
        for i in range(self.dim):
            center_adapted = self.centers[i] + self.adapt_factor * np.sum(x)
            rbf_component += np.exp(-0.5 * ((x[i] - center_adapted) / self.widths[i])**2)
        rbf_component /= self.dim
        
        # Cross-dimensional coupling with polynomial interaction
        cross_component = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_component += (x[i] * x[j]) ** 1.5 * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        cross_component /= (self.dim * (self.dim - 1) / 2.0)
        
        # Combined fitness value with weighted components
        result = 0.3 * poly_component + 0.25 * sin_component + 0.25 * rbf_component + 0.2 * cross_component
        
        return result