import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        # Fractal hierarchy with multiple scales
        for i in range(self.dim):
            # Scale-dependent frequency modulation with enhanced complexity
            scale_factor = 2 ** (i % 5)
            freq = scale_factor * (1 + 0.7 * np.sin(x_norm[i] * np.pi / 2))
            
            # Sinusoidal components with varying amplitudes and phases
            term1 = np.sin(freq * x_norm[i])
            term2 = np.cos(freq * x_norm[i]**2)
            term3 = np.sin(freq * x_norm[i]**3)
            term4 = np.cos(freq * x_norm[i]**4)
            
            # Enhanced exponentially decaying correlation structure
            corr_decay = np.exp(-0.15 * i)
            
            # Self-similar fractal component with modified scaling
            fractal_term = np.sin(x_norm[i] * 2**(i//2)) * np.cos(x_norm[i] * 3**(i//3))
            
            # Combine all components with scale-dependent weights
            weight = 1.0 / (1.0 + i * 0.15)
            result += weight * corr_decay * term1 * term2 * term3 * term4 * fractal_term
            
        # Add multi-scale global structure with improved conditioning
        global_structure = 0.0
        for i in range(self.dim):
            # Multi-scale sinusoidal modulation with dynamic frequency
            freq_global = (i + 1) * (1 + 0.4 * np.sin(i * np.pi / self.dim + np.sqrt(i)))
            global_structure += np.sin(freq_global * x_norm[i]) * np.cos(freq_global * x_norm[i]**2)
            
        # Combine local and global components with adaptive weighting
        alpha = 0.5 + 0.3 * np.sin(self.dim * 0.15)
        beta = 1.0 - alpha
        
        return alpha * result + beta * global_structure