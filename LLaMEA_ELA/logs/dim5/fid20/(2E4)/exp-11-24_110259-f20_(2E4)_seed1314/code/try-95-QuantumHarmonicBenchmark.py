import numpy as np

class QuantumHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize polynomial chaos coefficients
        self.poly_coeffs = np.random.randn(dim, 6) * 0.5
        # Quantum harmonic oscillator parameters
        self.oscillator_freqs = np.random.rand(dim) * 2.0 + 1.0
        self.oscillator_masses = np.random.rand(dim) * 0.5 + 0.5
        # Stochastic differential equation parameters
        self.diffeq_params = np.random.rand(dim) * 2.0 + 1.0
        # Dynamic coupling weights between dimensions
        self.coupling_weights = np.random.rand(dim, dim) * 0.3 + 0.1
        # Entangled energy wells
        self.entanglement_strengths = np.random.rand(dim, dim) * 0.4 + 0.1
        # Adaptive coupling strengths
        self.adaptive_couplings = np.random.rand(dim) * 0.8 + 0.2
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Polynomial chaos expansion terms
        poly_terms = []
        for i in range(self.dim):
            coeffs = self.poly_coeffs[i]
            x_i = x_norm[i]
            # 6th order polynomial with mixed monomials
            poly_val = (coeffs[0] + 
                       coeffs[1] * x_i + 
                       coeffs[2] * x_i**2 + 
                       coeffs[3] * x_i**3 + 
                       coeffs[4] * x_i**4 + 
                       coeffs[5] * x_i**5)
            poly_terms.append(poly_val)
        
        # Quantum harmonic oscillator components
        quantum_terms = []
        for i in range(self.dim):
            x_i = x_norm[i]
            # Harmonic oscillator potential with mass and frequency
            potential = 0.5 * self.oscillator_masses[i] * (self.oscillator_freqs[i] * x_i)**2
            # Quantum correction term
            quantum_corr = np.sin(self.oscillator_freqs[i] * x_i) * np.exp(-0.1 * x_i**2)
            quantum_terms.append(potential + quantum_corr)
        
        # Cross-dimension entanglement with dynamic weights
        entanglement_terms = []
        for i in range(self.dim):
            entanglement_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    # Entangled interaction between dimensions
                    entanglement_sum += self.entanglement_strengths[i][j] * np.cos(x_norm[i] * x_norm[j])
            entanglement_terms.append(entanglement_sum)
        
        # Adaptive coupling modulation
        coupling_mod = []
        for i in range(self.dim):
            x_i = x_norm[i]
            # Adaptive scaling based on position and coupling strength
            mod_factor = 1.0 + self.adaptive_couplings[i] * np.sin(3.0 * x_i) * np.cos(2.0 * x_i)
            coupling_mod.append(mod_factor)
        
        # Combine all terms with quantum-inspired weighting
        result = (np.sum(np.array(poly_terms) * np.array(coupling_mod)) + 
                 0.8 * np.sum(np.array(quantum_terms)) + 
                 0.2 * np.sum(np.array(entanglement_terms)))
        
        # Add global scaling and quantum noise
        global_scale = 1.0 + 0.15 * np.sin(0.3 * np.sum(x_norm**2))
        quantum_noise = np.random.normal(0, 0.08) * (1.0 + 0.1 * np.cos(np.sum(x_norm)))
        
        return result * global_scale + quantum_noise