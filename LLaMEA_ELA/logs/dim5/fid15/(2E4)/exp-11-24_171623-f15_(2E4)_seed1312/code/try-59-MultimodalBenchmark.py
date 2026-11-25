import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic sine-wave interactions with higher frequency modulation and phase shifts
        chaotic_term = 0
        for i in range(self.dim):
            freq_mod = 1 + 0.7 * np.sin(5 * np.pi * x_norm[i]) + 0.3 * np.cos(2 * np.pi * x_norm[i])
            phase_shift = np.sin(4 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[i])
            chaotic_term += np.sin(freq_mod * np.pi * x_norm[i]) * np.cos(freq_mod * 2 * np.pi * x_norm[i]) * phase_shift
        
        # Dynamic radial basis functions with adaptive bandwidths and multi-scale interactions
        rbf_term = 0
        for i in range(self.dim):
            rbf_sum = 0
            for j in range(self.dim):
                if i != j:
                    distance = np.abs(x_norm[i] - x_norm[j])
                    # Multi-scale dynamic bandwidth with dimensionality dependency
                    bandwidth = 0.05 + 0.3 * (1 / (1 + distance)) * (1 + 0.2 * np.sin(3 * np.pi * x_norm[i]))
                    rbf_sum += np.exp(-distance**2 / bandwidth) * np.sin(9 * np.pi * (x_norm[i] + x_norm[j])) * np.cos(4 * np.pi * (x_norm[i] - x_norm[j]))
            rbf_term += rbf_sum
            
        # Spectral polynomial chaos terms with higher-order and non-linear combinations
        poly_term = 0
        for i in range(self.dim):
            # Use high-order polynomials with alternating signs and trigonometric mixing
            poly_term += ((x_norm[i]**9 - 5*x_norm[i]**7 + 10*x_norm[i]**5 - 10*x_norm[i]**3 + 5*x_norm[i]) * 
                         np.cos(4*np.pi*x_norm[i]) + 
                         (x_norm[i]**8 - 4*x_norm[i]**6 + 6*x_norm[i]**4 - 4*x_norm[i]**2 + 1) * 
                         np.sin(4*np.pi*x_norm[i]))
            
        # Enhanced cross-dimensional coupling with chaotic phase interactions and non-linear mixing
        coupling_term = 0
        for i in range(0, self.dim - 3, 4):
            if i + 3 < self.dim:
                phase = np.sin(np.pi * x_norm[i]) * np.cos(np.pi * x_norm[i+1]) * np.sin(np.pi * x_norm[i+2]) * np.cos(np.pi * x_norm[i+3])
                # Non-linear mixing of coordinates
                coupling_term += phase * (x_norm[i]**3 + x_norm[i+1]**3 + x_norm[i+2]**3 + x_norm[i+3]**3)
        
        # Combined result with dynamic weighting and additional noise-like perturbations
        weight1, weight2, weight3, weight4 = 0.25, 0.3, 0.2, 0.25
        result = weight1 * chaotic_term + weight2 * rbf_term + weight3 * poly_term + weight4 * coupling_term
        
        # Add a global scaling and offset with additional complexity through polynomial terms
        result += 0.15 * np.sum(x_norm ** 2) + 0.05 * np.sum(x_norm ** 4)
        
        return result