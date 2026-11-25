import numpy as np

class PolynomialHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize polynomial correlation coefficients with cubic terms
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, (dim, 4))
        # Initialize radial barrier parameters
        self.barrier_centers = np.random.uniform(-4.0, 4.0, dim)
        self.barrier_widths = np.random.uniform(0.5, 2.0, dim)
        # Initialize harmonic oscillator frequencies with exponential modulation
        self.frequencies = np.random.uniform(0.5, 3.0, dim)
        # Initialize coupling strengths between dimensions
        self.coupling_strengths = np.random.uniform(0.1, 1.0, (dim, dim))
        # Set diagonal to zero for no self-coupling
        np.fill_diagonal(self.coupling_strengths, 0)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial correlation component with cubic terms
        poly_corr = 0
        for i in range(self.dim):
            x_i = x[i]
            poly_term = (self.poly_coeffs[i, 0] * x_i**3 + 
                        self.poly_coeffs[i, 1] * x_i**2 + 
                        self.poly_coeffs[i, 2] * x_i + 
                        self.poly_coeffs[i, 3])
            poly_corr += poly_term
        
        # Radial barrier component
        radial_barrier = 0
        for i in range(self.dim):
            center = self.barrier_centers[i]
            width = self.barrier_widths[i]
            distance = np.abs(x[i] - center)
            # Gaussian-like barrier
            radial_barrier += np.exp(-0.5 * (distance / width)**2)
        
        # Harmonic oscillator component with exponential frequency modulation
        harmonic = 0
        for i in range(self.dim):
            freq = self.frequencies[i]
            # Add sinusoidal oscillation with exponential modulation
            harmonic += np.sin(freq * x[i]) * np.exp(-0.1 * np.abs(x[i])) + 0.3 * np.sin(2 * freq * x[i])
        
        # Cross-dimension coupling with harmonic oscillators
        coupling = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling += self.coupling_strengths[i, j] * np.sin(x[i] - x[j])
        
        # Combine all components with different weights
        result = (1.2 * poly_corr + 
                 1.5 * radial_barrier + 
                 1.0 * harmonic + 
                 0.7 * coupling)
        
        return result