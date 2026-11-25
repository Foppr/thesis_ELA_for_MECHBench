import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sine-wave interactions with dynamic frequencies
        chaotic_term = 0
        for i in range(self.dim):
            freq = 2 * np.pi * (1 + 0.5 * np.sin(x_norm[i]))
            chaotic_term += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
            
        # Adaptive radial basis functions with dynamic widths and centers
        rbf_term = 0
        for i in range(self.dim):
            rbf_sum = 0
            for j in range(self.dim):
                if i != j:
                    distance = np.abs(x_norm[i] - x_norm[j])
                    width = 0.1 + 0.4 * np.sin(i * 0.5 + j * 0.3)
                    rbf_sum += np.exp(-distance**2 / (2 * width**2)) * np.sin(3 * np.pi * (x_norm[i] + x_norm[j]))
            rbf_term += rbf_sum
            
        # Quantum-inspired phase couplings with complex amplitudes
        quat_term = 0
        for i in range(0, self.dim - 3, 4):
            if i + 3 < self.dim:
                phase1 = np.exp(1j * (x_norm[i] + x_norm[i+1]))
                phase2 = np.exp(1j * (x_norm[i+2] + x_norm[i+3]))
                quat_term += np.real(phase1 * np.conj(phase2)) * \
                            np.exp(-0.3 * (x_norm[i]**2 + x_norm[i+1]**2 + x_norm[i+2]**2 + x_norm[i+3]**2))
        
        # Increased polynomial chaos terms with fractional powers and cross-terms
        poly_term = 0
        for i in range(self.dim):
            poly_term += (x_norm[i]**6 - 4*x_norm[i]**4 + 4*x_norm[i]**2) * np.cos(3*np.pi*x_norm[i]) + \
                        0.5 * x_norm[i] * np.sin(4*np.pi*x_norm[i])
            
        # Cross-dimensional coupling with chaotic phase interactions
        coupling_term = 0
        for i in range(0, self.dim - 2, 3):
            if i + 2 < self.dim:
                coupling_term += np.sin(np.pi * x_norm[i]) * np.cos(np.pi * x_norm[i+1]) * \
                               np.sin(np.pi * x_norm[i+2]) * \
                               (x_norm[i]**2 + x_norm[i+1]**2 + x_norm[i+2]**2)
        
        # Combined result with dynamic weighting and noise injection
        weight1, weight2, weight3, weight4 = 0.2, 0.25, 0.3, 0.25
        result = weight1 * chaotic_term + weight2 * rbf_term + weight3 * poly_term + weight4 * coupling_term
        
        # Add a global scaling and offset to ensure positive fitness values with dynamic noise
        noise = 0.02 * np.sum(np.sin(x_norm * 10))
        result += 0.1 * np.sum(x_norm ** 2) + noise
        
        return result