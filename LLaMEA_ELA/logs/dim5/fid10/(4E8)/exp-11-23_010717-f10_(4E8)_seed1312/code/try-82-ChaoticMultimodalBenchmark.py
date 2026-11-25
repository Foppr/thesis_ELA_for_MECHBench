import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Nested fractal basin terms with exponential scaling and chaotic frequency modulation
        basin = 0.5 * np.sum(np.exp(3.0 * np.abs(x)) * np.sin(2.0 * x)**2) + \
                0.3 * np.sum(np.log(np.abs(x) + 1.0) * np.cos(4.0 * x)**3) + \
                0.2 * np.sum(np.tanh(x)**4)
        
        # Complex hybrid wave interactions with frequency modulation and amplitude scaling
        wave_terms = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.5 * np.sin(0.5 * i)
            wave_terms += (7.0 * np.sin(freq_mod * 3.5 * x[i]) * np.cos(freq_mod * 2.5 * x[i]) + 
                          5.0 * np.sin(freq_mod * 4.0 * x[i])**2 * np.cos(freq_mod * 3.0 * x[i]) + 
                          3.0 * np.sin(freq_mod * 5.0 * x[i]) * np.cos(freq_mod * 4.0 * x[i])**2 + 
                          2.0 * np.sin(freq_mod * 6.0 * x[i])**3 + 
                          1.5 * np.cos(freq_mod * 7.0 * x[i])**3)
        
        # Enhanced cross-dimensional coupling with chaotic phase shifts and nested interactions
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_shift = 0.3 * np.sin(0.2 * (i + j))
                cross_terms += (0.8 * np.sin(3.0 * x[i] + phase_shift) * np.cos(4.0 * x[j] + phase_shift) + 
                               0.6 * np.cos(5.0 * x[i] + phase_shift) * np.sin(3.5 * x[j] + phase_shift) + 
                               0.4 * np.sin(2.5 * x[i] + phase_shift)**2 * np.sin(4.5 * x[j] + phase_shift)**2 + 
                               0.3 * np.cos(6.0 * x[i] + phase_shift) * np.cos(5.0 * x[j] + phase_shift))
        
        # Novel hybrid noise component with chaotic amplitude modulation and fractal-like correlation
        noise = 0.0
        for i in range(self.dim):
            noise += (0.2 * np.sin(15.0 * x[i]) * np.cos(12.0 * x[i]) + 
                     0.15 * np.cos(18.0 * x[i]) * np.sin(9.0 * x[i]) + 
                     0.1 * np.sin(20.0 * x[i])**3 * np.cos(14.0 * x[i])**2 + 
                     0.05 * np.tanh(25.0 * x[i]) * np.sin(8.0 * x[i]) + 
                     0.08 * np.exp(-np.abs(x[i])) * np.cos(16.0 * x[i]))
        
        # Global scaling with chaotic frequency modulation and nested fractal structure
        scaling_factor = 1.0 + 0.4 * np.sum(np.sin(x)**5) + 0.2 * np.sum(np.cos(x)**3)
        
        # Add a nested chaotic penalty term for enhanced complexity
        penalty = 0.1 * np.sum(np.sin(20.0 * x)**6 + np.cos(15.0 * x)**4)
        
        return scaling_factor * (basin + wave_terms + cross_terms + noise) + penalty