import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic gradient component with logistic map dynamics
        chaotic_grad = 0
        r = 3.9  # Logistic map parameter for chaos
        for i in range(self.dim):
            # Logistic map state update
            log_state = (r * x[i] * (1.0 - x[i])) if i == 0 else (r * log_state * (1.0 - log_state))
            phase_shift = np.sin(log_state * np.pi)
            chaotic_grad += phase_shift * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
        
        # Embedded saddle point structure with hyperbolic tangents
        saddle_points = 0
        for i in range(self.dim):
            saddle_term = np.tanh(x[i] * (1.0 + 0.3 * np.sin(0.5 * x[i]))) * \
                         np.cos(0.7 * x[i]**2) * \
                         np.exp(-0.1 * x[i]**2)
            saddle_points += saddle_term
        
        # Dynamic noise injection with time-varying amplitude
        noise = 0
        for i in range(self.dim):
            noise_amp = 0.5 + 0.3 * np.sin(0.2 * i + self.dim * 0.1)
            noise += noise_amp * np.random.normal(0, 0.1) * np.cos(x[i])
        
        # Spectral bandpass filtering with multi-frequency modulation
        spectral_filter = 0
        for i in range(self.dim):
            freqs = [1.0, 2.0, 3.0, 4.0]
            filtered = sum(np.sin(freq * x[i]) * np.exp(-0.05 * (freq - 2.5)**2) 
                          for freq in freqs)
            spectral_filter += filtered
        
        # Cross-dimensional coupling with exponential decay
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling = np.exp(-0.1 * (x[i] - x[j])**2) * \
                          np.sin(2.0 * (x[i] + x[j])) * \
                          np.cos(1.5 * (x[i] - x[j]))
                cross_coupling += coupling
        
        # Variable conditioning based on dimensionality
        condition_number = 1.0 + 0.4 * np.sin(0.3 * self.dim) + 0.2 * np.cos(0.2 * self.dim)
        
        # Combine all components with optimized weights
        return condition_number * (0.35 * chaotic_grad + 0.25 * saddle_points + 
                                  0.15 * noise + 0.2 * spectral_filter + 0.05 * cross_coupling)