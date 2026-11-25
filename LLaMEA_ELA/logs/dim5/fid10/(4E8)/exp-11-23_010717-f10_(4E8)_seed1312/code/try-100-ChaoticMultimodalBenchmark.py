import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced nested fractal basin terms with higher-order polynomial scaling and chaotic frequency modulation
        basin = 0.6 * np.sum(np.exp(4.0 * np.abs(x)) * np.sin(3.0 * x)**2) + \
                0.4 * np.sum(np.log(np.abs(x) + 1.0) * np.cos(5.0 * x)**3) + \
                0.3 * np.sum(np.tanh(x)**5) + \
                0.2 * np.sum(np.sinh(x)**2)
        
        # Complex hybrid wave interactions with frequency modulation, amplitude scaling, and chaotic phase shifts
        wave_terms = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.6 * np.sin(0.6 * i)
            wave_terms += (9.0 * np.sin(freq_mod * 4.0 * x[i]) * np.cos(freq_mod * 3.0 * x[i]) + 
                          7.0 * np.sin(freq_mod * 5.0 * x[i])**2 * np.cos(freq_mod * 4.0 * x[i]) + 
                          5.0 * np.sin(freq_mod * 6.0 * x[i]) * np.cos(freq_mod * 5.0 * x[i])**2 + 
                          3.0 * np.sin(freq_mod * 7.0 * x[i])**3 + 
                          2.5 * np.cos(freq_mod * 8.0 * x[i])**3 + 
                          1.8 * np.sin(freq_mod * 9.0 * x[i]) * np.cos(freq_mod * 6.0 * x[i]))
        
        # Enhanced cross-dimensional coupling with chaotic phase shifts, nested interactions, and fractal-like correlation
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_shift = 0.4 * np.sin(0.3 * (i + j))
                cross_terms += (1.0 * np.sin(4.0 * x[i] + phase_shift) * np.cos(5.0 * x[j] + phase_shift) + 
                               0.8 * np.cos(6.0 * x[i] + phase_shift) * np.sin(4.5 * x[j] + phase_shift) + 
                               0.6 * np.sin(3.5 * x[i] + phase_shift)**2 * np.sin(5.5 * x[j] + phase_shift)**2 + 
                               0.5 * np.cos(7.0 * x[i] + phase_shift) * np.cos(6.0 * x[j] + phase_shift) + 
                               0.3 * np.sin(8.0 * x[i] + phase_shift)**3 * np.cos(7.0 * x[j] + phase_shift)**2)
        
        # Novel hybrid noise component with chaotic amplitude modulation, fractal-like correlation, and higher-order harmonics
        noise = 0.0
        for i in range(self.dim):
            noise += (0.3 * np.sin(20.0 * x[i]) * np.cos(15.0 * x[i]) + 
                     0.25 * np.cos(25.0 * x[i]) * np.sin(10.0 * x[i]) + 
                     0.2 * np.sin(30.0 * x[i])**3 * np.cos(20.0 * x[i])**2 + 
                     0.1 * np.tanh(30.0 * x[i]) * np.sin(10.0 * x[i]) + 
                     0.15 * np.exp(-np.abs(x[i])) * np.cos(20.0 * x[i]) + 
                     0.08 * np.sin(25.0 * x[i])**4 * np.cos(18.0 * x[i])**3)
        
        # Global scaling with chaotic frequency modulation, nested fractal structure, and higher-order polynomial terms
        scaling_factor = 1.0 + 0.5 * np.sum(np.sin(x)**6) + 0.3 * np.sum(np.cos(x)**4) + 0.2 * np.sum(np.tanh(x)**3)
        
        # Add a nested chaotic penalty term for enhanced complexity and irregular fitness surfaces
        penalty = 0.15 * np.sum(np.sin(25.0 * x)**7 + np.cos(20.0 * x)**5)
        
        return scaling_factor * (basin + wave_terms + cross_terms + noise) + penalty