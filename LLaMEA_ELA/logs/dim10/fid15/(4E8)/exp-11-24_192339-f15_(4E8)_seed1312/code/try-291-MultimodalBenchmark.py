import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced quantum harmonic oscillator with phase modulation
        quantum_harmonic = 0
        for i in range(self.dim):
            freq = 1.0 + 0.6 * np.sin(0.3 * x[i]) + 0.3 * np.cos(0.4 * x[i])
            amplitude = 1.0 + 0.4 * np.sin(0.5 * x[i]) + 0.2 * np.cos(0.6 * x[i])
            phase_shift = 0.5 * np.sin(0.7 * x[i]) * np.cos(0.8 * x[i])
            quantum_harmonic += amplitude * (x[i]**2) * np.cos(freq * x[i] + phase_shift)
        
        # Dynamic coupling with adaptive coefficients and time-varying interactions
        dynamic_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = 0.6 + 0.4 * np.sin(0.2 * (x[i] + x[j])) * np.cos(0.3 * (x[i] - x[j]))
                coupling_interaction = np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
                dynamic_coupling += coeff * coupling_interaction
        
        # Fractal-based radial basis functions with adaptive centers, widths, and spectral filtering
        fractal_rbf = 0
        for i in range(self.dim):
            center = 2.0 * np.sin(0.4 * x[i]) + 0.5 * np.cos(0.6 * x[i]) + 0.3 * np.sin(0.8 * x[i])
            width = 0.5 + 0.4 * np.sin(0.3 * x[i]) + 0.2 * np.cos(0.5 * x[i])
            spectral_filter = 1.0 + 0.3 * np.sin(0.4 * x[i])**2
            fractal_rbf += spectral_filter * np.exp(-0.5 * ((x[i] - center) / width)**2) * np.cos(0.7 * x[i])
        
        # Adaptive saddle-point structure with enhanced curvature and chaotic modulation
        adaptive_saddle = 0
        for i in range(self.dim):
            a = 1.0 + 0.5 * np.sin(0.3 * x[i]) + 0.2 * np.cos(0.4 * x[i])
            b = 0.8 + 0.3 * np.cos(0.5 * x[i]) + 0.1 * np.sin(0.6 * x[i])
            chaotic_mod = 1.0 + 0.2 * np.sin(0.8 * x[i])**2
            adaptive_saddle += chaotic_mod * (x[i]**2 - a) * (x[i]**2 - b) * np.sin(0.6 * x[i])
        
        # Chaotic sine-cosine interactions with multi-scale fractal modulation and spectral filtering
        chaotic_interaction = 0
        for i in range(self.dim):
            mod_freq = 1.5 + 0.6 * np.sin(0.4 * x[i]) + 0.3 * np.cos(0.5 * x[i])
            mod_amp = 0.8 + 0.3 * np.cos(0.3 * x[i]) + 0.2 * np.sin(0.4 * x[i])
            spectral_component = 1.0 + 0.2 * np.sin(0.6 * x[i])**2
            chaotic_interaction += spectral_component * mod_amp * np.sin(mod_freq * x[i]) * np.cos(mod_freq * x[i])
        
        # Enhanced global conditioning with multi-scale dimension scaling and chaotic modulation
        condition_factor = 1.0 + 0.3 * np.sin(0.5 * self.dim) + 0.2 * np.cos(0.3 * self.dim) + 0.1 * np.sin(0.7 * self.dim)
        
        # Combine all components with optimized weights and enhanced nonlinearity
        return condition_factor * (0.25 * quantum_harmonic + 0.3 * dynamic_coupling + 
                                  0.25 * fractal_rbf + 0.18 * adaptive_saddle + 0.22 * chaotic_interaction)