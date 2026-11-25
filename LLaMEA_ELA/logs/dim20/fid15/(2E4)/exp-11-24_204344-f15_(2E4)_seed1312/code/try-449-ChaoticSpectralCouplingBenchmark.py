import numpy as np

class ChaoticSpectralCouplingBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic system parameters with higher complexity
        self.chebyshev_coeffs = np.random.randn(dim, 20)
        self.quaternion_weights = np.random.uniform(-5.0, 5.0, (dim, 7))
        self.spectral_filters = np.random.uniform(0.01, 8.0, (dim, 10))
        self.coupling_strengths = np.random.uniform(0.1, 6.0, dim)
        self.fractal_depth = np.random.randint(1, 15, dim)
        self.fractal_weights = np.random.uniform(0.001, 3.0, (dim, 9))
        # Additional oscillatory components
        self.oscillation_freqs = np.random.uniform(0.1, 30.0, dim)
        self.oscillation_amplitudes = np.random.uniform(0.01, 7.0, dim)
        # New hyperparameters for increased complexity
        self.hypercomplex_coeffs = np.random.randn(dim, 5)
        self.frequency_modulators = np.random.uniform(0.05, 3.0, (dim, 6))
        # Mutation: Slightly alter the coupling and fractal components for more ruggedness
        self.coupling_strengths *= 1.8
        self.fractal_weights *= 2.0
        # Mutation: Adjust oscillatory frequencies to increase complexity
        self.oscillation_freqs *= 1.5
        # Enhanced symmetry breaking and increased nonlinearity
        self.symmetry_breakers = np.random.uniform(-0.5, 0.5, dim)
        self.nonlinear_exponents = np.random.uniform(1.5, 4.0, dim)
        
    def f(self, x):
        x = np.array(x)
        
        # Chaotic component using Chebyshev polynomials with higher degree
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
                           coeffs[18] * T_x**18 + coeffs[19] * T_x**19
        
        # Quaternion-based spectral filtering component
        spectral_term = 0.0
        for i in range(self.dim):
            # Apply quaternion-like interactions with multiple spectral filters
            q_weight = np.sum([self.quaternion_weights[i, j] * np.sin(x[i] * (j+1)) 
                              for j in range(7)])
            filter_contrib = np.sum([self.spectral_filters[i, j] * np.cos(x[i] * (j+1) * 0.3)
                                   for j in range(10)])
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
                                       np.exp(-0.1 * (x[i]**2 + x[j]**2))
                coupling_term += recursive_factor * self.coupling_strengths[i] * self.coupling_strengths[j]
        
        # Fractal-like recursive structure in final combination with symmetry breaking
        fractal_term = 0.0
        for i in range(self.dim):
            # Multi-scale fractal interaction with symmetry breaking
            scale_factor = np.sum([self.fractal_weights[i, k] * np.sin(x[i] * (k+1) * 3.0 + k*0.5)
                                 for k in range(9)])
            fractal_term += scale_factor * np.sin(x[i] * 4.0) * np.cos(x[i] * 2.0) * \
                           np.exp(-0.08 * x[i]**2) * np.sin(x[i] * 0.1)
        
        # Oscillatory component with complex interaction and enhanced nonlinearity
        oscillatory_term = 0.0
        for i in range(self.dim):
            freq = self.oscillation_freqs[i]
            amp = self.oscillation_amplitudes[i]
            # Enhanced oscillatory structure with symmetry breaking and nonlinear exponents
            oscillatory_term += (amp * np.sin(freq * x[i]) + 
                               amp * np.cos(freq * x[i] * 0.5) + 
                               amp * np.sin(freq * x[i] * 1.5) * np.exp(-0.15 * x[i]**2) + \
                               amp * np.cos(freq * x[i] * 1.7) * np.sin(x[i] * 0.4) + \
                               amp * np.sin(freq * x[i] * 2.0) * np.cos(x[i] * 0.6)) * \
                              (1.0 + self.symmetry_breakers[i] * np.sin(x[i] * 3.0)) * \
                              (1.0 + 0.1 * np.abs(x[i])**self.nonlinear_exponents[i])
        
        # Hypercomplex modulation component
        hypercomplex_term = 0.0
        for i in range(self.dim):
            h_coeffs = self.hypercomplex_coeffs[i]
            hypercomplex_term += h_coeffs[0] * np.sin(x[i] * h_coeffs[1]) + \
                               h_coeffs[2] * np.cos(x[i] * h_coeffs[1]**2) + \
                               h_coeffs[3] * np.sin(x[i] * h_coeffs[4]) * np.cos(x[i] * h_coeffs[1])
        
        # Global modulation with quaternion-like symmetry breaking
        global_mod = 1.0 + 0.5 * np.sin(np.sum(x) * 0.4) * np.cos(np.sum(x) * 0.2) * \
                     np.sin(np.sum(x**2) * 0.08) * (1.0 + 0.3 * np.sin(np.sum(np.abs(x)) * 7.0)) * \
                     np.exp(-0.02 * np.sum(x**2))
        
        # Combine all components with new weighting scheme and introduce more ruggedness
        total = 0.25 * chaotic_term + 0.20 * spectral_term + 0.18 * coupling_term + \
                0.17 * fractal_term + 0.10 * oscillatory_term + 0.05 * hypercomplex_term
        
        # Add a more complex bias term to reduce algorithmic bias and improve fitness
        bias_term = 0.04 * np.sum(np.abs(x)) + 0.02 * np.sum(np.sin(x) * np.cos(x)) + \
                   0.01 * np.sum(np.sin(x**2) * np.cos(x))
        
        return (total * global_mod) + bias_term