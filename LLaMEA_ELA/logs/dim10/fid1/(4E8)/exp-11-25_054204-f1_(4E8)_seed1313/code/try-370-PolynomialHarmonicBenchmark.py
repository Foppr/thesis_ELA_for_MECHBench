import numpy as np

class PolynomialHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute harmonic frequencies and weights with enhanced chaos
        self.frequencies = np.arange(1, dim + 1) * (1.0 + 0.3 * np.sin(np.arange(dim) * 0.7))
        self.weights = np.exp(-np.arange(dim) * 0.25) * (1.0 + 0.2 * np.cos(np.arange(dim) * 0.5))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial chaos component with chaotic exponents
        poly_chaos = 0.0
        for i in range(self.dim):
            exponent = 4 + 2 * np.sin(0.3 * i) + 0.5 * np.cos(0.7 * i)
            poly_chaos += self.weights[i] * (x[i]**exponent + x[i]**3 - 1.5*x[i]**2 + 0.8*x[i])
        
        # Modified spherical harmonic decomposition with chaotic coupling
        spherical_harmonic = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt(x[i]**2 + x[j]**2) + 0.1 * np.sin(x[i] + x[j])
                angle = np.arctan2(x[j], x[i]) + 0.2 * np.cos(x[i] * x[j])
                spherical_harmonic += np.sin(self.frequencies[i] * angle) * np.cos(self.frequencies[j] * angle) * np.exp(-dist/4.0)
        
        # Enhanced adaptive gradient modulation with chaotic scaling
        grad_mod = 0.0
        for i in range(self.dim):
            chaotic_factor = 1.0 + 0.3 * np.sin(0.5 * x[i] + i)
            grad_mod += (x[i]**2 + 1.0) * np.sin(x[i]) * np.cos(0.5 * x[i]) * chaotic_factor
        
        # Improved cross-dimensional polynomial interactions with dynamic coupling
        cross_poly = 0.0
        for i in range(self.dim - 1):
            coupling = 1.0 + 0.3 * np.sin(i * 0.5) * np.cos((i+1) * 0.3)
            cross_poly += coupling * ((x[i] * x[i+1])**2 + (x[i] + x[i+1])**3)
        
        # Enhanced multi-scale oscillatory component with chaotic frequencies
        oscillatory = 0.0
        for i in range(self.dim):
            freq_i = self.frequencies[i] * (1.0 + 0.2 * np.sin(0.4 * i))
            oscillatory += np.sin(2.0 * freq_i * x[i]) * np.cos(3.0 * freq_i * x[i])
        
        # Enhanced fractal-like recursive interaction with chaotic scaling
        fractal = 0.0
        if self.dim >= 3:
            for i in range(self.dim - 2):
                scale = 1.0 + 0.25 * np.sin(i * 0.6)
                fractal += scale * np.sin(x[i] + x[i+1] + x[i+2]) * np.cos(x[i] * x[i+1] * x[i+2])
        
        # Enhanced dimensionality-adaptive scaling factor with chaotic component
        chaotic_scale = 1.0 + 0.4 * np.sin(0.3 * self.dim)
        scale_factor = chaotic_scale * (1.0 + 0.5 * np.log(self.dim + 1))
        
        # Combined function with modified weighted components for better conditioning
        return scale_factor * (0.8 * poly_chaos + 0.7 * spherical_harmonic + 
                              0.6 * grad_mod + 0.5 * cross_poly + 
                              0.4 * oscillatory + 0.3 * fractal)