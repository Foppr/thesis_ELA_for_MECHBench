import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        # Enhanced fractal hierarchy with recursive scaling
        for i in range(self.dim):
            # Multi-scale frequency modulation with chaotic components
            scale_factor = 2 ** (i % 5)
            freq = scale_factor * (1 + 0.7 * np.sin(x_norm[i] * np.pi * (i + 1)))
            
            # Multiple sinusoidal components with varying powers and amplitudes
            term1 = np.sin(freq * x_norm[i])
            term2 = np.cos(freq * x_norm[i]**1.5)
            term3 = np.sin(freq * x_norm[i]**2.5)
            term4 = np.cos(freq * x_norm[i]**3.5)
            
            # Exponentially decaying correlation with chaotic decay factor
            corr_decay = np.exp(-0.15 * i * (1 + 0.2 * np.sin(i * np.pi / self.dim)))
            
            # Recursive fractal component with self-similarity across dimensions
            fractal_term = np.sin(x_norm[i] * 2**(i % 3)) * np.cos(x_norm[i] * 3**(i % 4)) * np.sin(x_norm[i] * 5**(i % 2))
            
            # Additional chaotic modulation based on dimension index
            chaos_mod = 1.0 + 0.3 * np.sin(i * np.pi / self.dim) * np.cos(i * np.pi / (self.dim + 1))
            
            # Combine all components with scale-dependent weights and chaos
            weight = 1.0 / (1.0 + i * 0.15)
            result += weight * corr_decay * term1 * term2 * term3 * term4 * fractal_term * chaos_mod
            
        # Enhanced global structure with multi-scale coupling
        global_structure = 0.0
        for i in range(self.dim):
            # Multi-scale sinusoidal modulation with varying frequencies and phases
            freq_global = (i + 1) * (1 + 0.4 * np.sin(i * np.pi / self.dim)) * (1 + 0.3 * np.cos(i * np.pi / (self.dim * 2)))
            global_structure += np.sin(freq_global * x_norm[i]) * np.cos(freq_global * x_norm[i]**1.8) * np.sin(freq_global * x_norm[i]**2.2)
            
        # Add cross-dimensional coupling with recursive structure
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.5 * (1 + np.sin((i + j) * np.pi / self.dim))
                cross_coupling += coupling_strength * np.sin(x_norm[i] * x_norm[j] * (i + j + 1))
                
        # Combine local, global, and cross-dimensional components with dynamic weighting
        alpha = 0.7 + 0.3 * np.sin(self.dim * 0.25)
        beta = 0.8 - 0.4 * np.cos(self.dim * 0.1)
        gamma = 0.2 + 0.1 * np.sin(self.dim * 0.3)
        
        return alpha * result + beta * global_structure + gamma * cross_coupling