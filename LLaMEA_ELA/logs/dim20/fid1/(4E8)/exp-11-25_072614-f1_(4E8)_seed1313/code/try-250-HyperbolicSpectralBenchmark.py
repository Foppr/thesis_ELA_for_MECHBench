import numpy as np

class HyperbolicSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute quantum harmonic oscillator frequencies
        self.freqs = 2.0 + 1.5 * np.sin(np.linspace(0, 3*np.pi, dim) / 3.0)
        # Hyperbolic tangent chaotic coupling coefficients
        self.tanh_coeffs = 0.8 + 0.4 * np.tanh(np.linspace(0, 2*np.pi, dim))
        # Adaptive elastic net regularization parameters
        self.elastic_params = 0.5 + 0.3 * np.cos(np.linspace(0, np.pi, dim))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum harmonic oscillator component with hyperbolic coupling
        quantum_term = 0.0
        for i in range(self.dim):
            freq = self.freqs[i]
            # Hyperbolic tangent chaotic coupling with previous dimension
            if i > 0:
                tanh_coupling = np.tanh(x[i-1] * x[i]) + 0.3 * np.tanh(x[i-1] + x[i])
                quantum_term += freq * (np.sin(x[i])**2 + np.cos(x[i])**2) * tanh_coupling
            else:
                quantum_term += freq * (np.sin(x[i])**2 + np.cos(x[i])**2)
        quantum_term /= self.dim
        
        # Hyperbolic spectral decomposition with fractal-like modulation
        spectral_term = 0.0
        for i in range(self.dim):
            # Fractal-like frequency modulation using hyperbolic functions
            mod_freq = 1.5 + 0.8 * np.tanh(i * np.pi / (self.dim + 1)) + 0.3 * np.sin(x[i])
            spectral_term += self.tanh_coeffs[i] * np.tanh(mod_freq * x[i]) * np.cosh(mod_freq * x[i])
        spectral_term /= self.dim
        
        # Adaptive elastic net penalty with dynamic regularization
        elastic_term = 0.0
        for i in range(self.dim):
            # Dynamic elastic coefficient based on dimension and value with hyperbolic modulation
            elastic_coeff = self.elastic_params[i] + 0.2 * np.tanh(x[i]) + 0.1 * np.sinh(x[i])
            elastic_term += elastic_coeff * (np.abs(x[i]) + 0.4 * x[i]**2)
        elastic_term /= self.dim
        
        # Cross-dimensional interaction with hyperbolic coupling and fractal terms
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Hyperbolic coupling between dimensions with fractal modulation
                tanh_coupling = np.tanh(x[i] * x[j]) + 0.5 * np.sinh(x[i] - x[j])
                fractal_term = np.cosh(0.5 * (x[i]**2 + x[j]**2)) + 0.3 * np.tanh(x[i] + x[j])
                cross_term += tanh_coupling * fractal_term
        cross_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Fractal spatial dynamics with hyperbolic harmonics
        fractal_term = 0.0
        for i in range(self.dim):
            # Hyperbolic harmonic oscillators with different frequencies and coupling
            freq = 1.0 + 0.7 * np.tanh(i * np.pi / self.dim) + 0.4 * np.cos(x[i])
            fractal_term += np.tanh(freq * x[i]) * np.cosh(2.0 * freq * x[i]) + 0.5 * np.sinh(freq * x[i])
        fractal_term /= self.dim
        
        # Asymmetric distortion with hyperbolic transformation
        asym_term = 0.0
        for i in range(self.dim):
            # Apply hyperbolic tangent map to input for asymmetric effect
            tanh_val = np.tanh(self.tanh_coeffs[i] * x[i])
            asym_term += np.abs(tanh_val) + 0.5 * tanh_val**2
        asym_term /= self.dim
        
        # Dynamic conditioning factor with hyperbolic modulation
        cond_factor = 1.0 + 0.4 * np.tanh(np.mean(np.abs(x))) + 0.2 * np.sinh(self.dim * np.pi / 6.0)
        
        # Combine all terms with dynamic weights based on chaotic parameters
        total = (0.25 * quantum_term + 
                0.20 * spectral_term + 
                0.18 * elastic_term + 
                0.17 * cross_term + 
                0.15 * fractal_term + 
                0.05 * asym_term) * cond_factor
        
        return total