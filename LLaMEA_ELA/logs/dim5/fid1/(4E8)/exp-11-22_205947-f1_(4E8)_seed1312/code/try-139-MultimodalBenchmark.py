import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic sine-based map with nested fractal structures and multi-scale interference
        chaotic_term = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Nested fractal component with dynamic scaling and multiple feedback loops
            mod1 = 1 + 0.5 * np.sin(29 * np.pi * xi) * np.cos(17 * np.pi * xi)
            mod2 = 1 + 0.4 * np.sin(31 * np.pi * xi) * np.cos(19 * np.pi * xi)
            mod3 = 1 + 0.3 * np.sin(23 * np.pi * xi) * np.cos(13 * np.pi * xi)
            chaotic_val = mod1 * np.sin(37 * np.pi * xi) * mod2 * np.cos(29 * np.pi * xi) * mod3 * np.sin(17 * np.pi * xi)
            chaotic_term += chaotic_val * (1 + 0.6 * np.sin(13 * np.pi * xi)**3)
        
        # Modified radial basis function with fractal-like centers and multi-scale widths
        rbf_term = 0.0
        num_centers = min(12, self.dim)
        centers = np.linspace(-0.95, 0.95, num_centers)
        widths = np.logspace(-1, 0.5, num_centers)
        for i in range(self.dim):
            rbf_sum = 0.0
            for j, (center, width) in enumerate(zip(centers, widths)):
                dist = abs(x_norm[i] - center)
                rbf_sum += np.exp(-dist**2 / (2 * width**2)) * (1 + 0.5 * np.sin(31 * np.pi * x_norm[i] + j * 0.7))
            rbf_term += rbf_sum
        
        # Enhanced trigonometric coupling with multi-scale frequency and adaptive amplitude modulation
        trig_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):
                freq_i = 7 + (i % 8) * 2
                freq_j = 6 + (j % 7) * 2
                # Adaptive amplitude modulation with chaotic feedback and phase coupling
                amp_mod = 1 + 0.5 * np.sin(19 * np.pi * x_norm[i]) * np.cos(15 * np.pi * x_norm[j])
                phase_mod = 1 + 0.4 * np.sin(23 * np.pi * (x_norm[i] + x_norm[j])) * np.cos(17 * np.pi * (x_norm[i] - x_norm[j]))
                trig_term += amp_mod * np.sin(freq_i * x_norm[i]) * np.cos(freq_j * x_norm[j]) * phase_mod
        
        # Polynomial-exponential hybrid with nested fractal curvature and dynamic scaling
        poly_exp_term = 0.0
        for i in range(self.dim):
            # Fractal-like polynomial with exponential decay and multi-scale chaotic modulation
            mod = 1 + 0.4 * np.sin(25 * np.pi * x_norm[i]) * np.cos(17 * np.pi * x_norm[i])
            poly_exp_term += (mod * (x_norm[i]**7 + 0.9 * x_norm[i]**5 - 0.6 * x_norm[i]**4)) * \
                            np.exp(-0.8 * x_norm[i]**2) * (1 + 0.3 * np.sin(19 * np.pi * x_norm[i])**2)
        
        # Cross-dimensional coupling with nested fractal weights and multi-mode interaction
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Nested fractal weight based on both variables and their complex interactions
                weight = 0.8 * (1 + np.sin(x_norm[i]) * np.cos(x_norm[j]) * 
                               np.sin(9 * np.pi * (x_norm[i] + x_norm[j])) * 
                               np.cos(5 * np.pi * (x_norm[i] - x_norm[j])) * 
                               np.sin(7 * np.pi * (x_norm[i]**2 + x_norm[j]**2)))
                coupling_term += weight * (x_norm[i]**3 + x_norm[j]**3) * \
                               np.sin(13 * np.pi * (x_norm[i] - x_norm[j])) * \
                               np.cos(11 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Global modulation with nested chaotic sine-cosine combinations and fractal scaling
        global_mod = 0.9 * np.sin(37 * np.pi * np.sum(x_norm**2)) + 0.6 * np.cos(31 * np.pi * np.prod(x_norm)) + \
                     0.4 * np.sin(25 * np.pi * np.mean(x_norm**3)) + 0.3 * np.cos(19 * np.pi * np.std(x_norm))
        
        # Add enhanced interaction terms and fractal scaling to boost algorithmic challenge
        result = 1.8 * chaotic_term + 1.4 * rbf_term + 1.2 * trig_term + \
                 1.1 * poly_exp_term + 0.9 * coupling_term + global_mod
        
        # Add fractal-like noise modulation to improve algorithmic challenge and avoid trivial solutions
        noise_mod = 0.07 * np.sin(53 * np.pi * np.sum(x_norm**3)) * np.cos(41 * np.pi * np.prod(x_norm)) * \
                   np.sin(29 * np.pi * np.mean(x_norm**2))
        result += noise_mod
        
        return result