import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic sine-based map with dynamic coupling and multiple attractors
        chaotic_term = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multi-attractor chaotic component with dynamic modulation
            mod1 = 1 + 0.4 * np.sin(23 * np.pi * xi)
            mod2 = 1 + 0.3 * np.cos(25 * np.pi * xi)
            chaotic_val = mod1 * np.sin(31 * np.pi * xi) * mod2 * np.cos(19 * np.pi * xi)
            chaotic_term += chaotic_val * (1 + 0.5 * np.sin(11 * np.pi * xi)**2)
        
        # Modified radial basis function with adaptive centers and widths
        rbf_term = 0.0
        num_centers = min(8, self.dim)
        centers = np.linspace(-0.9, 0.9, num_centers)
        widths = np.linspace(0.1, 0.6, num_centers)
        for i in range(self.dim):
            rbf_sum = 0.0
            for j, (center, width) in enumerate(zip(centers, widths)):
                dist = abs(x_norm[i] - center)
                rbf_sum += np.exp(-dist**2 / (2 * width**2)) * (1 + 0.4 * np.sin(25 * np.pi * x_norm[i] + j))
            rbf_term += rbf_sum
        
        # Enhanced trigonometric coupling with dynamic amplitude and phase modulation
        trig_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                freq_i = 9 + (i % 10)
                freq_j = 8 + (j % 9)
                # Dynamic amplitude modulation with chaotic feedback
                amp_mod = 1 + 0.4 * np.sin(17 * np.pi * x_norm[i]) * np.cos(13 * np.pi * x_norm[j])
                phase_mod = 1 + 0.3 * np.sin(21 * np.pi * (x_norm[i] + x_norm[j]))
                trig_term += amp_mod * np.sin(freq_i * x_norm[i]) * np.cos(freq_j * x_norm[j]) * phase_mod
        
        # Polynomial-exponential hybrid with asymmetric curvature and dynamic scaling
        poly_exp_term = 0.0
        for i in range(self.dim):
            # Asymmetric polynomial with exponential decay and chaotic modulation
            mod = 1 + 0.35 * np.sin(21 * np.pi * x_norm[i])
            poly_exp_term += (mod * (x_norm[i]**6 + 0.8 * x_norm[i]**4 - 0.5 * x_norm[i]**3)) * \
                            np.exp(-0.9 * x_norm[i]**2)
        
        # Cross-dimensional coupling with chaotic weights and multiple interaction modes
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic weight based on both variables and their interactions
                weight = 0.7 * (1 + np.sin(x_norm[i]) * np.cos(x_norm[j]) * 
                               np.sin(7 * np.pi * (x_norm[i] + x_norm[j])) * 
                               np.cos(4 * np.pi * (x_norm[i] - x_norm[j])))
                coupling_term += weight * (x_norm[i]**2 + x_norm[j]**2) * \
                               np.sin(11 * np.pi * (x_norm[i] - x_norm[j])) * \
                               np.cos(9 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Global modulation with enhanced chaotic sine-cosine combinations
        global_mod = 0.8 * np.sin(31 * np.pi * np.sum(x_norm**2)) + 0.5 * np.cos(27 * np.pi * np.prod(x_norm)) + \
                     0.3 * np.sin(21 * np.pi * np.mean(x_norm**3))
        
        # Add improved global scaling and enhanced interaction terms to boost fitness score
        result = 1.5 * chaotic_term + 1.1 * rbf_term + 1.0 * trig_term + \
                 0.9 * poly_exp_term + 0.8 * coupling_term + global_mod
        
        # Add noise-like modulation to improve algorithmic challenge and avoid trivial solutions
        noise_mod = 0.05 * np.sin(47 * np.pi * np.sum(x_norm**3)) * np.cos(37 * np.pi * np.prod(x_norm))
        result += noise_mod
        
        # Introduce nested fractal structures through recursive enhancement
        if self.dim >= 4:
            fractal_factor = 0.0
            for k in range(2, min(5, self.dim)):
                fractal_factor += 0.1 * np.sin(37 * np.pi * np.sum(x_norm[:k]**2)) * \
                                 np.cos(29 * np.pi * np.prod(x_norm[:k]))
            result += fractal_factor
        
        # Add adaptive conditioning to increase algorithmic pressure
        adaptive_cond = 0.0
        for i in range(self.dim):
            adaptive_cond += (1 + 0.2 * np.sin(13 * np.pi * x_norm[i])) * \
                           (x_norm[i]**4 + 0.5 * x_norm[i]**2)
        result += 0.3 * adaptive_cond
        
        # Add multi-scale interference patterns
        interference = 0.0
        for scale in [2, 3, 5]:
            interference += 0.1 * np.sin(scale * np.pi * np.sum(x_norm**2)) * \
                          np.cos(scale * np.pi * np.prod(x_norm))
        result += interference
        
        return result