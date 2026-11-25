import numpy as np

class ChaoticHarmonicRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic system parameters with higher complexity
        self.chebyshev_coeffs = np.random.randn(dim, 9)
        self.rbf_centers = np.random.uniform(-4.8, 4.8, (dim, 7))
        self.rbf_widths = np.random.uniform(0.2, 3.0, (dim, 7))
        self.harmonic_freqs = np.random.uniform(0.3, 10.0, dim)
        self.harmonic_amplitudes = np.random.uniform(0.2, 5.0, dim)
        # Additional fractal-like recursive parameters with mutation
        self.fractal_depth = np.random.randint(3, 8, dim)
        self.fractal_weights = np.random.uniform(0.02, 1.5, (dim, 4))  # Mutated weights
        # Spectral modulation parameters with mutation
        self.spectral_freqs = np.random.uniform(0.1, 2.5, dim)  # Mutated frequencies
        self.spectral_amps = np.random.uniform(0.3, 3.5, dim)   # Mutated amplitudes
        
    def f(self, x):
        x = np.array(x)
        
        # Chaotic component using Chebyshev polynomials with higher degree
        chaotic_term = 0.0
        for i in range(self.dim):
            coeffs = self.chebyshev_coeffs[i]
            T_x = np.cos(coeffs[0] * np.arccos(np.clip(x[i], -1, 1)))
            chaotic_term += coeffs[1] * T_x + coeffs[2] * T_x**2 + coeffs[3] * T_x**3 + \
                           coeffs[4] * T_x**4 + coeffs[5] * T_x**5 + coeffs[6] * T_x**6 + \
                           coeffs[7] * T_x**7 + coeffs[8] * T_x**8
        
        # Radial basis function component with more centers and fractal-like scaling
        rbf_term = 0.0
        for i in range(self.dim):
            for j in range(7):
                center = self.rbf_centers[i, j]
                width = self.rbf_widths[i, j]
                # Fractal-like recursive scaling with higher complexity
                scale_factor = np.sum([self.fractal_weights[i, k] * np.sin((j+1) * x[i] * (k+1) + k*0.5) 
                                     for k in range(4)])
                rbf_term += np.exp(-0.5 * ((x[i] - center) / width)**2) * scale_factor
        
        # Harmonic oscillation component with multiple frequencies and fractal coupling
        harmonic_term = 0.0
        for i in range(self.dim):
            freq1 = self.harmonic_freqs[i]
            amp1 = self.harmonic_amplitudes[i]
            freq2 = freq1 * np.sin(x[i] * 0.3) + 1.0
            amp2 = amp1 * np.cos(x[i] * 0.7) + 1.0
            # Additional spectral modulation
            spec_mod = self.spectral_amps[i] * np.sin(self.spectral_freqs[i] * x[i])
            harmonic_term += (amp1 * np.sin(freq1 * x[i]) + amp2 * np.cos(freq2 * x[i] * 0.7)) * (1.0 + 0.3 * spec_mod)
        
        # Coupling between dimensions using fractal-like recursive terms
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Recursive fractal coupling with depth-dependent interaction and additional chaos
                recursive_factor = 1.0
                for k in range(min(self.fractal_depth[i], self.fractal_depth[j])):
                    recursive_factor *= np.sin(x[i] * x[j] * (k+1) + np.cos(x[i] + x[j])) * np.cos(x[i] + x[j] * (k+1))
                coupling_term += recursive_factor * (i + j) * 0.15
        
        # Gradient-enhanced component with non-uniform scaling and chaotic modulation
        grad_term = 0.0
        for i in range(self.dim):
            # Chaotic modulation of gradient term with more complex interactions
            modulator = np.sin(x[i] * 3.0) * np.cos(x[i] * 1.5) + 1.5 + 0.2 * np.sin(x[i] * 7.0)
            grad_term += (x[i]**2) * np.exp(-0.1 * x[i]**2) * np.sin(x[i] * 2) * modulator
        
        # Spectral coupling term between dimensions
        spectral_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                spectral_coupling += (self.spectral_amps[i] * np.sin(self.spectral_freqs[i] * x[i]) *
                                    self.spectral_amps[j] * np.sin(self.spectral_freqs[j] * x[j]))
        
        # Fractal-like recursive structure in final combination
        total = 0.20 * chaotic_term + 0.18 * rbf_term + 0.22 * harmonic_term + \
                0.18 * coupling_term + 0.15 * grad_term + 0.07 * spectral_coupling
        
        # Global modulation using a nonlinear transformation with fractal characteristics
        global_mod = 1.0 + 0.5 * np.sin(np.sum(x) * 0.5) * np.cos(np.sum(x) * 0.2) * \
                     np.sin(np.sum(x**2) * 0.1) * (1.0 + 0.1 * np.sin(np.sum(np.abs(x)) * 3.0))
        
        # Add a new term to improve fitness and reduce algorithmic bias
        # Introduce a smooth but highly oscillatory component that is difficult for simple algorithms to navigate
        oscillatory_term = 0.0
        for i in range(self.dim):
            # Use a combination of sinusoidal and exponential functions to create complex landscape features
            oscillatory_term += np.sin(x[i] * 12.0) * np.exp(-0.5 * x[i]**2) + \
                               np.cos(x[i] * 8.0) * np.exp(-0.3 * x[i]**2) + \
                               np.sin(x[i] * 17.0) * np.exp(-0.1 * x[i]**2)
        
        # Adjust weights to balance all components and improve overall fitness
        return (0.18 * chaotic_term + 0.16 * rbf_term + 0.20 * harmonic_term + \
                0.18 * coupling_term + 0.14 * grad_term + 0.07 * spectral_coupling + \
                0.10 * oscillatory_term) * global_mod