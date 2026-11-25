import numpy as np

class PolynomialChaosBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion components with varying degrees
        result = 0.0
        for i in range(self.dim):
            result += 1.5 * (x[i]**4 - 2*x[i]**2 + 1) + 0.8 * (x[i]**6 - 3*x[i]**4 + 3*x[i]**2 - 1)
        
        # Radial basis functions with adaptive widths and heights
        for i in range(self.dim):
            result += 2.0 * np.exp(-0.5 * (x[i] - 1.5)**2) + 1.2 * np.exp(-0.3 * (x[i] + 2.0)**2) + 0.9 * np.exp(-0.7 * (x[i] - 3.0)**2)
        
        # Sine-cosine coupling with adaptive frequencies
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                freq_i = 2 + 0.5 * np.sin(x[i])
                freq_j = 2 + 0.5 * np.cos(x[j])
                coupling = 1.8 * np.exp(-0.1 * (x[i] - x[j])**2)
                result += coupling * np.sin(freq_i * x[i]) * np.cos(freq_j * x[j])
        
        # Adaptive conditioning with polynomial weights
        condition_factor = 1.0
        for i in range(self.dim):
            condition_factor *= (1 + 0.4 * x[i]**2 * np.sin(5 * x[i]))
        result += 1.2 * condition_factor
        
        # Cross-dimensional interactions with chaotic modulation
        chaos_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaos_interaction += np.sin(3 * (x[i] + x[j])) * np.cos(4 * (x[i] - x[j]))
        result += 0.7 * chaos_interaction
        
        # Asymmetric penalty terms near boundaries
        for i in range(self.dim):
            if x[i] < 0:
                result += 1.5 * np.exp(-0.2 * (x[i] + 5.0)**2) * (1 + 0.3 * np.sin(10 * x[i]))
            else:
                result += 1.8 * np.exp(-0.3 * (x[i] - 5.0)**2) * (1 + 0.2 * np.cos(8 * x[i]))
        
        # High-order polynomial terms with sine modulation
        for i in range(self.dim):
            result += 0.6 * x[i]**5 * np.sin(7 * x[i])
        
        # Fractal-like structure using recursive sine components
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += np.sin(15 * x[i]) * np.cos(12 * x[i])
        result += 1.1 * fractal_term**2
        
        # Multi-scale harmonic coupling with exponential weights
        harmonic_sum = 0.0
        for i in range(self.dim):
            harmonic_sum += np.sin(4 * x[i]) * np.cos(3 * x[i]) * np.exp(-0.1 * x[i]**2)
        result += 0.9 * harmonic_sum**2
        
        # Noise injection with chaotic sine-wave components
        noise = 0.0
        for i in range(self.dim):
            noise += 0.3 * np.sin(25 * x[i]) * np.cos(22 * x[i])
        result += noise
        
        # Chaotic tent map dynamics
        tent_map = 0.0
        for i in range(self.dim):
            if x[i] < 0.5:
                tent_map += 2.0 * x[i]
            else:
                tent_map += 2.0 * (1.0 - x[i])
        result += 0.8 * tent_map**3
        
        # Time-varying radial basis functions
        time_factor = 0.0
        for i in range(self.dim):
            time_factor += 1.5 * np.exp(-0.4 * (x[i] - np.sin(0.1 * i))**2) * np.cos(0.3 * i)
        result += 0.6 * time_factor
        
        # Multi-scale fractal interference patterns
        interference = 0.0
        for i in range(self.dim):
            interference += np.sin(20 * x[i]) * np.cos(18 * x[i]) * np.sin(16 * x[i])
        result += 1.3 * interference**2
        
        # Enhanced chaotic coupling with exponential modulation
        chaotic_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic_coupling += np.exp(-0.5 * (x[i] - x[j])**2) * np.sin(10 * (x[i] + x[j]))
        result += 0.9 * chaotic_coupling
        
        # Complex boundary penalty with multi-modal components
        boundary_penalty = 0.0
        for i in range(self.dim):
            boundary_penalty += 2.0 * np.exp(-0.1 * (x[i] - 5.0)**2) * np.sin(15 * x[i]) + \
                              1.8 * np.exp(-0.1 * (x[i] + 5.0)**2) * np.cos(12 * x[i])
        result += 0.7 * boundary_penalty
        
        # Multi-scale polynomial chaos with coupling
        multi_scale = 0.0
        for i in range(self.dim):
            multi_scale += 0.5 * x[i]**8 * np.sin(9 * x[i]) + 0.3 * x[i]**7 * np.cos(8 * x[i])
        result += 1.4 * multi_scale
        
        # Hyper-chaotic sine-cosine interactions
        hyper_chaos = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                hyper_chaos += np.sin(5 * x[i]) * np.cos(6 * x[j]) * np.sin(7 * (x[i] - x[j]))
        result += 1.2 * hyper_chaos
        
        return result