import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        
        # Fractal-like basin structure with dynamic scaling
        for i in range(self.dim):
            # Base quadratic term with fractal-like modification
            base = x_norm[i]**2
            
            # Fractal-like harmonic modulation
            fractal_mod = np.sin(3 * np.pi * x_norm[i]) * np.cos(7 * np.pi * x_norm[i])
            
            # Dynamic phase shift based on dimension index
            phase_shift = np.sin(0.5 * np.pi * i / self.dim)
            
            # Multi-scale harmonic component
            harmonic = (0.5 * np.sin(12 * x_norm[i] + phase_shift) + 
                       0.3 * np.cos(20 * x_norm[i] + phase_shift) + 
                       0.2 * np.sin(30 * x_norm[i] + phase_shift))
            
            result += base + 0.5 * fractal_mod + harmonic
            
        # Multi-scale cross-dimensional coupling with chaotic interaction
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic coupling with multi-scale frequencies
                diff = x_norm[i] - x_norm[j]
                sum_val = x_norm[i] + x_norm[j]
                
                # Multi-scale interaction terms
                coupling_term = (np.sin(15 * diff) * np.cos(10 * sum_val) * 
                               np.exp(-0.5 * (diff**2 + sum_val**2)) +
                               0.3 * np.sin(25 * diff) * np.cos(18 * sum_val) * 
                               np.exp(-0.3 * (diff**2 + sum_val**2)))
                
                # Dimensional weighting based on position
                weight = 1.0 / (1.0 + np.exp(-5 * (i - j)))
                
                coupling += weight * coupling_term
        
        # Add coupling with scaling factor
        result += 0.4 * coupling
        
        # Saddle point enhancement through asymmetric harmonic components
        saddle = 0.0
        for i in range(self.dim):
            # Asymmetric harmonic that creates saddle points
            asym_harmonic = (0.4 * np.sin(8 * x_norm[i]) * 
                           np.cos(12 * x_norm[i]) * 
                           np.exp(-0.1 * x_norm[i]**2))
            saddle += asym_harmonic
            
        # Add saddle point component
        result += 0.3 * saddle
        
        # Global scaling with fractal-like complexity
        distance = np.sum(x_norm**2)
        global_scale = 1.0 + 0.8 * np.sin(5 * np.sqrt(distance)) * np.exp(-0.05 * distance)
        
        # Add noise-like component for increased complexity
        noise = 0.0
        for i in range(self.dim):
            noise += (0.2 * np.sin(50 * x_norm[i]) + 
                     0.1 * np.cos(70 * x_norm[i]) + 
                     0.15 * np.sin(90 * x_norm[i]))
        
        return result * global_scale + 0.1 * noise