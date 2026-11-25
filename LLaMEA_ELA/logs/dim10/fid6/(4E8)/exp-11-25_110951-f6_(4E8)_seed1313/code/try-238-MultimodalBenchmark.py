import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced fractal construction with chaotic coupling and exponential potentials
        result = 0.0
        for i in range(self.dim):
            # Multi-scale sine transformations with chaotic frequency modulation and exponential scaling
            freq1 = 3 * (1 + 0.4 * np.sin(4 * x_norm[i]))
            freq2 = 6 * (1 + 0.3 * np.cos(7 * x_norm[i]))
            freq3 = 12 * (1 + 0.2 * np.sin(9 * x_norm[i]))
            
            term1 = np.sin(freq1 * np.pi * x_norm[i])
            term2 = np.sin(freq2 * np.pi * x_norm[i])
            term3 = np.sin(freq3 * np.pi * x_norm[i])
            
            # Asymmetric elliptic scaling with exponential weights
            exp_weight = np.exp(-0.5 * np.abs(x_norm[i]))
            asym_scale = 1.0 + 0.3 * np.sin(2 * np.pi * x_norm[i])**3
            
            scaled_term = (term1 + 0.5 * term2 + 0.25 * term3) * exp_weight * asym_scale / (1.0 + 0.1 * np.abs(x_norm[i])**2)
            
            # Enhanced cross-dimensional coupling with multi-scale interactions
            coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    # Multi-scale phase coupling with asymmetric elliptic structures
                    phase_diff = x_norm[i] - x_norm[j]
                    phase_sum = x_norm[i] + x_norm[j]
                    
                    # Asymmetric elliptic interaction terms
                    elliptic_factor = 1.0 + 0.2 * np.sin(3 * x_norm[i])**2
                    
                    coupling += (np.sin(3 * np.pi * phase_diff) * 
                                np.cos(4 * np.pi * phase_sum) * 
                                np.exp(-0.3 * (phase_diff**2)) * 
                                (1 + 0.3 * np.sin(5 * x_norm[i])) *
                                elliptic_factor)
            
            result += scaled_term + 0.5 * coupling
        
        # Spectral complexity enhancement with multiple harmonic modulations and exponential potentials
        spectral_mod = 0.0
        for i in range(self.dim):
            # Multiple frequency bands with varying amplitudes, phases, and exponential scaling
            exp_scaling = np.exp(-0.2 * np.abs(x_norm[i]))
            spectral_mod += (np.sin(15 * x_norm[i]) * np.cos(20 * x_norm[i]) * exp_scaling + 
                           0.4 * np.sin(30 * x_norm[i]) * np.cos(40 * x_norm[i]) * exp_scaling +
                           0.2 * np.sin(60 * x_norm[i]) * np.cos(80 * x_norm[i]) * exp_scaling)
        
        # Increased noise-like perturbations with fractal characteristics and asymmetric elliptic structures
        noise = 0.0
        for i in range(self.dim):
            # Fractal noise with multiple scales and asymmetric elliptic modulations
            elliptic_mod = 1.0 + 0.25 * np.sin(3 * x_norm[i])**2
            noise += (0.2 * np.sin(70 * x_norm[i]) * elliptic_mod + 
                     0.1 * np.cos(100 * x_norm[i]) * elliptic_mod + 
                     0.08 * np.sin(140 * x_norm[i]) * elliptic_mod + 
                     0.06 * np.cos(180 * x_norm[i]) * elliptic_mod)
        
        # Add chaotic modulation based on global landscape characteristics with asymmetric elliptic structures
        global_mod = 0.0
        for i in range(self.dim):
            # Asymmetric elliptic global modulation
            elliptic_global = 1.0 + 0.3 * np.sin(2 * x_norm[i])**2
            global_mod += np.sin(30 * x_norm[i]) * np.cos(35 * x_norm[i]) * \
                         np.exp(-0.15 * np.sum(x_norm**2)) * elliptic_global
        
        # Add dynamic weighting scheme based on dimensionality
        dim_weight = 1.0 + 0.1 * (self.dim - 1) / (self.dim + 1)
        
        return result * dim_weight + 0.4 * spectral_mod + 0.2 * noise + 0.25 * global_mod