import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters
        self.chaos_params = np.random.rand(dim) * 0.1 + 0.05
        self.osc_freqs = np.random.rand(dim) * 2.0 + 1.0
        self.osc_amps = np.random.rand(dim) * 3.0 + 1.0
        self.saddle_weights = np.random.randn(dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic gradient component with time-varying modulation
        chaotic_grad = 0.0
        for i in range(self.dim):
            chaotic_grad += (self.chaos_params[i] * 
                           np.sin(x[i] * self.osc_freqs[i]) * 
                           np.cos(x[i] * self.osc_amps[i]) * 
                           np.exp(-0.1 * x[i]**2))
        
        # Harmonic oscillation with dynamic frequency modulation
        harmonic_osc = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.5 * np.sin(np.sum(x) * 0.3)
            harmonic_osc += self.osc_amps[i] * np.sin(freq_mod * x[i] * self.osc_freqs[i])
            
        # Saddle-point dominance with weighted linear combinations
        saddle_point = 0.0
        for i in range(self.dim):
            saddle_point += self.saddle_weights[i] * (x[i]**2 - x[i]**4)
            
        # Cross-dimensional coupling with exponential decay
        cross_coupling = 0.0
        for i in range(self.dim - 1):
            cross_coupling += np.exp(-0.5 * (x[i]**2 + x[i+1]**2)) * np.sin(x[i] * x[i+1])
            
        # Time-varying chaotic skewness component
        time_skew = 0.0
        for i in range(self.dim):
            time_skew += np.sin(x[i] * 0.5 + np.sum(x) * 0.1) * np.cos(x[i] * 0.3)
            
        # Combine all components with adaptive scaling
        result = (chaotic_grad + harmonic_osc + saddle_point + cross_coupling + time_skew)
        
        return result