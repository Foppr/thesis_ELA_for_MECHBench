import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced quaternion-inspired symmetry breaking with chaotic phase modulation
        basin_term = 0.0
        for i in range(self.dim):
            phase = np.sin(i * 1.7 + np.cos(i * 0.4)) * np.cos(i * 0.9 + np.sin(i * 0.6))
            steepness = 2.0 + 1.2 * np.sin(i * 0.8 + np.cos(i * 0.3))
            basin_term += (np.tanh(steepness * x[i])**4) * np.exp(-0.2 * x[i]**2) * (1.0 + 0.3 * np.sin(4.0 * x[i] + phase))
        
        # Multi-frequency gradient flow with chaotic coupling and memory effects
        grad_term = 0.0
        for i in range(self.dim):
            freq_mod = 1.5 + 0.4 * np.cos(i * 0.6 + np.sin(i * 0.2))
            memory_factor = 1.0 + 0.1 * np.sin(x[i] * 0.5)
            grad_term += (0.5 * x[i]**3 + 0.3 * x[i]**5 + 0.1 * np.exp(0.8 * x[i])) * np.cos(freq_mod * x[i]) * np.sin(0.5 * x[i]) * memory_factor
        
        # Fractal-like energy interactions with adaptive coupling coefficients and multi-scale distance metrics
        energy_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.001)
                coupling = 1.0 + 0.2 * np.sin(x[i] + x[j]) * np.cos(3.0 * x[i]) * np.sin(2.0 * x[j])
                energy_term += (np.log(dist + 2.0) / (dist**1.5 + 1.0)) * coupling * np.sin(3.0 * x[i]) * np.cos(2.0 * x[j])
        
        # Chaotic saddle-point modulation with higher-order sinusoidal perturbations and non-linear feedback
        chaotic_term = 0.0
        for i in range(self.dim):
            feedback = np.sin(x[i] + np.sin(2.0 * x[i]) + 0.5 * np.sin(4.0 * x[i]))
            chaotic_term += (np.sin(x[i]) * np.cos(x[i]) * 
                           np.exp(-0.15 * np.abs(x[i])) * 
                           np.sin(4.0 * x[i] + feedback))
        
        # Global scaling with fractal-like polynomial and exponential components plus adaptive basin boundaries
        global_term = 0.0
        for i in range(self.dim):
            boundary_mod = 1.0 + 0.2 * np.sin(x[i] * 0.7)
            global_term += (0.6 * x[i]**4 * np.exp(-0.15 * x[i]**2) + 
                          0.3 * x[i] * np.sin(0.7 * x[i]) + 
                          0.2 * np.log(np.abs(x[i]) + 3.0) + 
                          0.1 * np.sin(6.0 * x[i]) * boundary_mod)
        
        # Add multi-scale harmonic coupling terms with adaptive frequencies and phase shifts
        harmonic_term = 0.0
        for i in range(self.dim):
            freq1 = 2.5 + 0.3 * np.sin(i * 0.5)
            freq2 = 3.5 + 0.2 * np.cos(i * 0.7)
            harmonic_term += (0.4 * np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) + 
                            0.3 * np.sin(2.0 * freq1 * x[i]) * np.cos(2.0 * freq2 * x[i]) + 
                            0.2 * np.sin(3.0 * freq1 * x[i]))
        
        # Add fractal basin boundary irregularities and extreme conditioning
        irregularity_term = 0.0
        for i in range(self.dim):
            irregularity_term += (0.15 * np.sin(7.0 * x[i]) * np.cos(5.0 * x[i]) * 
                               np.exp(-0.3 * x[i]**2) * (1.0 + 0.4 * np.sin(8.0 * x[i])))
        
        # Return the combined function value with enhanced regularization and extreme conditioning
        return basin_term + grad_term + energy_term + chaotic_term + global_term + harmonic_term + irregularity_term + 0.02 * np.sum(x**2) + 0.01 * np.sum(np.abs(x)**3)