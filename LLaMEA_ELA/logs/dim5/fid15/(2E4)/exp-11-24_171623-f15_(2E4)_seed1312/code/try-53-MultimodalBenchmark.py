import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sine-wave interactions with frequency modulation
        chaotic_term = 0
        for i in range(self.dim):
            freq_mod = 1 + 0.5 * np.sin(3 * np.pi * x_norm[i])
            chaotic_term += np.sin(freq_mod * np.pi * x_norm[i]) * np.cos(freq_mod * 2 * np.pi * x_norm[i])
        
        # Adaptive radial basis functions with dynamic bandwidths
        rbf_term = 0
        for i in range(self.dim):
            rbf_sum = 0
            for j in range(self.dim):
                if i != j:
                    distance = np.abs(x_norm[i] - x_norm[j])
                    # Dynamic bandwidth based on dimensionality and distance
                    bandwidth = 0.1 + 0.2 * (1 / (1 + distance))
                    rbf_sum += np.exp(-distance**2 / bandwidth) * np.sin(7 * np.pi * (x_norm[i] + x_norm[j]))
            rbf_term += rbf_sum
            
        # Spectral polynomial chaos terms with varying degrees
        poly_term = 0
        for i in range(self.dim):
            # Use higher-order polynomials with alternating signs
            poly_term += ((x_norm[i]**7 - 4*x_norm[i]**5 + 6*x_norm[i]**3 - 4*x_norm[i]) * 
                         np.cos(3*np.pi*x_norm[i]) + 
                         (x_norm[i]**6 - 3*x_norm[i]**4 + 3*x_norm[i]**2 - 1) * 
                         np.sin(3*np.pi*x_norm[i]))
            
        # Cross-dimensional coupling with chaotic phase interactions
        coupling_term = 0
        for i in range(0, self.dim - 2, 3):
            if i + 2 < self.dim:
                phase = np.sin(np.pi * x_norm[i]) * np.cos(np.pi * x_norm[i+1]) * np.sin(np.pi * x_norm[i+2])
                coupling_term += phase * (x_norm[i]**2 + x_norm[i+1]**2 + x_norm[i+2]**2)
        
        # Combined result with dynamic weighting
        weight1, weight2, weight3, weight4 = 0.2, 0.35, 0.25, 0.2
        result = weight1 * chaotic_term + weight2 * rbf_term + weight3 * poly_term + weight4 * coupling_term
        
        # Add a global scaling and offset to ensure positive fitness values
        result += 0.1 * np.sum(x_norm ** 2)
        
        return result