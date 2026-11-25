import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        
        # Asymmetric elliptic components with multi-scale sinusoidal modulations
        for i in range(self.dim):
            # Base elliptic term with asymmetric scaling and exponential potential
            base_ellipse = x_norm[i]**2 + 0.5 * np.sin(3 * x_norm[i])**2
            
            # Multi-scale sinusoidal modulation with varying frequencies
            mod1 = 0.3 * np.sin(10 * x_norm[i])
            mod2 = 0.2 * np.cos(15 * x_norm[i])
            mod3 = 0.1 * np.sin(25 * x_norm[i])
            
            # Asymmetric elliptic structure with exponential weighting
            ellipse_term = base_ellipse * (1.0 + 0.3 * np.exp(-5 * np.abs(x_norm[i])))
            
            # Combined interference pattern
            interference = mod1 + mod2 + mod3
            
            result += ellipse_term + interference
            
        # Enhanced cross-dimensional coupling with fractal basin interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal-like coupling with exponential decay and phase modulation
                diff = x_norm[i] - x_norm[j]
                sum_val = x_norm[i] + x_norm[j]
                
                # Asymmetric weighting based on difference magnitude
                weight_pos = 0.6 * (1 + np.tanh(2 * diff))  # Bias towards positive differences
                weight_neg = 0.4 * (1 - np.tanh(2 * diff))  # Bias towards negative differences
                
                # Fractal basin interaction with exponential potentials
                coupling_factor = np.exp(-0.5 * (diff**2 + sum_val**2))
                
                # Multi-scale sinusoidal coupling
                coupling += (weight_pos * np.sin(12 * diff) * np.cos(8 * sum_val) * 
                           coupling_factor + 
                           weight_neg * np.cos(10 * diff) * np.sin(6 * sum_val) * 
                           coupling_factor)
        
        # Add enhanced coupling term with scaling factor
        result += 0.4 * coupling
        
        # Increased spectral complexity with novel exponential potentials
        spectral_complexity = 0.0
        for i in range(self.dim):
            # Exponential potential with multi-scale sinusoidal components
            exp_potential = np.exp(2 * np.abs(x_norm[i])) - 1
            
            # Multi-frequency sinusoidal modulation
            freq_mod = 0.4 * np.sin(30 * x_norm[i]) + 0.3 * np.cos(40 * x_norm[i])
            
            spectral_complexity += exp_potential * freq_mod
        
        # Add spectral complexity term
        result += 0.2 * spectral_complexity
        
        # Dynamic weighting scheme with adaptive dimensionality scaling
        dim_scaling = 1.0 + 0.3 * np.log(1.0 + self.dim)
        
        # Global scaling based on distance from origin with fractal characteristics
        dist_from_origin = np.sum(x_norm**2)
        global_scale = 1.0 + 0.4 * np.exp(-0.05 * dist_from_origin) * np.sin(5 * dist_from_origin)
        
        return result * dim_scaling * global_scale
