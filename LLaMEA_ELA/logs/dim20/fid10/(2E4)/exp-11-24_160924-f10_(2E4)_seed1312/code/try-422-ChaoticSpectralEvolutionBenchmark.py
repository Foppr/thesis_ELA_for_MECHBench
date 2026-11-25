import numpy as np

class ChaoticSpectralEvolutionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        
        # Tent map chaotic parameters
        self.tent_r = np.random.uniform(1.5, 3.9, dim)
        self.tent_init = np.random.uniform(0.1, 0.9, dim)
        
        # Spectral decomposition components (frequency bands)
        self.spectral_freq = np.random.uniform(2.0, 15.0, dim)
        self.spectral_amp = np.random.uniform(1.0, 5.0, dim)
        self.spectral_phase = np.random.uniform(0.0, 2*np.pi, dim)
        
        # Evolutionary pressure terms
        self.evo_pressure = np.random.uniform(0.5, 3.0, dim)
        self.evo_decay = np.random.uniform(0.1, 0.9, dim)
        
        # Cross-dimensional coupling coefficients
        self.coupling_coeffs = np.random.uniform(-1.0, 1.0, (dim, dim))
        
        # Polynomial chaos expansion terms
        self.poly_chaos = np.random.uniform(-2.0, 2.0, (dim, 4))
        
        # Adaptive scaling factors
        self.scale_factors = np.random.uniform(0.5, 2.0, dim)
        
        # Multi-scale harmonic components
        self.harmonic_freq = np.random.uniform(1.0, 8.0, dim)
        self.harmonic_amp = np.random.uniform(0.5, 3.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Tent map chaotic components
        tent_vals = np.zeros(self.dim)
        for i in range(self.dim):
            tent_val = self.tent_init[i]
            for _ in range(10):  # Iterate to reach chaotic regime
                if tent_val < 0.5:
                    tent_val = self.tent_r[i] * tent_val
                else:
                    tent_val = self.tent_r[i] * (1 - tent_val)
            tent_vals[i] = tent_val
            
        result += np.sum(tent_vals * x)
        
        # Spectral decomposition components
        for i in range(self.dim):
            spectral_term = self.spectral_amp[i] * np.sin(self.spectral_freq[i] * x[i] + self.spectral_phase[i])
            result += spectral_term
            
        # Evolutionary pressure terms
        for i in range(self.dim):
            evo_term = self.evo_pressure[i] * np.exp(-self.evo_decay[i] * (x[i]**2))
            result += evo_term
            
        # Cross-dimensional coupling
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    result += self.coupling_coeffs[i][j] * x[i] * np.sin(x[j])
                    
        # Polynomial chaos expansion terms (using Hermite polynomials)
        for i in range(self.dim):
            poly_sum = 0.0
            for k in range(4):
                hermite_poly = np.polynomial.hermite.hermval(x[i], [0]*k + [1])
                poly_sum += self.poly_chaos[i][k] * hermite_poly
            result += poly_sum
            
        # Adaptive scaling components
        for i in range(self.dim):
            result += self.scale_factors[i] * np.sin(x[i]**3) * np.cos(x[i]**2)
            
        # Multi-scale harmonic components
        for i in range(self.dim):
            result += self.harmonic_amp[i] * np.sin(self.harmonic_freq[i] * x[i]) * np.cos(self.harmonic_freq[i] * x[i]**2)
            
        # Add dimensionality-dependent noise
        result += 0.1 * np.sum(np.sin(x**4))
        
        return result