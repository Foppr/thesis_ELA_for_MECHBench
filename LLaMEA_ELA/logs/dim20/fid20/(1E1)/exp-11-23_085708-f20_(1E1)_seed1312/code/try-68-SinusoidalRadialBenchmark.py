import numpy as np

class SinusoidalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Fractal-like radial component with chaotic sine/cosine combinations
        r = np.sqrt(np.sum(x_scaled**2))
        radial_term = r * (1 + 0.8 * np.sin(5 * r) + 0.3 * np.cos(7 * r) + 
                          0.1 * np.sin(11 * r) + 0.05 * np.cos(13 * r) + 
                          0.02 * np.sin(17 * r) * np.cos(19 * r))
        
        # Chaotic cross-terms with fractal-like interaction patterns
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Quantum-inspired interaction with phase modulation
                phase = (x[i] * x[j] * np.pi / 4) + (i * j * np.pi / 8)
                cross_term += (np.sin(phase) * np.cos(phase) + 
                              0.5 * np.sin(2 * phase) * np.cos(3 * phase) + 
                              0.3 * np.sin(5 * x[i]) * np.cos(7 * x[j]) +
                              0.2 * np.cos(4 * x[i] + 3 * x[j])) * (i + j + 1)
                
        # Adaptive gradient modulation with quantum-like tunneling effects
        grad_mod = 1.0
        for i in range(self.dim):
            # Multi-scale quantum tunneling components
            grad_mod *= (1 + 0.5 * np.sin(x[i] * 0.3) + 
                        0.2 * np.cos(x[i] * 0.7) + 
                        0.3 * np.sin(x[i] * 1.1) +
                        0.1 * np.cos(x[i] * 1.5) +
                        0.05 * np.sin(x[i] * 2.3) * np.cos(x[i] * 3.7))
            
        # Fractal multimodal component with exponential growth in peaks
        multi_modal = 0.0
        for i in range(self.dim):
            # Exponentially increasing frequency components
            multi_modal += (np.sin(3 * x[i]) + 
                           0.7 * np.sin(6 * x[i]) + 
                           0.4 * np.cos(4 * x[i]) + 
                           0.2 * np.sin(9 * x[i]) +
                           0.1 * np.cos(8 * x[i]) +
                           0.05 * np.sin(12 * x[i]) * np.cos(15 * x[i]))
            
        # Fractal interaction terms with exponentially increasing complexity
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    # Fractal-like interaction with multi-scale frequencies
                    interaction_term += (0.1 * np.sin(x[i] * x[j] * 0.5) + 
                                       0.05 * np.cos(x[i] * x[j] * 2) +
                                       0.03 * np.sin(x[i] * 0.7 * x[j] * 0.3) +
                                       0.02 * np.cos(x[i] * 1.1 * x[j] * 0.9)) * (i + j + 1)
        
        # Quantum-inspired periodic modulation based on coordinate sum
        coord_sum = np.sum(x)
        periodic_mod = 1.0 + 0.3 * np.sin(0.5 * coord_sum) * np.cos(0.3 * coord_sum) + \
                      0.1 * np.sin(0.8 * coord_sum) * np.cos(0.6 * coord_sum) + \
                      0.05 * np.sin(coord_sum * 1.2) * np.cos(coord_sum * 1.4)
        
        # Add fractal-like dimensionality scaling factor
        dim_scaling = 1.0 + 0.1 * (self.dim - 1) * np.sin(r * 2)
        
        # Combine all terms with fractal scaling
        return radial_term + cross_term + grad_mod * multi_modal + interaction_term + periodic_mod + dim_scaling + 5.0