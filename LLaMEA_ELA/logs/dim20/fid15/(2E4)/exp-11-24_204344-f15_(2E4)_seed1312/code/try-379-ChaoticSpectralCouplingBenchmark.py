import numpy as np

class ChaoticSpectralCouplingBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic system parameters with higher complexity
        self.chebyshev_coeffs = np.random.randn(dim, 12)
        self.quaternion_components = np.random.randn(dim, 4)
        self.spectral_filters = np.random.uniform(0.1, 5.0, (dim, 6))
        self.coupling_strengths = np.random.uniform(0.5, 3.0, dim)
        self.fractal_depth = np.random.randint(4, 10, dim)
        self.fractal_weights = np.random.uniform(0.1, 2.0, (dim, 5))
        # Additional spectral modulation parameters
        self.spectral_freqs = np.random.uniform(0.05, 3.0, dim)
        self.spectral_amps = np.random.uniform(0.3, 4.0, dim)
        # Symmetry breaking parameters
        self.symmetry_breaking = np.random.uniform(-0.5, 0.5, dim)
        
    def f(self, x):
        x = np.array(x)
        
        # Chaotic component using Chebyshev polynomials with higher degree and quaternion integration
        chaotic_term = 0.0
        for i in range(self.dim):
            coeffs = self.chebyshev_coeffs[i]
            T_x = np.cos(coeffs[0] * np.arccos(np.clip(x[i], -1, 1)))
            chaotic_term += coeffs[1] * T_x + coeffs[2] * T_x**2 + coeffs[3] * T_x**3 + \
                           coeffs[4] * T_x**4 + coeffs[5] * T_x**5 + coeffs[6] * T_x**6 + \
                           coeffs[7] * T_x**7 + coeffs[8] * T_x**8 + \
                           coeffs[9] * T_x**9 + coeffs[10] * T_x**10 + coeffs[11] * T_x**11
        
        # Quaternion-based spectral filtering component
        quaternion_term = 0.0
        for i in range(self.dim):
            q = self.quaternion_components[i]
            # Quaternion multiplication with x[i]
            quat_result = (q[0] * x[i] - q[1] * x[i] * 0.5 + q[2] * x[i]**2 - q[3] * x[i]**3)
            quaternion_term += quat_result * np.sin(x[i] * 2.0) * np.cos(x[i] * 1.5)
        
        # Spectral filtering component with adaptive coupling
        spectral_term = 0.0
        for i in range(self.dim):
            for j in range(6):
                filter_freq = self.spectral_filters[i, j]
                spectral_term += np.sin(filter_freq * x[i]) * np.exp(-0.1 * (x[i] - j)**2)
        
        # Fractal-like recursive coupling between dimensions with symmetry breaking
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Recursive fractal coupling with depth-dependent interaction and additional chaos
                recursive_factor = 1.0
                depth = min(self.fractal_depth[i], self.fractal_depth[j])
                for k in range(depth):
                    recursive_factor *= np.sin(x[i] * x[j] * (k+1) + np.cos(x[i] + x[j])) * \
                                       np.cos(x[i] + x[j] * (k+1)) * \
                                       np.sin(self.symmetry_breaking[i] * x[i] + self.symmetry_breaking[j] * x[j])
                coupling_term += recursive_factor * self.coupling_strengths[i] * self.coupling_strengths[j]
        
        # Adaptive spectral modulation component
        adaptive_term = 0.0
        for i in range(self.dim):
            freq = self.spectral_freqs[i]
            amp = self.spectral_amps[i]
            # Adaptive modulation based on x[i] and fractal weights
            mod_factor = np.sum([self.fractal_weights[i, k] * np.sin(x[i] * (k+1)) 
                               for k in range(5)])
            adaptive_term += amp * np.sin(freq * x[i]) * mod_factor
        
        # Gradient-enhanced component with non-uniform scaling and chaotic modulation
        grad_term = 0.0
        for i in range(self.dim):
            # Chaotic modulation of gradient term with more complex interactions
            modulator = np.sin(x[i] * 4.0) * np.cos(x[i] * 2.0) + 1.8 + 0.3 * np.sin(x[i] * 9.0)
            grad_term += (x[i]**3) * np.exp(-0.05 * x[i]**2) * np.sin(x[i] * 3) * modulator
        
        # Symmetry breaking term to introduce complex patterns
        symmetry_term = 0.0
        for i in range(self.dim):
            symmetry_term += self.symmetry_breaking[i] * np.sin(x[i] * 5.0) * np.cos(x[i] * 3.0)
        
        # Fractal-like recursive structure in final combination
        total = 0.22 * chaotic_term + 0.18 * quaternion_term + 0.20 * spectral_term + \
                0.18 * coupling_term + 0.15 * adaptive_term + 0.07 * grad_term + \
                0.06 * symmetry_term
        
        # Global modulation using a nonlinear transformation with fractal characteristics
        global_mod = 1.0 + 0.6 * np.sin(np.sum(x) * 0.6) * np.cos(np.sum(x) * 0.3) * \
                     np.sin(np.sum(x**2) * 0.15) * (1.0 + 0.15 * np.sin(np.sum(np.abs(x)) * 4.0))
        
        # Add a new term to improve fitness and reduce algorithmic bias
        # Introduce a smooth but highly oscillatory component that is difficult for simple algorithms to navigate
        oscillatory_term = 0.0
        for i in range(self.dim):
            # Use a combination of sinusoidal and exponential functions to create complex landscape features
            oscillatory_term += np.sin(x[i] * 12.0) * np.exp(-0.5 * x[i]**2) + \
                               np.cos(x[i] * 9.0) * np.exp(-0.3 * x[i]**2) + \
                               np.sin(x[i] * 18.0) * np.exp(-0.1 * x[i]**2) + \
                               np.cos(x[i] * 15.0) * np.exp(-0.2 * x[i]**2)
        
        # Adjust weights to balance all components and improve overall fitness
        return (0.18 * chaotic_term + 0.16 * quaternion_term + 0.18 * spectral_term + \
                0.18 * coupling_term + 0.14 * adaptive_term + 0.10 * grad_term + \
                0.07 * symmetry_term + 0.09 * oscillatory_term) * global_mod