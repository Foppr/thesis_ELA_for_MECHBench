import numpy as np

class PolynomialHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial harmonic conditioning with polynomial modulation
        r = np.sqrt(np.sum(x**2))
        radial_harmonic = 1.0 + 0.3 * np.sin(0.5 * r) * np.cos(0.3 * r)
        
        # Polynomial chaos terms with varying exponents
        f1 = 0.0
        for i in range(self.dim):
            exp_factor = 2.0 + 1.5 * np.sin(0.2 * i)
            f1 += (x[i]**exp_factor) * radial_harmonic
            
        # Dynamic gradient modulation with harmonic coupling
        f2 = 0.0
        for i in range(self.dim):
            grad_mod = 1.0 + 0.4 * np.cos(0.3 * i + 0.1 * r)
            f2 += grad_mod * np.sin(x[i]) * np.exp(-0.05 * x[i]**2)
            
        # Radial harmonic coupling with cross-dimensional terms
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.6 + 0.4 * np.sin(0.2 * (i + j) + 0.1 * r)
                f3 += coupling * x[i] * x[j] * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                
        # Multi-scale spectral interactions with frequency modulation
        f4 = 0.0
        for i in range(self.dim):
            freq = 1.0 + 2.0 * np.sin(0.25 * i)
            f4 += np.cos(freq * x[i]) * np.exp(-0.02 * x[i]**2)
            
        # Adaptive boundary conditioning with polynomial penalties
        f5 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                penalty = 1.5 * (np.abs(x[i]) - 4.0)**3
                f5 += penalty * np.exp(-0.1 * x[i]**2)
                
        # Cross-dimensional polynomial interactions with dynamic coefficients
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = 0.8 + 0.4 * np.cos(0.15 * (i - j))
                f6 += coeff * x[i]**2 * x[j]**3 * np.exp(-0.04 * (x[i]**2 + x[j]**2))
                
        # Harmonic gradient terms with radial scaling
        f7 = 0.0
        for i in range(self.dim):
            harmonic_amp = 1.0 + 0.5 * np.sin(0.3 * i)
            f7 += harmonic_amp * np.cos(x[i]) * np.exp(-0.06 * r**2)
            
        # Dynamic phase-shifted polynomial terms
        f8 = 0.0
        for i in range(self.dim):
            phase_shift = 0.5 * np.cos(0.2 * i + 0.1 * r)
            exp_val = 3.0 + 2.0 * np.sin(0.1 * i)
            f8 += (x[i]**exp_val) * np.exp(-0.03 * x[i]**2) * np.cos(phase_shift)
            
        # Multi-scale radial polynomial chaos
        f9 = 0.0
        for i in range(self.dim):
            poly_degree = 4 + 2 * np.sin(0.2 * i)
            f9 += (x[i]**poly_degree) * np.exp(-0.01 * x[i]**2)
            
        # Cross-dimensional harmonic coupling with exponential decay
        f10 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.7 + 0.3 * np.sin(0.1 * (i - j))
                f10 += coupling_strength * np.sin(x[i] + x[j]) * np.exp(-0.02 * (x[i]**2 + x[j]**2))
                
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10