import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute random coefficients for polynomial chaos
        self.poly_coeffs = np.random.randn(4, dim)
        # Precompute wave interference parameters
        self.wave_freqs = 0.3 + np.random.rand(dim) * 7.0
        self.wave_amps = 0.5 + np.random.rand(dim) * 3.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial chaos component with higher-order terms
        poly_chaos = 0.0
        for i in range(self.dim):
            poly_chaos += (self.poly_coeffs[0, i] * x[i]**2 + 
                          self.poly_coeffs[1, i] * x[i]**3 + 
                          self.poly_coeffs[2, i] * x[i]**4 +
                          self.poly_coeffs[3, i] * x[i]**5)
        
        # Fractal wave interference with multiple harmonics
        wave_interference = 0.0
        for i in range(self.dim):
            wave_interference += (self.wave_amps[i] * 
                                np.sin(self.wave_freqs[i] * x[i]) * 
                                np.cos(self.wave_freqs[i] * x[i] * 0.7) *
                                np.sin(self.wave_freqs[i] * x[i] * 0.3))
        
        # Non-smooth gradient field with sharp transitions
        grad_field = 0.0
        for i in range(self.dim):
            grad_field += (x[i]**2) * np.tanh(x[i]) * np.cos(x[i])
            
        # Cross-dimensional coupling with chaotic interaction terms - mutated
        cross_coupling = 0.0
        for i in range(self.dim - 1):
            cross_coupling += np.sin(0.9 * x[i] * x[i+1]) * np.exp(-0.05 * (x[i]**2 + x[i+1]**2)) * x[i] * x[i+1]
            
        # Dynamic conditioning with chaotic modulation - mutated
        dynamic_cond = 1.0 + 0.8 * np.sin(np.sum(x**2) * 0.3) * np.cos(np.sum(x) * 0.2)
        
        # Add fractal ridge structures with modified exponents
        ridge_structure = 0.0
        for i in range(self.dim):
            ridge_structure += np.exp(-0.2 * np.abs(x[i])) * np.sin(5.0 * x[i])
            
        # Combine all components with adaptive weights
        result = dynamic_cond * (poly_chaos + wave_interference + grad_field + cross_coupling + ridge_structure)
        
        return result