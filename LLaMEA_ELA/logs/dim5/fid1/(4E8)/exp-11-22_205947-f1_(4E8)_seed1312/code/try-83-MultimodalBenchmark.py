import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic logistic map with time-delayed feedback and multiple attractors
        logistic_term = 0.0
        r = 3.999  # Increased chaos parameter
        for i in range(self.dim):
            xi = x_norm[i]
            # Time-delayed logistic map with chaotic sine modulation
            delayed_val = np.sin(13 * np.pi * xi) * np.cos(7 * np.pi * xi)
            logistic_val = r * xi * (1 - xi) + 0.2 * delayed_val
            logistic_term += logistic_val * np.sin(23 * np.pi * xi)**2
        
        # Multi-modal radial basis function with dynamic centers and varying widths
        rbf_term = 0.0
        centers = np.linspace(-0.8, 0.8, min(9, self.dim))
        widths = np.linspace(0.05, 0.6, min(9, self.dim))
        for i in range(self.dim):
            rbf_sum = 0.0
            for j, (center, width) in enumerate(zip(centers, widths)):
                dist = abs(x_norm[i] - center)
                rbf_sum += np.exp(-dist**2 / (2 * width**2)) * (1 + 0.5 * np.sin(21 * np.pi * x_norm[i] + j))
            rbf_term += rbf_sum
        
        # Non-separable high-frequency trigonometric interactions with dynamic coupling
        trig_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+7, self.dim)):  # Extended coupling
                freq_i = 8 + i % 9
                freq_j = 7 + j % 8
                # Dynamic amplitude modulation with chaotic feedback
                amp_mod = 1 + 0.4 * np.sin(13 * np.pi * x_norm[i]) * np.cos(11 * np.pi * x_norm[j])
                trig_interaction += amp_mod * np.sin(freq_i * x_norm[i]) * np.cos(freq_j * x_norm[j]) * \
                                  (1 + 0.3 * np.sin(17 * np.pi * (x_norm[i] + x_norm[j])))
        
        # Polynomial and exponential mix with asymmetric curvature and dynamic scaling
        poly_exp_term = 0.0
        for i in range(self.dim):
            # Asymmetric polynomial with dynamic exponential decay and chaotic modulation
            mod = 1 + 0.2 * np.sin(19 * np.pi * x_norm[i])
            poly_exp_term += (mod * (x_norm[i]**6 + 0.8 * x_norm[i]**4 - 0.3 * x_norm[i]**2)) * \
                            np.exp(-0.9 * x_norm[i]**2)
        
        # Cross-dimensional coupling with chaotic weights and multiple interaction modes
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic weight based on both variables and their interactions
                weight = 0.7 * (1 + np.sin(x_norm[i]) * np.cos(x_norm[j]) * 
                               np.sin(5 * np.pi * (x_norm[i] + x_norm[j])) * 
                               np.cos(3 * np.pi * (x_norm[i] - x_norm[j])))
                coupling_term += weight * (x_norm[i]**2 + x_norm[j]**2) * \
                               np.sin(10 * np.pi * (x_norm[i] - x_norm[j])) * \
                               np.cos(7 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Global modulation with chaotic sine-cosine combinations
        global_mod = 0.8 * np.sin(29 * np.pi * np.sum(x_norm**2)) + 0.5 * np.cos(23 * np.pi * np.prod(x_norm)) + \
                     0.3 * np.sin(17 * np.pi * np.mean(x_norm**3))
        
        # Quaternion-inspired hybrid component
        quat_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                # Quaternion-like interaction with chaotic modulation
                q_mod = 1 + 0.3 * np.sin(17 * np.pi * x_norm[i]) * np.cos(19 * np.pi * x_norm[j])
                quat_term += q_mod * (np.sin(x_norm[i]**2) * np.cos(x_norm[j]**2) + 
                                    np.cos(x_norm[i]**2) * np.sin(x_norm[j]**2))
        
        # Adaptive sigmoidal modulation with dynamic thresholds
        sigmoid_term = 0.0
        for i in range(self.dim):
            # Sigmoidal transformation with time-varying parameters
            sig_param = 1 + 0.5 * np.sin(11 * np.pi * x_norm[i])
            sigmoid_term += (1 / (1 + np.exp(-sig_param * x_norm[i])) - 0.5) * \
                           (1 + 0.4 * np.cos(13 * np.pi * x_norm[i]))
        
        # Combine all terms with enhanced scaling and global modulation
        result = 1.0 * logistic_term + 0.8 * rbf_term + 0.7 * trig_interaction + \
                 0.6 * poly_exp_term + 0.5 * coupling_term + global_mod + 0.3 * quat_term + 0.2 * sigmoid_term
        
        return result