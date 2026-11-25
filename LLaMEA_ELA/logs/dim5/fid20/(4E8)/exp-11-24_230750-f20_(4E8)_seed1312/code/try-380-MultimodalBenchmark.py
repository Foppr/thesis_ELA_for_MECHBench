import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Hyperchaotic sine-wave modulations with memory effects
        chaotic_modulation = 0.0
        for i in range(self.dim):
            freq = 5.0 + 4.0 * np.sin(0.7 * x[i] + 0.5) * np.cos(0.9 * x[i]**2)
            amp = 2.5 + 2.0 * np.sin(0.8 * x[i] + 0.6)
            phase = 0.5 * np.sin(2.0 * x[i] + 0.3) * np.cos(1.2 * x[i]**2)
            # Memory effect: previous values influence current
            if i > 0:
                memory_factor = 0.7 + 0.3 * np.sin(x[i-1])
                chaotic_modulation += amp * np.sin(freq * x[i] + phase) * np.exp(-0.2 * x[i]**2) * memory_factor
            else:
                chaotic_modulation += amp * np.sin(freq * x[i] + phase) * np.exp(-0.2 * x[i]**2)
        
        # Dynamic Gaussian peak structures with temporal dependencies
        gaussian_peaks = 0.0
        for i in range(self.dim):
            center = -4.5 + 9.0 * np.sin(0.6 * x[i] + 0.4) / (1.0 + np.abs(x[i]))
            variance = 1.2 + 0.9 * np.cos(0.7 * x[i])
            height = 2.5 + 0.8 * np.sin(1.0 * x[i] + 0.5)
            # Temporal dependency: peak height changes based on position
            temporal_factor = 1.0 + 0.4 * np.sin(0.5 * x[i]**2)
            gaussian_peaks += height * temporal_factor * np.exp(-0.5 * ((x[i] - center) / variance)**2)
        
        # Cross-dimensional cubic polynomial couplings with memory
        polynomial_coupling = 0.0
        for i in range(self.dim):
            exp_factor = 1.3 + 0.5 * np.sin(0.8 * x[i] + 0.7)
            poly_term = 0.0
            for j in range(i+1, min(i+5, self.dim)):
                weight = 0.7 + 0.3 * np.cos(0.6 * (x[i] - x[j]))
                # Memory effect on coupling weights
                if i > 0 and j > 0:
                    memory_weight = 0.9 + 0.1 * np.sin(x[i-1] + x[j-1])
                    poly_term += weight * memory_weight * (x[i]**3 + x[j]**3)
                else:
                    poly_term += weight * (x[i]**3 + x[j]**3)
            polynomial_coupling += poly_term
        
        # Adaptive conditioning with temporal stiffness
        conditioning = 0.0
        for i in range(self.dim):
            stiffness = 2.0 + 1.5 * np.sin(0.9 * x[i] + 0.5) * np.cos(0.7 * x[i]**2)
            # Temporal stiffness variation
            temporal_stiffness = 1.0 + 0.3 * np.sin(0.6 * x[i]**3)
            conditioning += 0.7 * stiffness * temporal_stiffness * x[i]**4
        
        # Saddle-point interactions with complex phase couplings and memory
        saddle_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                phase_coupling = np.sin(0.7 * (x[i] + x[j]) + 0.4) * np.cos(0.5 * (x[i] - x[j]))
                # Memory effect on phase coupling
                if i > 0 and j > 0:
                    memory_phase = 0.95 + 0.05 * np.sin(x[i-1] - x[j-1])
                    saddle_interaction += phase_coupling * memory_phase * (x[i]**3 + x[j]**3)
                else:
                    saddle_interaction += phase_coupling * (x[i]**3 + x[j]**3)
        
        # Multi-scale harmonic potential with exponential modulation and memory
        harmonic_potential = 0.0
        for i in range(self.dim):
            scale = 4.0 + np.sin(1.0 * x[i] + 0.6) * np.cos(0.8 * x[i]**2)
            # Memory effect on scale
            if i > 0:
                memory_scale = 1.3 + 0.3 * np.sin(x[i-1])
                harmonic_potential += scale * memory_scale * np.sin(5.0 * x[i]) * np.exp(-0.3 * np.abs(x[i]))
            else:
                harmonic_potential += scale * np.sin(5.0 * x[i]) * np.exp(-0.3 * np.abs(x[i]))
        
        # Dimensionally adaptive normalization with memory
        norm_factor = 2.5 + 0.6 * np.log(self.dim + 1) * np.exp(-0.06 * self.dim)
        # Memory effect on normalization factor
        if self.dim > 1:
            memory_norm = 1.2 + 0.2 * np.sin(x[0] + x[-1])
            norm_factor *= memory_norm
        
        return (0.35 * chaotic_modulation + 0.3 * gaussian_peaks + 
                0.25 * polynomial_coupling + 0.2 * conditioning + 
                0.15 * saddle_interaction + 0.08 * harmonic_potential) * norm_factor