import numpy as np

class ChaoticSineWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Chaotic sine-wave components with varying frequencies and phase shifts
        chaotic_terms = 0
        for i in range(self.dim):
            chaotic_terms += np.sin(2 * np.pi * x[i] * (1 + 0.1 * np.sin(5 * x[i]))) * \
                           np.cos(3 * np.pi * x[i] * (1 + 0.05 * np.cos(7 * x[i]))) + \
                           np.sin(4 * np.pi * x[i] * (1 + 0.2 * np.tan(3 * x[i]))) * \
                           np.cos(2 * np.pi * x[i] * (1 + 0.15 * np.sin(9 * x[i])))
        
        # Adaptive dimensional coupling with dynamic weights based on input values
        adaptive_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.5 + 0.5 * np.tanh(x[i] * x[j])
                adaptive_coupling += weight * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * \
                                   (1 + 0.3 * np.sin(0.7 * (x[i]**2 + x[j]**2)))
                
        # Fractal-like penalty regions with self-similar structure at different scales
        fractal_penalty = 0
        for i in range(self.dim):
            dist_from_origin = np.sqrt(np.sum(x**2))
            fractal_penalty += 10 * (1 - np.exp(-0.1 * (dist_from_origin - 2)**2)) * \
                             np.sin(5 * np.pi * dist_from_origin)**3 + \
                             8 * np.exp(-0.2 * (dist_from_origin - 4)**2) * \
                             np.cos(6 * np.pi * dist_from_origin)**4 + \
                             6 * np.sin(0.5 * dist_from_origin)**5
        
        # Combine all components with a global scaling factor
        return 0.8 * (chaotic_terms + adaptive_coupling + fractal_penalty)