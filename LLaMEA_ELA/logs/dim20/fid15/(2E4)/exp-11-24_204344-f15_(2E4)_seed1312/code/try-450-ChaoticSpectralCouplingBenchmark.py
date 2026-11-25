import numpy as np

class ChaoticSpectralCouplingBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic system parameters with higher complexity
        self.chebyshev_coeffs = np.random.randn(dim, 25)
        self.quaternion_weights = np.random.uniform(-10.0, 10.0, (dim, 10))
        self.spectral_filters = np.random.uniform(0.005, 12.0, (dim, 15))
        self.coupling_strengths = np.random.uniform(0.05, 10.0, dim)
        self.fractal_depth = np.random.randint(1, 20, dim)
        self.fractal_weights = np.random.uniform(0.0005, 5.0, (dim, 12))
        # Additional oscillatory components
        self.oscillation_freqs = np.random.uniform(0.05, 50.0, dim)
        self.oscillation_amplitudes = np.random.uniform(0.005, 10.0, dim)
        # New hyperparameters for increased complexity
        self.hypercomplex_coeffs = np.random.randn(dim, 8)
        self.frequency_modulators = np.random.uniform(0.02, 5.0, (dim, 10))
        # Mutation: Slightly alter the coupling and fractal components for more ruggedness
        self.coupling_strengths *= 2.0
        self.fractal_weights *= 2.0
        # Additional mutation: Introduce higher-order polynomial nonlinearity in chaotic component
        self.polynomial_coeffs = np.random.uniform(-1.0, 1.0, (dim, 8))
        
    def f(self, x):
        x = np.array(x)
        
        # Chaotic component using Chebyshev polynomials with higher degree and polynomial modification
        chaotic_term = 0.0
        for i in range(self.dim):
            coeffs = self.chebyshev_coeffs[i]
            T_x = np.cos(coeffs[0] * np.arccos(np.clip(x[i], -1, 1)))
            chaotic_term += coeffs[1] * T_x + coeffs[2] * T_x**2 + coeffs[3] * T_x**3 + \
                           coeffs[4] * T_x**4 + coeffs[5] * T_x**5 + coeffs[6] * T_x**6 + \
                           coeffs[7] * T_x**7 + coeffs[8] * T_x**8 + \
                           coeffs[9] * T_x**9 + coeffs[10] * T_x**10 + coeffs[11] * T_x**11 + \
                           coeffs[12] * T_x**12 + coeffs[13] * T_x**13 + coeffs[14] * T_x**14 + \
                           coeffs[15] * T_x**15 + coeffs[16] * T_x**16 + coeffs[17] * T_x**17 + \
                           coeffs[18] * T_x**18 + coeffs[19] * T_x**19 + coeffs[20] * T_x**20 + \
                           coeffs[21] * T_x**21 + coeffs[22] * T_x**22 + coeffs[23] * T_x**23 + \
                           coeffs[24] * T_x**24
            # Add higher-order polynomial nonlinearity for increased ruggedness
            chaotic_term += self.polynomial_coeffs[i, 0] * x[i]**3 + \
                           self.polynomial_coeffs[i, 1] * x[i]**4 + \
                           self.polynomial_coeffs[i, 2] * x[i]**5 + \
                           self.polynomial_coeffs[i, 3] * x[i]**6 + \
                           self.polynomial_coeffs[i, 4] * x[i]**7 + \
                           self.polynomial_coeffs[i, 5] * x[i]**8 + \
                           self.polynomial_coeffs[i, 6] * x[i]**9 + \
                           self.polynomial_coeffs[i, 7] * x[i]**10
        
        # Quaternion-based spectral filtering component
        spectral_term = 0.0
        for i in range(self.dim):
            # Apply quaternion-like interactions with multiple spectral filters
            q_weight = np.sum([self.quaternion_weights[i, j] * np.sin(x[i] * (j+1)) 
                              for j in range(10)])
            filter_contrib = np.sum([self.spectral_filters[i, j] * np.cos(x[i] * (j+1) * 0.2)
                                   for j in range(15)])
            spectral_term += q_weight * filter_contrib
        
        # Adaptive coupling component with fractal-like recursive structure
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal coupling with depth-dependent interaction and quaternion modulation
                recursive_factor = 1.0
                for k in range(min(self.fractal_depth[i], self.fractal_depth[j])):
                    recursive_factor *= np.sin(x[i] * x[j] * (k+1) + np.cos(x[i] + x[j])) * \
                                       np.cos(x[i] + x[j] * (k+1)) * \
                                       np.sin(x[i] * 0.5 + x[j] * 0.3) * \
                                       np.cos(x[i] * x[j] * 0.2) * \
                                       np.exp(-0.15 * (x[i]**2 + x[j]**2))
                coupling_term += recursive_factor * self.coupling_strengths[i] * self.coupling_strengths[j]
        
        # Fractal-like recursive structure in final combination with symmetry breaking
        fractal_term = 0.0
        for i in range(self.dim):
            # Multi-scale fractal interaction with symmetry breaking
            scale_factor = np.sum([self.fractal_weights[i, k] * np.sin(x[i] * (k+1) * 4.0 + k*0.3)
                                 for k in range(12)])
            fractal_term += scale_factor * np.sin(x[i] * 5.0) * np.cos(x[i] * 3.0) * \
                           np.exp(-0.12 * x[i]**2) * np.sin(x[i] * 0.15)
        
        # Oscillatory component with complex interaction
        oscillatory_term = 0.0
        for i in range(self.dim):
            freq = self.oscillation_freqs[i]
            amp = self.oscillation_amplitudes[i]
            oscillatory_term += (amp * np.sin(freq * x[i]) + 
                               amp * np.cos(freq * x[i] * 0.4) + 
                               amp * np.sin(freq * x[i] * 1.3) * np.exp(-0.2 * x[i]**2) + \
                               amp * np.cos(freq * x[i] * 1.9) * np.sin(x[i] * 0.3) + \
                               amp * np.sin(freq * x[i] * 2.5) * np.cos(x[i] * 0.7) + \
                               amp * np.cos(freq * x[i] * 0.8) * np.exp(-0.1 * x[i]**2))
        
        # Hypercomplex modulation component
        hypercomplex_term = 0.0
        for i in range(self.dim):
            h_coeffs = self.hypercomplex_coeffs[i]
            hypercomplex_term += h_coeffs[0] * np.sin(x[i] * h_coeffs[1]) + \
                               h_coeffs[2] * np.cos(x[i] * h_coeffs[1]**2) + \
                               h_coeffs[3] * np.sin(x[i] * h_coeffs[4]) * np.cos(x[i] * h_coeffs[1]) + \
                               h_coeffs[5] * np.cos(x[i] * h_coeffs[6]) * np.sin(x[i] * h_coeffs[7])
        
        # Global modulation with quaternion-like symmetry breaking
        global_mod = 1.0 + 0.7 * np.sin(np.sum(x) * 0.3) * np.cos(np.sum(x) * 0.15) * \
                     np.sin(np.sum(x**2) * 0.06) * (1.0 + 0.4 * np.sin(np.sum(np.abs(x)) * 9.0)) * \
                     np.exp(-0.03 * np.sum(x**2))
        
        # Combine all components with new weighting scheme and introduce more ruggedness
        total = 0.22 * chaotic_term + 0.18 * spectral_term + 0.16 * coupling_term + \
                0.15 * fractal_term + 0.12 * oscillatory_term + 0.07 * hypercomplex_term
        
        # Add a more complex bias term to reduce algorithmic bias and improve fitness
        bias_term = 0.06 * np.sum(np.abs(x)) + 0.03 * np.sum(np.sin(x) * np.cos(x)) + \
                   0.02 * np.sum(np.sin(x**2) * np.cos(x)) + \
                   0.01 * np.sum(np.sin(x**3) * np.cos(x**2))
        
        return (total * global_mod) + bias_term