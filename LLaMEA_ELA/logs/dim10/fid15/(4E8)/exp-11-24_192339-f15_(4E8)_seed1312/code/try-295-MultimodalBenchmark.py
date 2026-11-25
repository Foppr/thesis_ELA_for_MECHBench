import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum harmonic oscillator components with chaotic phase coupling
        quantum_harmonic = 0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(0.3 * x[i]) + 0.2 * np.cos(0.4 * x[i])
            amplitude = 1.0 + 0.3 * np.sin(0.5 * x[i])
            phase_shift = 0.8 * np.sin(0.7 * x[i] + 0.3 * np.sin(0.9 * x[i]))
            quantum_harmonic += amplitude * (x[i]**2) * np.cos(freq * x[i] + phase_shift)
        
        # Dynamic coupling terms with chaotic coefficient modulation
        dynamic_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic coupling coefficient using logistic map
                coeff = 0.5 + 0.3 * np.sin(0.2 * (x[i] + x[j])) * np.cos(0.1 * x[i] * x[j])
                dynamic_coupling += coeff * np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Fractal-based radial basis functions with adaptive centers and widths
        fractal_rbf = 0
        for i in range(self.dim):
            center = 2.0 * np.sin(0.4 * x[i]) + 0.5 * np.cos(0.6 * x[i]) + 0.1 * np.sin(0.8 * x[i])
            width = 0.5 + 0.3 * np.sin(0.3 * x[i]) + 0.2 * np.cos(0.5 * x[i])
            fractal_rbf += np.exp(-0.5 * ((x[i] - center) / width)**2) * np.cos(0.7 * x[i]) * np.sin(0.4 * x[i])
        
        # Adaptive saddle-point structure with dynamic curvature and spectral filtering
        adaptive_saddle = 0
        for i in range(self.dim):
            a = 1.0 + 0.4 * np.sin(0.3 * x[i]) + 0.1 * np.cos(0.6 * x[i])
            b = 0.8 + 0.2 * np.cos(0.5 * x[i]) + 0.1 * np.sin(0.7 * x[i])
            # Spectral filtering for enhanced complexity
            spectral_filter = 1.0 + 0.3 * np.sin(0.4 * x[i] * x[i])
            adaptive_saddle += (x[i]**2 - a) * (x[i]**2 - b) * np.sin(0.6 * x[i]) * spectral_filter
        
        # Chaotic sine-cosine interactions with fractal modulation and quantum interference
        chaotic_interaction = 0
        for i in range(self.dim):
            mod_freq = 1.5 + 0.5 * np.sin(0.4 * x[i]) + 0.2 * np.cos(0.6 * x[i])
            mod_amp = 0.8 + 0.2 * np.cos(0.3 * x[i]) + 0.1 * np.sin(0.5 * x[i])
            # Quantum interference term
            interference = 0.3 * np.sin(0.8 * x[i]) * np.cos(0.9 * x[i])
            chaotic_interaction += mod_amp * np.sin(mod_freq * x[i]) * np.cos(mod_freq * x[i]) + interference
        
        # Enhanced global conditioning with dimension scaling and fractal modulation
        condition_factor = 1.0 + 0.2 * np.sin(0.5 * self.dim) + 0.1 * np.cos(0.3 * self.dim) + 0.05 * np.sin(0.7 * self.dim)
        
        # Additional complexity through mixed conditioning and basin structures
        mixed_conditioning = 1.0 + 0.1 * np.sin(0.2 * np.sum(x**2)) + 0.05 * np.cos(0.3 * np.sum(np.abs(x)))
        
        # Combine all components with optimized weights and enhanced complexity
        return condition_factor * mixed_conditioning * (0.2 * quantum_harmonic + 0.25 * dynamic_coupling + 
                                  0.2 * fractal_rbf + 0.15 * adaptive_saddle + 0.2 * chaotic_interaction)