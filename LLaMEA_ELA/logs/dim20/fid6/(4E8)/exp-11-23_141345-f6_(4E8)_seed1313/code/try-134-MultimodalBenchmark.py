import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic oscillations with sine and cosine combinations
        chaotic_term = np.sum(np.sin(10.0 * x) * np.cos(7.0 * x) * np.sin(5.0 * x) * np.cos(3.0 * x))
        
        # Modified radial symmetry with exponential decay
        radial_term = np.sum(np.exp(-0.1 * np.sum(x**2, axis=0)) * np.cos(2.0 * np.sum(x**2, axis=0)))
        
        # Increased cross-dimensional coupling with higher-order polynomial interactions
        coupling_term = np.sum(0.7 * x[:-1]**4 * x[1:] + 0.5 * x[:-1] * x[1:]**4 + 0.3 * x[:-1]**2 * x[1:]**3 + 0.2 * x[:-1]**3 * x[1:]**2)
        
        # Novel hybrid interaction terms combining trigonometric and exponential functions
        hybrid_term = np.sum(np.exp(-x**2) * np.sin(8.0 * x) * np.cos(4.0 * x) + np.sinh(0.5 * x) * np.cos(6.0 * x))
        
        # Enhanced fractal-like gradient variations with multiple frequency components
        fractal_grad = np.sum(np.sin(6.0 * x) * np.cos(5.0 * x) * np.sin(4.0 * x) * np.cos(2.0 * x) * np.exp(-0.3 * x**2))
        
        # Additional non-linear coupling with asymmetric interaction weights and time-varying coefficients
        nonlinear_coupling = np.sum(0.9 * x[:-1]**3 * x[1:]**2 + 0.7 * x[:-1]**2 * x[1:]**3 + 0.5 * x[:-1] * x[1:]**4 + 0.3 * x[:-1]**4 * x[1:])
        
        # Multi-scale oscillation with amplitude modulation and phase shifts
        oscillation_term = np.sum(np.sin(9.0 * x) * np.cos(8.0 * x) * (1.0 + 0.4 * np.sin(5.0 * x)) * np.exp(-0.3 * x**2) + np.cos(7.0 * x) * np.sin(6.0 * x) * (1.0 + 0.3 * np.cos(4.0 * x)) * np.exp(-0.2 * x**2))
        
        # Ruggedness enhancement through polynomial and exponential interactions with adaptive scaling
        rugged_term = np.sum(0.6 * x**6 - 0.4 * x**5 + 0.3 * x**4 - 0.2 * x**3 + 0.1 * x**2 + 0.05 * x)
        
        # Combined function with optimized weights for ruggedness and multimodality
        return 0.30 * chaotic_term + 0.25 * radial_term + 0.20 * coupling_term + 0.15 * hybrid_term + 0.10 * fractal_grad + 0.08 * nonlinear_coupling + 0.07 * oscillation_term + 0.05 * rugged_term