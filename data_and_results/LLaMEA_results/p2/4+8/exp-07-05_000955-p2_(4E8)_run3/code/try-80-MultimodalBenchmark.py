import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map component for dynamic complexity
        tent = np.sum(1.0 - 2.0 * np.abs(0.5 - np.mod(x / 0.5, 1.0)))
        
        # Radial basis function with multi-scale Gaussian peaks
        rbf = np.sum(np.exp(-0.1 * np.sum((x[:, np.newaxis] - np.linspace(-5, 5, 20))**2, axis=0)))
        
        # High-dimensional coupling with polynomial interaction
        poly_coupling = np.sum((x**3 + x**5) * np.sin(2.0 * x) * np.cos(3.0 * x))
        
        # Sine-wave modulation with varying frequencies and amplitudes
        sine_mod = np.sum(np.sin(10.0 * x) * np.cos(15.0 * x) * np.exp(-0.05 * np.sum(x**2)))
        
        # Cross-dimensional interaction with exponential scaling
        exp_interaction = np.sum(np.exp(-0.2 * np.sum(x**2)) * np.sin(5.0 * x) * np.cos(7.0 * x))
        
        # Multi-modal Gaussian peaks with varying heights and widths
        gaussian_peaks = np.sum(np.exp(-0.5 * ((x - 2.0)**2 + (x + 2.0)**2)) * np.sin(8.0 * x))
        
        # Polynomial chaos expansion term with cubic and quintic components
        chaos_expansion = np.sum(x**3 * np.sin(4.0 * x) + x**5 * np.cos(6.0 * x))
        
        # Nonlinear coupling with inverse distance scaling
        inverse_coupling = np.sum(1.0 / (1.0 + np.sum((x[:, np.newaxis] - x)**2, axis=0)) * np.sin(3.0 * x))
        
        # Fractal-like structure using recursive sine and cosine operations
        fractal_term = np.sum(np.sin(np.cos(np.sin(9.0 * x))) * np.cos(np.sin(np.cos(8.0 * x))))
        
        # Combine all terms with carefully adjusted weights
        return 0.5 * tent + 0.3 * rbf + 0.2 * poly_coupling + 0.15 * sine_mod + 0.1 * exp_interaction + 0.25 * gaussian_peaks + 0.1 * chaos_expansion + 0.1 * inverse_coupling + 0.05 * fractal_term