import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced fractal construction with chaotic coupling
        result = 0.0
        for i in range(self.dim):
            # Multi-scale sine transformations with dynamic frequency modulation
            freq1 = 2 * (1 + 0.4 * np.sin(3 * x_norm[i] + 0.5 * np.cos(x_norm[i])))
            freq2 = 4 * (1 + 0.3 * np.cos(5 * x_norm[i] + 0.3 * np.sin(x_norm[i])))
            freq3 = 8 * (1 + 0.2 * np.sin(7 * x_norm[i] + 0.4 * np.cos(x_norm[i])))
            
            term1 = np.sin(freq1 * np.pi * x_norm[i])
            term2 = np.sin(freq2 * np.pi * x_norm[i])
            term3 = np.sin(freq3 * np.pi * x_norm[i])
            
            # Fractal basin scaling with adaptive weights and dynamic exponent
            scaled_term = (term1 + 0.4 * term2 + 0.16 * term3) / (1.0 + 0.08 * np.abs(x_norm[i])**1.8)
            
            # Enhanced cross-dimensional coupling with chaotic interactions and dynamic phase
            coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    # Dynamic phase coupling with time-varying parameters
                    phase_diff = x_norm[i] - x_norm[j]
                    phase_sum = x_norm[i] + x_norm[j]
                    
                    coupling += np.sin(2 * np.pi * phase_diff + 0.3 * np.cos(x_norm[i])) * \
                               np.cos(3 * np.pi * phase_sum + 0.2 * np.sin(x_norm[j])) * \
                               np.exp(-0.3 * (phase_diff**2)) * \
                               (1 + 0.3 * np.sin(4 * x_norm[i]) * np.cos(2 * x_norm[j]))
            
            result += scaled_term + 0.5 * coupling
        
        # Spectral complexity enhancement with multiple harmonic modulations and frequency mixing
        spectral_mod = 0.0
        for i in range(self.dim):
            # Multiple frequency bands with varying amplitudes, phases, and dynamic modulation
            spectral_mod += (np.sin(15 * x_norm[i]) * np.cos(20 * x_norm[i]) + 
                           0.4 * np.sin(30 * x_norm[i]) * np.cos(40 * x_norm[i]) +
                           0.2 * np.sin(60 * x_norm[i]) * np.cos(80 * x_norm[i]) +
                           0.1 * np.sin(120 * x_norm[i]) * np.cos(160 * x_norm[i]))
        
        # Increased noise-like perturbations with fractal characteristics and dynamic scaling
        noise = 0.0
        for i in range(self.dim):
            # Fractal noise with multiple scales and dynamic amplitude modulation
            noise += (0.2 * np.sin(70 * x_norm[i]) + 
                     0.12 * np.cos(100 * x_norm[i]) + 
                     0.08 * np.sin(140 * x_norm[i]) + 
                     0.06 * np.cos(180 * x_norm[i]) +
                     0.04 * np.sin(210 * x_norm[i]))
        
        # Add chaotic modulation based on global landscape characteristics with enhanced dynamic coupling
        global_mod = 0.0
        for i in range(self.dim):
            global_mod += np.sin(30 * x_norm[i]) * np.cos(35 * x_norm[i]) * \
                         np.exp(-0.15 * np.sum(x_norm**2)) * \
                         (1 + 0.25 * np.sin(5 * x_norm[i]))
        
        # Add novel interaction terms between dimensions for higher complexity
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_term += np.sin(8 * (x_norm[i] - x_norm[j])) * \
                                  np.cos(6 * (x_norm[i] + x_norm[j])) * \
                                  np.exp(-0.2 * ((x_norm[i] - x_norm[j])**2))
        
        return result + 0.4 * spectral_mod + 0.2 * noise + 0.25 * global_mod + 0.1 * interaction_term