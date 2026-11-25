import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced nested fractal basin terms with higher-order polynomial scaling and chaotic frequency modulation
        basin = 0.6 * np.sum(np.abs(x)**5 * np.sin(2.0 * x)**3) + \
                0.4 * np.sum(np.log(np.abs(x) + 1.0) * np.cos(5.0 * x)**4) + \
                0.3 * np.sum(np.tanh(x)**5) + \
                0.2 * np.sum(x**6 * np.exp(-0.5 * np.abs(x)))
        
        # Complex hybrid wave interactions with frequency modulation, amplitude scaling, and higher-order harmonics
        wave_terms = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.7 * np.sin(0.3 * i + 0.5 * np.cos(0.2 * i))
            wave_terms += (9.0 * np.sin(freq_mod * 4.0 * x[i]) * np.cos(freq_mod * 3.0 * x[i])**2 + 
                          7.0 * np.sin(freq_mod * 5.0 * x[i])**3 * np.cos(freq_mod * 4.0 * x[i]) + 
                          5.0 * np.sin(freq_mod * 6.0 * x[i]) * np.cos(freq_mod * 5.0 * x[i])**3 + 
                          3.0 * np.sin(freq_mod * 7.0 * x[i])**4 + 
                          2.0 * np.cos(freq_mod * 8.0 * x[i])**4 + 
                          1.0 * np.sin(freq_mod * 9.0 * x[i]) * np.cos(freq_mod * 7.0 * x[i]))
        
        # Enhanced cross-dimensional coupling with chaotic phase shifts, nested interactions, and polynomial coupling
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_shift = 0.4 * np.sin(0.3 * (i + j) + 0.2 * np.cos(0.1 * (i - j)))
                cross_terms += (1.0 * np.sin(4.0 * x[i] + phase_shift) * np.cos(5.0 * x[j] + phase_shift)**2 + 
                               0.8 * np.cos(6.0 * x[i] + phase_shift) * np.sin(5.0 * x[j] + phase_shift)**2 + 
                               0.6 * np.sin(3.5 * x[i] + phase_shift)**3 * np.sin(6.5 * x[j] + phase_shift)**3 + 
                               0.4 * np.cos(7.0 * x[i] + phase_shift) * np.cos(6.0 * x[j] + phase_shift) + 
                               0.3 * np.sin(8.0 * x[i] + phase_shift)**2 * np.cos(7.5 * x[j] + phase_shift)**2)
        
        # Novel hybrid noise component with chaotic amplitude modulation, fractal-like correlation, and higher-order terms
        noise = 0.0
        for i in range(self.dim):
            noise += (0.3 * np.sin(20.0 * x[i]) * np.cos(15.0 * x[i]) + 
                     0.25 * np.cos(25.0 * x[i]) * np.sin(10.0 * x[i]) + 
                     0.2 * np.sin(30.0 * x[i])**4 * np.cos(20.0 * x[i])**3 + 
                     0.1 * np.tanh(35.0 * x[i]) * np.sin(10.0 * x[i]) + 
                     0.15 * np.exp(-np.abs(x[i])) * np.cos(25.0 * x[i]) + 
                     0.08 * np.sin(40.0 * x[i])**5)
        
        # Global scaling with chaotic frequency modulation, nested fractal structure, and polynomial enhancement
        scaling_factor = 1.0 + 0.5 * np.sum(np.sin(x)**6) + 0.3 * np.sum(np.cos(x)**4) + 0.2 * np.sum(x**8)
        
        # Add a nested chaotic penalty term for enhanced complexity with higher-order polynomial
        penalty = 0.15 * np.sum(np.sin(25.0 * x)**7 + np.cos(20.0 * x)**5)
        
        return scaling_factor * (basin + wave_terms + cross_terms + noise) + penalty