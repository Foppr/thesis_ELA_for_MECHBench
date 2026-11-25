import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sinusoidal modulations with dynamic frequencies and amplitudes
        chaotic_term = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Use chaotic modulation for frequency and amplitude
            freq = 3 + 2 * np.sin(17 * xi) * np.cos(11 * xi)
            amp = 1.5 + 0.8 * np.sin(13 * xi) * np.cos(7 * xi)
            # Combine multiple sine waves with chaotic parameters
            chaotic_term += amp * np.sin(freq * xi) + \
                           0.6 * amp * np.sin(2 * freq * xi) + \
                           0.3 * amp * np.sin(3 * freq * xi)
        chaotic_term = chaotic_term**2
        
        # Dynamic radial basis functions with time-varying centers and widths
        rbf_term = 0.0
        num_centers = min(7, self.dim)
        centers = np.linspace(-0.8, 0.8, num_centers)
        widths = np.linspace(0.15, 0.5, num_centers)
        for i in range(self.dim):
            rbf_sum = 0.0
            for j, (center, width) in enumerate(zip(centers, widths)):
                dist = (x_norm[i] - center)**2
                # Add chaotic phase modulation to RBFs
                phase = np.sin(19 * x_norm[i] + j * np.pi / 3 + 2 * np.sin(11 * x_norm[i]))
                rbf_sum += np.exp(-dist / (2 * width**2)) * (1 + 0.4 * phase)
            rbf_term += rbf_sum
        
        # Cross-dimensional coupling with fractal-like recursive structure
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal-like coupling strength with chaotic modulation
                coupling_strength = 0.8 * (1 + np.sin(15 * x_norm[i]) * np.cos(13 * x_norm[j]))
                dist = (x_norm[i] - x_norm[j])**2
                coupling_term += coupling_strength * np.exp(-dist / 1.5) * \
                                np.sin(7 * (x_norm[i] + x_norm[j])) * \
                                np.cos(5 * (x_norm[i] - x_norm[j]))
        
        # Multi-scale polynomial chaos with Hermite polynomials and dynamic weights
        poly_term = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Use fourth-order Hermite polynomial with dynamic scaling
            h4 = 8 * xi**4 - 8 * xi**2 + 1
            weight = 1.2 + 0.6 * np.sin(11 * xi) * np.cos(9 * xi)
            poly_term += weight * h4**2
        
        # Asymmetric exponential decay with chaotic modulation
        exp_term = 0.0
        for i in range(self.dim):
            mod = 1.0 + 0.5 * np.sin(19 * x_norm[i]) * np.cos(17 * x_norm[i])
            exp_term += mod * (x_norm[i]**3 - 0.6 * x_norm[i]**2 + 0.2 * x_norm[i]) * \
                       np.exp(-0.8 * x_norm[i]**2)
        
        # Global interaction with nested fractal structure
        global_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Nested fractal coupling with recursive scaling
                scale = 0.6 * (1 + np.sin(25 * x_norm[i]) * np.cos(21 * x_norm[j]))
                global_interaction += scale * np.sin(13 * (x_norm[i] - x_norm[j])) * \
                                    np.cos(9 * (x_norm[i] + x_norm[j]))
        
        # Combine all terms with appropriate scaling factors
        result = 0.9 * chaotic_term + 0.8 * rbf_term + 0.7 * coupling_term + \
                 0.6 * poly_term + 0.5 * exp_term + 0.4 * global_interaction
        
        return result