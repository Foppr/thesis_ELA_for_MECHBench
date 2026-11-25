import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial chaos expansion with Hermite polynomials and dynamic weights
        chaos_term = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Use third-order Hermite polynomial with dynamic scaling
            h3 = 2 * xi**3 - 3 * xi
            weight = 1.0 + 0.6 * np.sin(15 * xi) * np.cos(9 * xi)
            chaos_term += weight * h3**2
        
        # Radial basis function with dynamic centers and time-varying widths
        rbf_term = 0.0
        num_centers = min(5, self.dim)
        centers = np.linspace(-0.8, 0.8, num_centers)  # Slightly shifted centers
        widths = np.linspace(0.12, 0.65, num_centers)
        for i in range(self.dim):
            rbf_sum = 0.0
            for j, (center, width) in enumerate(zip(centers, widths)):
                dist = (x_norm[i] - center)**2
                # Add dynamic phase modulation to RBFs
                phase = np.sin(21 * x_norm[i] + j * np.pi / 3)
                rbf_sum += np.exp(-dist / (2 * width**2)) * (1 + 0.4 * phase)
            rbf_term += rbf_sum
        
        # Dynamic coupling with multivariate Gaussian interactions
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Time-varying coupling strength based on chaotic modulation
                coupling_strength = 0.8 * (1 + np.sin(11 * x_norm[i]) * np.cos(13 * x_norm[j]))
                dist = (x_norm[i] - x_norm[j])**2
                coupling_term += coupling_strength * np.exp(-dist / 2) * \
                                np.sin(6 * (x_norm[i] + x_norm[j])) * \
                                np.cos(4 * (x_norm[i] - x_norm[j]))
        
        # Multi-scale sinusoidal modulation with varying frequencies and amplitudes
        sin_term = 0.0
        for i in range(self.dim):
            freq_base = 2.5 + (i % 6)
            amp_base = 1.2 + 0.3 * np.sin(8 * x_norm[i])
            # Combine multiple sine waves with different frequencies and amplitudes
            sin_val = amp_base * np.sin(freq_base * x_norm[i]) + \
                      0.6 * amp_base * np.sin(2 * freq_base * x_norm[i]) + \
                      0.4 * amp_base * np.sin(3 * freq_base * x_norm[i])
            sin_term += sin_val**2
        
        # Asymmetric polynomial with exponential decay and chaotic modulation
        poly_exp_term = 0.0
        for i in range(self.dim):
            mod = 1.0 + 0.5 * np.sin(19 * x_norm[i]) * np.cos(15 * x_norm[i])
            poly_exp_term += mod * (x_norm[i]**4 - 0.9 * x_norm[i]**2 + 0.2 * x_norm[i]) * \
                            np.exp(-0.8 * x_norm[i]**2)
        
        # Global interaction term with fractal-like structure
        global_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal-like coupling with recursive scaling
                scale = 0.6 * (1 + np.sin(25 * x_norm[i]) * np.cos(21 * x_norm[j]))
                global_interaction += scale * np.sin(13 * (x_norm[i] - x_norm[j])) * \
                                    np.cos(8 * (x_norm[i] + x_norm[j]))
        
        # Combine all terms with appropriate scaling factors
        result = 0.9 * chaos_term + 1.0 * rbf_term + 0.8 * coupling_term + \
                 0.7 * sin_term + 0.6 * poly_exp_term + 0.5 * global_interaction
        
        return result