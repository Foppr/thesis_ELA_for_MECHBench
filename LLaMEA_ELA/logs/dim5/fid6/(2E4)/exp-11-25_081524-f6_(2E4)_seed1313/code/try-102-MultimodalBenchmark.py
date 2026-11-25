import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute random parameters for oscillatory components
        self.omega = 2.0 + np.random.rand(dim) * 8.0
        self.phi = np.random.rand(dim) * 2 * np.pi
        self.gamma = 0.5 + np.random.rand(dim) * 2.0
        # Precompute ridge coefficients
        self.ridge_coeffs = np.random.randn(dim)
        # Precompute cross-dimensional coupling strengths
        self.coupling_strengths = np.random.rand(dim - 1) * 0.5
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal oscillation component
        sin_component = 0.0
        for i in range(self.dim):
            sin_component += np.sin(self.omega[i] * x[i] + self.phi[i]) * np.cos(self.gamma[i] * x[i])
            
        # Adaptive ridge structure with exponential decay
        ridge_component = 0.0
        for i in range(self.dim):
            ridge_component += self.ridge_coeffs[i] * np.exp(-0.1 * np.abs(x[i])) * np.sin(3.0 * x[i])
            
        # Cross-dimensional coupling with varying interaction strengths
        cross_coupling = 0.0
        for i in range(self.dim - 1):
            coupling_term = self.coupling_strengths[i] * np.exp(-0.05 * (x[i]**2 + x[i+1]**2)) * \
                            np.sin(0.5 * x[i] * x[i+1]) * (x[i]**2 + x[i+1]**2)
            cross_coupling += coupling_term
            
        # Nonlinear conditioning with dynamic scaling
        condition_factor = 1.0 + 0.3 * np.sin(np.sum(x**2) * 0.1) * np.cos(np.sum(x) * 0.05)
        
        # Asymmetric skewness component
        skew_component = 0.0
        for i in range(self.dim):
            skew_component += (x[i]**3) * np.exp(-0.02 * x[i]**2) * np.sin(2.0 * x[i])
            
        # Combine all components
        result = condition_factor * (sin_component + ridge_component + cross_coupling + skew_component)
        
        return result