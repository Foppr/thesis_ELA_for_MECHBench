import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum harmonic oscillator components with modified chaotic phase coupling
        quantum_harmonic = 0
        for i in range(self.dim):
            freq = 1.2 + 0.4 * np.sin(0.35 * x[i]) + 0.15 * np.cos(0.45 * x[i])
            amplitude = 1.1 + 0.25 * np.sin(0.55 * x[i])
            phase_shift = 0.9 * np.sin(0.75 * x[i] + 0.35 * np.sin(0.95 * x[i]))
            quantum_harmonic += amplitude * (x[i]**2) * np.cos(freq * x[i] + phase_shift)
        
        # Dynamic coupling terms with chaotic coefficient modulation
        dynamic_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic coupling coefficient using logistic map
                coeff = 0.45 + 0.35 * np.sin(0.25 * (x[i] + x[j])) * np.cos(0.15 * x[i] * x[j])
                dynamic_coupling += coeff * np.sin(x[i] * x[j]) * np.exp(-0.12 * (x[i] - x[j])**2)
        
        # Fractal-based radial basis functions with adaptive centers and widths
        fractal_rbf = 0
        for i in range(self.dim):
            center = 2.1 * np.sin(0.45 * x[i]) + 0.55 * np.cos(0.65 * x[i]) + 0.12 * np.sin(0.85 * x[i])
            width = 0.55 + 0.35 * np.sin(0.35 * x[i]) + 0.25 * np.cos(0.55 * x[i])
            fractal_rbf += np.exp(-0.5 * ((x[i] - center) / width)**2) * np.cos(0.75 * x[i]) * np.sin(0.45 * x[i])
        
        # Adaptive saddle-point structure with dynamic curvature and spectral filtering
        adaptive_saddle = 0
        for i in range(self.dim):
            a = 1.1 + 0.35 * np.sin(0.35 * x[i]) + 0.12 * np.cos(0.65 * x[i])
            b = 0.85 + 0.22 * np.cos(0.55 * x[i]) + 0.12 * np.sin(0.75 * x[i])
            # Spectral filtering for enhanced complexity
            spectral_filter = 1.05 + 0.35 * np.sin(0.45 * x[i] * x[i])
            adaptive_saddle += (x[i]**2 - a) * (x[i]**2 - b) * np.sin(0.65 * x[i]) * spectral_filter
        
        # Chaotic sine-cosine interactions with fractal modulation and quantum interference
        chaotic_interaction = 0
        for i in range(self.dim):
            mod_freq = 1.4 + 0.55 * np.sin(0.45 * x[i]) + 0.22 * np.cos(0.65 * x[i])
            mod_amp = 0.85 + 0.22 * np.cos(0.35 * x[i]) + 0.12 * np.sin(0.55 * x[i])
            # Quantum interference term
            interference = 0.32 * np.sin(0.85 * x[i]) * np.cos(0.95 * x[i])
            chaotic_interaction += mod_amp * np.sin(mod_freq * x[i]) * np.cos(mod_freq * x[i]) + interference
        
        # Enhanced global conditioning with dimension scaling and fractal modulation
        condition_factor = 1.05 + 0.22 * np.sin(0.55 * self.dim) + 0.12 * np.cos(0.35 * self.dim) + 0.06 * np.sin(0.75 * self.dim)
        
        # Additional complexity through mixed conditioning and basin structures
        mixed_conditioning = 1.05 + 0.12 * np.sin(0.25 * np.sum(x**2)) + 0.06 * np.cos(0.35 * np.sum(np.abs(x)))
        
        # Introduce new component for improved fitness: hyper-chaotic gradient modulation
        hyperchaos = 0
        for i in range(self.dim):
            # Hyper-chaotic modulation using multiple sine/cosine combinations
            mod1 = 0.55 * np.sin(0.35 * x[i] + 0.22 * np.sin(0.75 * x[i]))
            mod2 = 0.32 * np.cos(0.45 * x[i] + 0.12 * np.cos(0.65 * x[i]))
            mod3 = 0.22 * np.sin(0.55 * x[i] + 0.12 * np.sin(0.85 * x[i]))
            hyperchaos += (mod1 + mod2 + mod3) * np.exp(-0.12 * x[i]**2)
        
        # Combine all components with optimized weights and enhanced complexity
        return condition_factor * mixed_conditioning * (0.22 * quantum_harmonic + 0.27 * dynamic_coupling + 
                                  0.22 * fractal_rbf + 0.16 * adaptive_saddle + 0.19 * chaotic_interaction + 0.03 * hyperchaos)