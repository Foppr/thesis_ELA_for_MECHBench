import numpy as np

class ChaoticSpectralCouplingBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic system parameters with higher complexity
        self.chebyshev_coeffs = np.random.randn(dim, 12)
        self.quaternion_weights = np.random.uniform(-2.0, 2.0, (dim, 4))
        self.spectral_filters = np.random.uniform(0.1, 5.0, (dim, 6))
        self.coupling_strengths = np.random.uniform(0.5, 3.0, dim)
        self.fractal_depth = np.random.randint(2, 10, dim)
        self.fractal_weights = np.random.uniform(0.01, 1.5, (dim, 5))
        # Additional oscillatory components
        self.oscillation_freqs = np.random.uniform(1.0, 20.0, dim)
        self.oscillation_amplitudes = np.random.uniform(0.1, 4.0, dim)
        
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
                           coeffs[9] * T_x**9 + coeffs[10] * T_x**10 + coeffs[11] * T_x**11
        
        # Quaternion-based spectral filtering component
        spectral_term = 0.0
        for i in range(self.dim):
            # Apply quaternion-like interactions with multiple spectral filters
            q_weight = np.sum([self.quaternion_weights[i, j] * np.sin(x[i] * (j+1)) 
                              for j in range(4)])
            filter_contrib = np.sum([self.spectral_filters[i, j] * np.cos(x[i] * (j+1) * 0.5)
                                   for j in range(6)])
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
                                       np.sin(x[i] * 0.5 + x[j] * 0.3)
                coupling_term += recursive_factor * self.coupling_strengths[i] * self.coupling_strengths[j]
        
        # Fractal-like recursive structure in final combination with symmetry breaking
        fractal_term = 0.0
        for i in range(self.dim):
            # Multi-scale fractal interaction with symmetry breaking
            scale_factor = np.sum([self.fractal_weights[i, k] * np.sin(x[i] * (k+1) * 2.0 + k*0.3)
                                 for k in range(5)])
            fractal_term += scale_factor * np.sin(x[i] * 3.0) * np.cos(x[i] * 1.7)
        
        # Oscillatory component with complex interaction
        oscillatory_term = 0.0
        for i in range(self.dim):
            freq = self.oscillation_freqs[i]
            amp = self.oscillation_amplitudes[i]
            oscillatory_term += (amp * np.sin(freq * x[i]) + 
                               amp * np.cos(freq * x[i] * 0.7) + 
                               amp * np.sin(freq * x[i] * 1.3) * np.exp(-0.1 * x[i]**2))
        
        # Global modulation with quaternion-like symmetry breaking
        global_mod = 1.0 + 0.3 * np.sin(np.sum(x) * 0.3) * np.cos(np.sum(x) * 0.1) * \
                     np.sin(np.sum(x**2) * 0.05) * (1.0 + 0.2 * np.sin(np.sum(np.abs(x)) * 5.0))
        
        # Combine all components with new weighting scheme
        total = 0.25 * chaotic_term + 0.20 * spectral_term + 0.18 * coupling_term + \
                0.15 * fractal_term + 0.12 * oscillatory_term
        
        return (total * global_mod) + 0.05 * np.sum(np.abs(x))  # Add a bias term to reduce algorithmic bias