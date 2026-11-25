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
            # Multi-scale sine transformations with slightly altered frequency modulation
            freq1 = 3.2 * (1 + 0.42 * np.sin(4.1 * x_norm[i]))
            freq2 = 6.3 * (1 + 0.31 * np.cos(7.2 * x_norm[i]))
            freq3 = 12.1 * (1 + 0.21 * np.sin(9.3 * x_norm[i]))
            
            term1 = np.sin(freq1 * np.pi * x_norm[i])
            term2 = np.sin(freq2 * np.pi * x_norm[i])
            term3 = np.sin(freq3 * np.pi * x_norm[i])
            
            # Slightly modified fractal basin scaling with altered weights
            scaled_term = (term1 + 0.52 * term2 + 0.26 * term3) / (1.0 + 0.11 * np.abs(x_norm[i])**2)
            
            # Modified cross-dimensional coupling with adjusted chaotic interactions
            coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    # Slightly altered phase coupling
                    phase_diff = x_norm[i] - x_norm[j]
                    phase_sum = x_norm[i] + x_norm[j]
                    
                    coupling += np.sin(3.1 * np.pi * phase_diff) * \
                               np.cos(4.2 * np.pi * phase_sum) * \
                               np.exp(-0.32 * (phase_diff**2)) * \
                               (1 + 0.31 * np.sin(5.1 * x_norm[i]))
            
            result += scaled_term + 0.51 * coupling
        
        # Spectral complexity enhancement with modified harmonic modulations
        spectral_mod = 0.0
        for i in range(self.dim):
            # Modified frequency bands with altered amplitudes and phases
            spectral_mod += (0.98 * np.sin(15.2 * x_norm[i]) * np.cos(20.1 * x_norm[i]) + 
                           0.41 * np.sin(30.3 * x_norm[i]) * np.cos(40.2 * x_norm[i]) +
                           0.21 * np.sin(60.1 * x_norm[i]) * np.cos(80.3 * x_norm[i]))
        
        # Slightly adjusted noise-like perturbations with modified fractal characteristics
        noise = 0.0
        for i in range(self.dim):
            # Modified fractal noise with altered scales
            noise += (0.21 * np.sin(70.1 * x_norm[i]) + 
                     0.11 * np.cos(100.2 * x_norm[i]) + 
                     0.085 * np.sin(140.1 * x_norm[i]) + 
                     0.065 * np.cos(180.2 * x_norm[i]))
        
        # Modified chaotic modulation based on global landscape characteristics
        global_mod = 0.0
        for i in range(self.dim):
            global_mod += 0.99 * np.sin(30.1 * x_norm[i]) * np.cos(35.2 * x_norm[i]) * \
                         np.exp(-0.16 * np.sum(x_norm**2))
        
        return result + 0.41 * spectral_mod + 0.21 * noise + 0.26 * global_mod