import numpy as np

class ChaoticSpectralCouplingBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic system parameters with higher complexity
        self.chebyshev_coeffs = np.random.randn(dim, 12)
        self.quaternion_components = np.random.randn(dim, 4)
        self.spectral_filters = np.random.uniform(0.1, 3.0, (dim, 6))
        self.coupling_weights = np.random.uniform(-2.0, 2.0, (dim, dim))
        self.fractal_depth = np.random.randint(4, 10, dim)
        self.fractal_weights = np.random.uniform(0.1, 1.5, (dim, 5))
        # Additional oscillatory components
        self.oscillation_freqs = np.random.uniform(1.0, 15.0, dim)
        self.oscillation_amplitudes = np.random.uniform(0.5, 6.0, dim)
        # Spectral modulation parameters
        self.spectral_freqs = np.random.uniform(0.2, 2.5, dim)
        self.spectral_amps = np.random.uniform(0.8, 3.5, dim)
        
    def f(self, x):
        x = np.array(x)
        
        # Chaotic component using Chebyshev polynomials with higher degree and quaternion enhancement
        chaotic_term = 0.0
        for i in range(self.dim):
            coeffs = self.chebyshev_coeffs[i]
            T_x = np.cos(coeffs[0] * np.arccos(np.clip(x[i], -1, 1)))
            chaotic_term += coeffs[1] * T_x + coeffs[2] * T_x**2 + coeffs[3] * T_x**3 + \
                           coeffs[4] * T_x**4 + coeffs[5] * T_x**5 + coeffs[6] * T_x**6 + \
                           coeffs[7] * T_x**7 + coeffs[8] * T_x**8 + coeffs[9] * T_x**9 + \
                           coeffs[10] * T_x**10 + coeffs[11] * T_x**11
        
        # Quaternion-based spectral filtering component
        quaternion_term = 0.0
        for i in range(self.dim):
            q = self.quaternion_components[i]
            # Apply quaternion multiplication-like operations with spectral components
            quat_component = (q[0] * np.sin(x[i]) + q[1] * np.cos(x[i]) + 
                             q[2] * np.tan(x[i]) + q[3] * np.exp(-x[i]**2))
            quaternion_term += quat_component
        
        # Spectral filtering with recursive fractal scaling
        spectral_term = 0.0
        for i in range(self.dim):
            for j in range(6):
                filter_freq = self.spectral_filters[i, j]
                # Fractal-like recursive scaling with higher complexity
                scale_factor = np.sum([self.fractal_weights[i, k] * np.cos((j+1) * x[i] * (k+1) + k*0.7) 
                                     for k in range(5)])
                spectral_term += np.sin(filter_freq * x[i]) * scale_factor
        
        # Coupling between dimensions using fractal-like recursive terms and quaternion interactions
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Recursive fractal coupling with depth-dependent interaction and additional chaos
                recursive_factor = 1.0
                for k in range(min(self.fractal_depth[i], self.fractal_depth[j])):
                    recursive_factor *= np.sin(x[i] * x[j] * (k+1) + np.cos(x[i] + x[j])) * \
                                      np.cos(x[i] + x[j] * (k+1)) * \
                                      np.sin(self.coupling_weights[i, j] * x[i] * x[j])
                coupling_term += recursive_factor * (i + j) * 0.2
        
        # Gradient-enhanced component with non-uniform scaling and chaotic modulation
        grad_term = 0.0
        for i in range(self.dim):
            # Chaotic modulation of gradient term with more complex interactions
            modulator = np.sin(x[i] * 4.0) * np.cos(x[i] * 2.0) + 1.8 + 0.3 * np.sin(x[i] * 9.0)
            grad_term += (x[i]**3) * np.exp(-0.15 * x[i]**2) * np.sin(x[i] * 2.5) * modulator
        
        # Spectral coupling term between dimensions with quaternion enhancement
        spectral_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                spectral_coupling += (self.spectral_amps[i] * np.sin(self.spectral_freqs[i] * x[i]) *
                                    self.spectral_amps[j] * np.sin(self.spectral_freqs[j] * x[j])) * \
                                   (self.coupling_weights[i, j] + 0.5)
        
        # Oscillatory component with enhanced complexity
        oscillatory_term = 0.0
        for i in range(self.dim):
            freq1 = self.oscillation_freqs[i]
            amp1 = self.oscillation_amplitudes[i]
            freq2 = freq1 * np.sin(x[i] * 0.5) + 2.0
            amp2 = amp1 * np.cos(x[i] * 0.8) + 1.5
            oscillatory_term += (amp1 * np.sin(freq1 * x[i]) + amp2 * np.cos(freq2 * x[i])) * \
                               np.exp(-0.2 * x[i]**2)
        
        # Fractal-like recursive structure in final combination
        total = 0.22 * chaotic_term + 0.15 * quaternion_term + 0.18 * spectral_term + \
                0.20 * coupling_term + 0.15 * grad_term + 0.07 * spectral_coupling + \
                0.08 * oscillatory_term
        
        # Global modulation using a nonlinear transformation with fractal characteristics
        global_mod = 1.0 + 0.6 * np.sin(np.sum(x) * 0.6) * np.cos(np.sum(x) * 0.3) * \
                     np.sin(np.sum(x**2) * 0.15) * (1.0 + 0.15 * np.sin(np.sum(np.abs(x)) * 4.0))
        
        return (0.22 * chaotic_term + 0.15 * quaternion_term + 0.18 * spectral_term + \
                0.20 * coupling_term + 0.15 * grad_term + 0.07 * spectral_coupling + \
                0.08 * oscillatory_term) * global_mod