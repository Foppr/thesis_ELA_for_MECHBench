import numpy as np

class ChaoticRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term
        base_term = np.sum(x**2)
        
        # Exponential decay potentials with chaotic centers
        potential_term = 0.0
        for i in range(self.dim):
            # Chaotic center positions using logistic map-like behavior
            center = 5.0 * np.sin(i * np.pi / (self.dim + 1)) * np.cos(i * np.pi / (self.dim + 2))
            distance = np.abs(x[i] - center)
            # Exponential decay with adaptive rate
            rate = 0.5 + 0.5 * np.sin(i * np.pi / self.dim)
            potential_term += np.exp(-rate * distance) * (1.0 + 0.2 * np.sin(3.0 * distance))
        
        # Sinusoidal modulation with dimensionally adaptive frequencies
        modulation_term = 0.0
        for i in range(self.dim):
            freq = 1.0 + 2.0 * np.sin(i * np.pi / (self.dim + 1))
            amp = 1.0 + 0.5 * np.cos(i * np.pi / self.dim)
            modulation_term += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] / 2.0)
        
        # Adaptive ridge structure with varying heights and widths
        ridge_term = 0.0
        for i in range(self.dim):
            # Ridge parameters vary by dimension
            height = 0.5 + 0.5 * np.sin(i * np.pi / self.dim)
            width = 1.0 + 0.3 * np.cos(i * np.pi / (self.dim + 1))
            ridge_center = 2.0 * np.sin(i * np.pi / (self.dim + 2))
            # Ridge function: Gaussian-like with adaptive parameters
            ridge_term += height * np.exp(-0.5 * ((x[i] - ridge_center) ** 2) / (width ** 2))
        
        # Cross-dimension coupling with chaotic interaction coefficients
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = np.sin(i * j * np.pi / (self.dim + 1)) * np.cos(i * j * np.pi / (self.dim + 2))
                coupling_term += coeff * (x[i] - x[j]) ** 2
        
        # Dimensionality scaling factor
        dim_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        return dim_factor * (base_term + 0.3 * potential_term + 0.2 * modulation_term + 
                           0.1 * ridge_term + 0.15 * coupling_term)