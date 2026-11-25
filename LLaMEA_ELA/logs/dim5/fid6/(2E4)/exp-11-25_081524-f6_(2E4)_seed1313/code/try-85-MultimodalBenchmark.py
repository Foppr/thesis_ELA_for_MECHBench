import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute random coefficients for polynomial chaos
        self.poly_coeffs = np.random.randn(3, dim)
        # Precompute wave interference parameters
        self.wave_freqs = 1.0 + np.random.rand(dim) * 4.0
        self.wave_amps = 0.5 + np.random.rand(dim) * 2.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos component with mixed degrees
        poly_chaos = 0.0
        for i in range(self.dim):
            poly_chaos += (self.poly_coeffs[0, i] * x[i]**2 + 
                          self.poly_coeffs[1, i] * x[i]**3 + 
                          self.poly_coeffs[2, i] * x[i]**4)
        
        # Trigonometric wave interference with adaptive amplitudes
        wave_interference = 0.0
        for i in range(self.dim):
            wave_interference += (self.wave_amps[i] * 
                                np.sin(self.wave_freqs[i] * x[i]) * 
                                np.cos(self.wave_freqs[i] * x[i] * 0.5))
        
        # Adaptive gradient field with directional bias
        grad_field = 0.0
        for i in range(self.dim):
            grad_field += (x[i]**2) * np.sin(x[i]) * np.cos(x[i])
            
        # Cross-dimensional coupling with exponential decay
        cross_coupling = 0.0
        for i in range(self.dim - 1):
            cross_coupling += np.exp(-0.1 * (x[i]**2 + x[i+1]**2)) * x[i] * x[i+1]
            
        # Dynamic conditioning based on position
        dynamic_cond = 1.0 + 0.3 * np.sin(np.sum(x**2) * 0.1)
        
        # Combine all components with adaptive weights
        result = dynamic_cond * (poly_chaos + wave_interference + grad_field + cross_coupling)
        
        return result