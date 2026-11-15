import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        result = np.sum(x**2)
        
        # Fractal-like chaotic perturbations with recursive sine-cosine combinations
        fractal = 0.8 * np.sum(np.sin(3.0 * np.pi * x) * np.cos(2.0 * np.pi * x) * 
                              np.sin(0.5 * np.pi * np.sin(1.5 * np.pi * x)))
        
        # Quantum-inspired coupling with complex exponential interactions
        quantum_coupling = 0.7 * np.sum(np.exp(1j * x[:-1] * x[1:]) * 
                                       (np.sin(x[:-1]) + np.cos(x[1:]))).real
        
        # Adaptive sine-cosine interaction with dimension-dependent frequencies
        adaptive_freq = np.sum(np.sin((1.0 + 0.1 * self.dim) * x) * 
                              np.cos((0.7 + 0.05 * self.dim) * x))
        
        # Modified polynomial couplings with exponential decay
        poly_coupling = 0.5 * np.sum(np.exp(-0.1 * np.abs(x)) * (x**3 + 0.3 * x**5))
        
        # Novel hyperbolic tangent-based multimodal peaks with dynamic centers
        peaks = 0.6 * np.sum(np.tanh(2.0 * x) * np.cos(3.0 * x) * np.sin(0.5 * x))
        
        # Saddle point perturbations with fractional calculus-inspired terms
        saddle = 0.2 * np.sum(np.sin(x**2) * np.cos(x**0.5) * np.tan(0.3 * x))
        
        # Additional chaotic landscape with modified logistic map interactions
        logistic_map = 0.4 * np.sum(np.sin(np.pi * np.sin(x)) * np.cos(np.pi * np.cos(x)))
        
        # Combined terms with dynamic weighting based on dimension
        dynamic_weight = 1.0 + 0.1 * np.sin(self.dim * 0.1)
        
        result = result + dynamic_weight * (fractal + quantum_coupling + adaptive_freq + 
                                          poly_coupling + peaks + saddle + logistic_map)
        
        return result