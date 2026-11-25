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
            weight = 1.0 + 0.5 * np.sin(13 * xi) * np.cos(7 * xi)
            chaos_term += weight * h3**2
        
        # Radial basis function with dynamic centers and time-varying widths
        rbf_term = 0.0
        num_centers = min(5, self.dim)
        centers = np.linspace(-0.9, 0.9, num_centers)
        widths = np.linspace(0.1, 0.6, num_centers)
        for i in range(self.dim):
            rbf_sum = 0.0
            for j, (center, width) in enumerate(zip(centers, widths)):
                dist = (x_norm[i] - center)**2
                # Add dynamic phase modulation to RBFs
                phase = np.sin(19 * x_norm[i] + j * np.pi / 4)
                rbf_sum += np.exp(-dist / (2 * width**2)) * (1 + 0.3 * phase)
            rbf_term += rbf_sum
        
        # Dynamic coupling with multivariate Gaussian interactions
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Time-varying coupling strength based on chaotic modulation
                coupling_strength = 0.7 * (1 + np.sin(9 * x_norm[i]) * np.cos(11 * x_norm[j]))
                dist = (x_norm[i] - x_norm[j])**2
                coupling_term += coupling_strength * np.exp(-dist / 2) * \
                                np.sin(5 * (x_norm[i] + x_norm[j])) * \
                                np.cos(3 * (x_norm[i] - x_norm[j]))
        
        # Multi-scale sinusoidal modulation with varying frequencies and amplitudes
        sin_term = 0.0
        for i in range(self.dim):
            freq_base = 2 + (i % 5)
            amp_base = 1.0 + 0.2 * np.sin(7 * x_norm[i])
            # Combine multiple sine waves with different frequencies and amplitudes
            sin_val = amp_base * np.sin(freq_base * x_norm[i]) + \
                      0.5 * amp_base * np.sin(2 * freq_base * x_norm[i]) + \
                      0.3 * amp_base * np.sin(3 * freq_base * x_norm[i])
            sin_term += sin_val**2
        
        # Asymmetric polynomial with exponential decay and chaotic modulation
        poly_exp_term = 0.0
        for i in range(self.dim):
            mod = 1.0 + 0.4 * np.sin(17 * x_norm[i]) * np.cos(13 * x_norm[i])
            poly_exp_term += mod * (x_norm[i]**4 - 0.8 * x_norm[i]**2 + 0.15 * x_norm[i]) * \
                            np.exp(-0.7 * x_norm[i]**2)
        
        # Global interaction term with fractal-like structure
        global_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal-like coupling with recursive scaling
                scale = 0.5 * (1 + np.sin(23 * x_norm[i]) * np.cos(19 * x_norm[j]))
                global_interaction += scale * np.sin(11 * (x_norm[i] - x_norm[j])) * \
                                    np.cos(7 * (x_norm[i] + x_norm[j]))
        
        # Combine all terms with appropriate scaling factors
        result = 0.8 * chaos_term + 0.9 * rbf_term + 0.7 * coupling_term + \
                 0.6 * sin_term + 0.5 * poly_exp_term + 0.4 * global_interaction
        
        return result