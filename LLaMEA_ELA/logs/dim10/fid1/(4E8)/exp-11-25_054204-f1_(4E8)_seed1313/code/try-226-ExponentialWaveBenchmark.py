import numpy as np

class ExponentialWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute adaptive weights for dimensional coupling
        self.weights = np.exp(-np.arange(dim) / (dim + 1))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Exponential decay with sinusoidal modulation
        f2 = 0.3 * np.sum(np.exp(-x**2 / 10.0) * np.sin(3.0 * x))
        
        # Multi-scale wave interference pattern
        f3 = 0.25 * np.sum(np.sin(x) * np.cos(2.0 * x) * np.sin(4.0 * x))
        
        # Adaptive dimensional coupling with exponential weights
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += self.weights[i] * np.exp(-(x[i] - x[i+1])**2 / 2.0)
        f4 = 0.4 * coupling
        
        # Radial exponential component with angular modulation
        r = np.sqrt(np.sum(x**2))
        f5 = 0.2 * np.exp(-r / 3.0) * np.cos(r)
        
        # High-frequency oscillation with adaptive amplitude
        f6 = 0.18 * np.sum(np.sin(10.0 * x) * np.cos(15.0 * x))
        
        # Cross-dimensional polynomial interaction
        poly_interaction = 0.0
        for i in range(self.dim - 2):
            poly_interaction += (x[i] * x[i+1] * x[i+2])**2
        f7 = 0.22 * poly_interaction
        
        # Logarithmic scaling with trigonometric modulation
        f8 = 0.15 * np.sum(np.log(1.0 + x**2) * np.sin(x))
        
        # Multi-modal exponential component
        f9 = 0.2 * np.sum(np.exp(-x**2) * np.cos(5.0 * x))
        
        # Sigmoidal wave with adaptive frequency
        f10 = 0.12 * np.sum(1.0 / (1.0 + np.exp(-x)) * np.sin(2.0 * x))
        
        # Fractional dimensional coupling with inverse weights
        inv_coupling = 0.0
        for i in range(self.dim - 1):
            inv_coupling += (1.0 / (i + 1)) * np.sin(x[i] * x[i+1])
        f11 = 0.18 * inv_coupling
        
        # Polynomial wave with varying exponents
        f12 = 0.1 * np.sum(x**5 * np.cos(2.0 * x))
        
        # Combined scaling factor based on dimensionality
        scale_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        # Additional harmonic component with cubic modulation
        f13 = 0.15 * np.sum(np.sin(x**3) * np.cos(3.0 * x))
        
        # Modified exponential decay with double sinusoidal modulation
        f14 = 0.12 * np.sum(np.exp(-x**2 / 5.0) * np.sin(2.0 * x) * np.cos(3.0 * x))
        
        # Final combined function
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14)