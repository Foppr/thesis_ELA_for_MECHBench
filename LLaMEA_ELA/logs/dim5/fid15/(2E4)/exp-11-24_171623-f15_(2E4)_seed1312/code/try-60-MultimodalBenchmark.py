import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic sine-wave interactions with multiple frequency modulations
        chaotic_term = 0
        for i in range(self.dim):
            freq_mod1 = 1 + 0.3 * np.sin(2 * np.pi * x_norm[i])
            freq_mod2 = 1 + 0.4 * np.cos(3 * np.pi * x_norm[i])
            freq_mod3 = 1 + 0.2 * np.sin(5 * np.pi * x_norm[i])
            chaotic_term += (np.sin(freq_mod1 * np.pi * x_norm[i]) * 
                           np.cos(freq_mod2 * 2 * np.pi * x_norm[i]) * 
                           np.sin(freq_mod3 * 3 * np.pi * x_norm[i]))
        
        # Adaptive radial basis functions with dynamic bandwidths and multi-scale interactions
        rbf_term = 0
        for i in range(self.dim):
            rbf_sum = 0
            for j in range(self.dim):
                if i != j:
                    distance = np.abs(x_norm[i] - x_norm[j])
                    # Dynamic bandwidth based on dimensionality and distance with additional scaling
                    bandwidth = 0.05 + 0.3 * (1 / (1 + distance)) * (1 + 0.1 * np.sin(4 * np.pi * x_norm[i]))
                    rbf_sum += np.exp(-distance**2 / bandwidth) * np.sin(5 * np.pi * (x_norm[i] + x_norm[j])) * np.cos(2 * np.pi * x_norm[i])
            rbf_term += rbf_sum
            
        # Spectral polynomial chaos terms with varying degrees and enhanced nonlinearity
        poly_term = 0
        for i in range(self.dim):
            # Use higher-order polynomials with alternating signs and additional trigonometric components
            poly_term += ((x_norm[i]**9 - 5*x_norm[i]**7 + 10*x_norm[i]**5 - 10*x_norm[i]**3 + 5*x_norm[i]) * 
                         np.cos(4*np.pi*x_norm[i]) + 
                         (x_norm[i]**8 - 4*x_norm[i]**6 + 6*x_norm[i]**4 - 4*x_norm[i]**2 + 1) * 
                         np.sin(4*np.pi*x_norm[i]))
            
        # Novel cross-dimensional coupling with chaotic phase interactions and fractal-like patterns
        coupling_term = 0
        for i in range(0, self.dim - 3, 4):
            if i + 3 < self.dim:
                phase = np.sin(np.pi * x_norm[i]) * np.cos(np.pi * x_norm[i+1]) * np.sin(np.pi * x_norm[i+2]) * np.cos(np.pi * x_norm[i+3])
                # Fractal-like scaling factor
                fractal_scale = 1 + 0.2 * np.sin(7 * np.pi * x_norm[i]) * np.cos(7 * np.pi * x_norm[i+1])
                coupling_term += phase * (x_norm[i]**2 + x_norm[i+1]**2 + x_norm[i+2]**2 + x_norm[i+3]**2) * fractal_scale
        
        # Add a novel noise component to increase deception
        noise_term = 0
        for i in range(self.dim):
            noise_term += np.sin(10 * np.pi * x_norm[i]) * np.cos(8 * np.pi * x_norm[i])
        
        # Combined result with dynamic weighting and additional complexity
        weight1, weight2, weight3, weight4, weight5 = 0.15, 0.30, 0.20, 0.25, 0.10
        result = weight1 * chaotic_term + weight2 * rbf_term + weight3 * poly_term + weight4 * coupling_term + weight5 * noise_term
        
        # Add a global scaling and offset to ensure positive fitness values with enhanced complexity
        result += 0.15 * np.sum(x_norm ** 2) + 0.05 * np.sum(np.abs(x_norm))
        
        return result