import numpy as np

class SinusoidalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Fractional dimensional scaling with chaotic interaction
        r = np.sqrt(np.sum(x_scaled**2))
        fractional_r = r ** (1.3 + 0.2 * np.sin(10 * r))
        radial_term = fractional_r * (1 + 0.8 * np.sin(5 * r) + 0.3 * np.cos(7 * r) + 0.1 * np.sin(11 * r))
        
        # Chaotic cross-terms with quantum phase interactions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = np.sin(x[i] * x[j] * 2 + 0.5 * np.cos(x[i] + x[j]))
                cross_term += (np.sin(x[i] * x[j] * 2) + 
                              0.5 * np.cos(x[i] * x[j] * 3) + 
                              0.3 * np.sin(x[i] * 0.7) * np.cos(x[j] * 0.9) +
                              0.2 * np.cos(x[i] * x[j] * 4) +
                              0.1 * phase) * (i + j + 1) * (1 + 0.3 * np.sin(5 * (i + j)))
                
        # Quantum-inspired gradient modulation with complex phase
        grad_mod = 1.0
        for i in range(self.dim):
            phase = np.exp(1j * x[i] * 0.3)
            grad_mod *= (1 + 0.5 * np.sin(x[i] * 0.3) + 
                        0.2 * np.cos(x[i] * 0.7) + 
                        0.3 * np.sin(x[i] * 1.1) +
                        0.1 * np.cos(x[i] * 1.5) +
                        0.1 * np.real(phase))
            
        # Multi-modal component with exponential peak density
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += (np.sin(3 * x[i]) + 
                           0.7 * np.sin(6 * x[i]) + 
                           0.4 * np.cos(4 * x[i]) + 
                           0.2 * np.sin(9 * x[i]) +
                           0.1 * np.cos(8 * x[i]) +
                           0.05 * np.sin(15 * x[i]) * np.cos(12 * x[i]))
            
        # Additional chaotic interaction terms with fractal-like behavior
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction_term += 0.1 * (np.sin(x[i] * x[j] * 0.5) + 
                                             0.05 * np.cos(x[i] * x[j] * 2) +
                                             0.03 * np.sin(x[i] * x[j] * 7)) * (i + j + 1) * (1 + 0.2 * np.sin(3 * i))
        
        # Quantum phase modulation based on coordinate sum
        coord_sum = np.sum(x)
        quantum_mod = 1.0 + 0.3 * np.sin(0.5 * coord_sum + 0.1 * np.cos(coord_sum)) * np.cos(0.3 * coord_sum + 0.2 * np.sin(coord_sum))
        
        # Add chaotic perturbation term
        chaos_perturb = 0.0
        for i in range(self.dim):
            chaos_perturb += 0.05 * np.sin(20 * x[i] + 3 * np.cos(5 * x[i]))
            
        # Combine all terms with different weights and chaotic scaling
        return (radial_term + cross_term + grad_mod * multi_modal + 
                interaction_term + quantum_mod + chaos_perturb + 5.0)