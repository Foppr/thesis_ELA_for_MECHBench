import numpy as np

class SinusoidalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Fractional dimension scaling with chaotic sinusoidal modulation
        r = np.sqrt(np.sum(x_scaled**2))
        fractional_r = r ** (1.3 + 0.7 * np.sin(3 * r))
        radial_term = fractional_r * (1 + 0.8 * np.sin(5 * r) + 0.3 * np.cos(7 * r) + 0.1 * np.sin(11 * r))
        
        # Chaotic cross-terms with fractional exponents and quantum phase interference
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = np.sin(x[i] * x[j] * 2 + 0.5 * np.cos(x[i] + x[j]))
                cross_term += (np.sin(x[i] * x[j] * 2) + 
                              0.5 * np.cos(x[i] * x[j] * 3) + 
                              0.3 * np.sin(x[i] * 0.7) * np.cos(x[j] * 0.9) +
                              0.2 * np.cos(x[i] * x[j] * 4) +
                              0.1 * phase) * (i + j + 1) * (1 + 0.2 * np.sin(2 * r))
                
        # Adaptive gradient modulation with fractional powers and chaotic components
        grad_mod = 1.0
        for i in range(self.dim):
            grad_mod *= (1 + 0.5 * np.sin(x[i] * 0.3) + 
                        0.2 * np.cos(x[i] * 0.7) + 
                        0.3 * np.sin(x[i] * 1.1) +
                        0.1 * np.cos(x[i] * 1.5) +
                        0.05 * np.sin(4 * x[i]) * np.cos(3 * x[i]))
            
        # Multimodal component with fractal-like frequency scaling and quantum tunneling effects
        multi_modal = 0.0
        for i in range(self.dim):
            freq_factor = 1 + 0.5 * np.sin(0.1 * i)
            multi_modal += (np.sin(3 * x[i] * freq_factor) + 
                           0.7 * np.sin(6 * x[i] * freq_factor) + 
                           0.4 * np.cos(4 * x[i] * freq_factor) + 
                           0.2 * np.sin(9 * x[i] * freq_factor) +
                           0.1 * np.cos(8 * x[i] * freq_factor) +
                           0.05 * np.sin(x[i] * 13) * np.cos(x[i] * 7))
            
        # Additional interaction terms with fractional dimension coupling and chaotic modulation
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    frac_exp = 0.5 + 0.3 * np.sin(0.2 * (i + j))
                    interaction_term += 0.1 * (np.sin(x[i] * x[j] * 0.5) + 
                                             0.05 * np.cos(x[i] * x[j] * 2)) * (i + j + 1) * (1 + 0.1 * np.sin(r))
        
        # Quantum-like phase interference with fractal dimension scaling
        coord_sum = np.sum(x)
        quantum_phase = np.sin(0.5 * coord_sum + 0.3 * np.cos(coord_sum * 2)) * np.cos(0.3 * coord_sum + 0.4 * np.sin(coord_sum * 3))
        periodic_mod = 1.0 + 0.3 * quantum_phase
        
        # Fractal dimension scaling factor
        fractal_factor = 1.0 + 0.2 * np.sin(2 * r) * np.cos(3 * r)
        
        # Combine all terms with different weights and chaotic modulation
        return radial_term + cross_term + grad_mod * multi_modal + interaction_term + periodic_mod * fractal_factor + 5.0