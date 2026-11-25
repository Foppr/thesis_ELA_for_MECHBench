import numpy as np

class MultimodalRadialCouplingBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial weights and coupling coefficients
        self.radial_weights = np.exp(-np.arange(dim) / (dim + 1))
        self.coupling_coeffs = np.sin(np.linspace(0, np.pi, dim)) * 0.5 + 0.5
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with Gaussian peaks
        radial_term = np.sum(np.exp(-0.5 * (x**2)) * np.cos(3.0 * x))
        
        # Sinusoidal oscillations with varying frequencies
        sin_term = np.sum(np.sin(2.0 * x) * np.cos(1.5 * x) * np.exp(-0.1 * x**2))
        
        # Cross-dimensional coupling with radial influence
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += self.coupling_coeffs[i] * np.sin(x[i] + x[i+1]) * np.cos(x[i] * x[i+1])
        coupling_term = 0.3 * coupling
        
        # Multimodal component with multiple local minima
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += (x[i]**4 - 10 * x[i]**2 + 5 * x[i]) * np.cos(0.5 * x[i])
        multimodal_term = 0.25 * multimodal
        
        # Radial basis function component with varying widths
        rbf = 0.0
        for i in range(self.dim):
            rbf += np.exp(-0.5 * ((x[i] - 1.0)**2) / (0.5 + i * 0.1)) + \
                   np.exp(-0.5 * ((x[i] + 1.0)**2) / (0.3 + i * 0.05))
        rbf_term = 0.4 * rbf
        
        # Saddle point structure with mixed polynomial and trigonometric terms
        saddle = 0.0
        for i in range(self.dim):
            saddle += x[i]**3 * np.sin(2.0 * x[i]) + x[i]**2 * np.cos(1.5 * x[i])
        saddle_term = 0.15 * saddle
        
        # Combined function with dimensionality scaling
        scale_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        return scale_factor * (radial_term + sin_term + coupling_term + multimodal_term + rbf_term + saddle_term)