import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Nested chaotic oscillator components with quantum entanglement
        nested_oscillator = 0
        for i in range(self.dim):
            freq1 = 1.3 + 0.35 * np.sin(0.4 * x[i]) + 0.2 * np.cos(0.5 * x[i])
            freq2 = 0.8 + 0.25 * np.cos(0.6 * x[i]) + 0.15 * np.sin(0.7 * x[i])
            amplitude1 = 1.2 + 0.3 * np.sin(0.5 * x[i])
            amplitude2 = 0.9 + 0.2 * np.cos(0.4 * x[i])
            # Quantum entanglement term
            entangle = 0.15 * np.sin(0.8 * x[i]) * np.cos(0.9 * x[i])
            nested_oscillator += (amplitude1 * np.sin(freq1 * x[i]) + 
                                amplitude2 * np.cos(freq2 * x[i])) * entangle
        
        # Dynamic quantum coupling with fractal phase modulation
        quantum_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal phase coefficient
                phase_coeff = 0.5 + 0.3 * np.sin(0.3 * x[i]) * np.cos(0.4 * x[j])
                coupling_strength = 0.7 + 0.25 * np.cos(0.2 * (x[i] + x[j]))
                quantum_coupling += coupling_strength * np.sin(phase_coeff * x[i] * x[j]) * np.exp(-0.15 * (x[i] - x[j])**2)
        
        # Fractal basin structure with multiple fractal dimensions
        fractal_basin = 0
        for i in range(self.dim):
            center1 = 2.3 * np.sin(0.4 * x[i]) + 0.6 * np.cos(0.5 * x[i])
            center2 = 1.7 * np.cos(0.3 * x[i]) + 0.4 * np.sin(0.6 * x[i])
            width1 = 0.6 + 0.3 * np.sin(0.4 * x[i])
            width2 = 0.5 + 0.25 * np.cos(0.5 * x[i])
            fractal_basin += (np.exp(-0.5 * ((x[i] - center1) / width1)**2) * 
                            np.exp(-0.5 * ((x[i] - center2) / width2)**2) * 
                            np.cos(0.6 * x[i]))
        
        # Adaptive multi-saddle structure with spectral filtering
        multi_saddle = 0
        for i in range(self.dim):
            a1 = 1.2 + 0.3 * np.sin(0.4 * x[i])
            a2 = 0.9 + 0.2 * np.cos(0.5 * x[i])
            b1 = 0.8 + 0.25 * np.sin(0.6 * x[i])
            b2 = 1.1 + 0.3 * np.cos(0.4 * x[i])
            # Enhanced spectral filtering
            spectral_filter = 1.1 + 0.3 * np.sin(0.5 * x[i]**2) + 0.15 * np.cos(0.3 * x[i])
            multi_saddle += ((x[i]**2 - a1) * (x[i]**2 - a2) * 
                           (x[i]**2 - b1) * (x[i]**2 - b2)) * spectral_filter
        
        # Hyper-chaotic sine-cosine interactions with quantum interference
        hyperchaos_interaction = 0
        for i in range(self.dim):
            mod_freq1 = 1.5 + 0.4 * np.sin(0.5 * x[i]) + 0.2 * np.cos(0.6 * x[i])
            mod_freq2 = 0.9 + 0.3 * np.cos(0.4 * x[i]) + 0.15 * np.sin(0.7 * x[i])
            mod_amp1 = 0.9 + 0.2 * np.cos(0.5 * x[i])
            mod_amp2 = 0.8 + 0.15 * np.sin(0.4 * x[i])
            # Enhanced quantum interference
            interference = 0.35 * np.sin(0.9 * x[i]) * np.cos(0.8 * x[i]) + 0.1 * np.sin(0.7 * x[i]**2)
            hyperchaos_interaction += (mod_amp1 * np.sin(mod_freq1 * x[i]) * 
                                     mod_amp2 * np.cos(mod_freq2 * x[i]) + interference)
        
        # Enhanced global conditioning with multi-scale fractal modulation
        condition_factor = 1.1 + 0.3 * np.sin(0.6 * self.dim) + 0.15 * np.cos(0.4 * self.dim) + 0.08 * np.sin(0.8 * self.dim)
        
        # Additional complexity through mixed conditioning and basin structures
        mixed_conditioning = 1.1 + 0.15 * np.sin(0.3 * np.sum(x**2)) + 0.08 * np.cos(0.4 * np.sum(np.abs(x)))
        
        # New hyper-chaotic gradient modulation with quantum tunneling effects
        quantum_tunneling = 0
        for i in range(self.dim):
            # Quantum tunneling modulations
            mod1 = 0.6 * np.sin(0.4 * x[i] + 0.25 * np.sin(0.8 * x[i]))
            mod2 = 0.35 * np.cos(0.5 * x[i] + 0.15 * np.cos(0.7 * x[i]))
            mod3 = 0.25 * np.sin(0.6 * x[i] + 0.2 * np.sin(0.9 * x[i]))
            mod4 = 0.15 * np.cos(0.3 * x[i] + 0.1 * np.cos(0.8 * x[i]))
            quantum_tunneling += (mod1 + mod2 + mod3 + mod4) * np.exp(-0.1 * x[i]**2)
        
        # Combine all components with optimized weights and enhanced complexity
        return condition_factor * mixed_conditioning * (0.25 * nested_oscillator + 0.25 * quantum_coupling + 
                                  0.2 * fractal_basin + 0.18 * multi_saddle + 0.12 * hyperchaos_interaction + 0.03 * quantum_tunneling)