import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Hyperchaotic sine-wave modulations with modified frequencies
        chaotic_modulation = 0.0
        for i in range(self.dim):
            freq = 4.0 + 1.5 * np.sin(0.6 * x[i] + 0.3) * np.cos(0.8 * x[i]**2)
            amp = 1.2 + 1.2 * np.sin(0.7 * x[i] + 0.4)
            phase = 0.4 * np.sin(1.2 * x[i] + 0.1) * np.cos(0.8 * x[i]**2)
            # Memory effect: previous values influence current
            if i > 0:
                memory_factor = 0.6 + 0.4 * np.sin(x[i-1])
                chaotic_modulation += amp * np.sin(freq * x[i] + phase) * np.exp(-0.15 * x[i]**2) * memory_factor
            else:
                chaotic_modulation += amp * np.sin(freq * x[i] + phase) * np.exp(-0.15 * x[i]**2)
        
        # Dynamic Gaussian peak structures with modified variance and center
        gaussian_peaks = 0.0
        for i in range(self.dim):
            center = -2.5 + 5.0 * np.sin(0.3 * x[i] + 0.2) / (1.0 + np.abs(x[i]))
            variance = 1.0 + 0.4 * np.cos(0.6 * x[i])
            height = 1.8 + 0.3 * np.sin(0.9 * x[i] + 0.3)
            # Temporal dependency: peak height changes based on position
            temporal_factor = 1.0 + 0.15 * np.sin(0.2 * x[i]**2)
            gaussian_peaks += height * temporal_factor * np.exp(-0.5 * ((x[i] - center) / variance)**2)
        
        # Cross-dimensional cubic polynomial couplings with modified weights
        polynomial_coupling = 0.0
        for i in range(self.dim):
            exp_factor = 1.2 + 0.2 * np.sin(0.7 * x[i] + 0.5)
            poly_term = 0.0
            for j in range(i+1, min(i+4, self.dim)):
                weight = 0.3 + 0.7 * np.cos(0.3 * (x[i] - x[j]))
                # Memory effect on coupling weights
                if i > 0 and j > 0:
                    memory_weight = 0.8 + 0.2 * np.sin(x[i-1] + x[j-1])
                    poly_term += weight * memory_weight * (x[i]**3 + x[j]**3)
                else:
                    poly_term += weight * (x[i]**3 + x[j]**3)
            polynomial_coupling += poly_term
        
        # Adaptive conditioning with modified stiffness
        conditioning = 0.0
        for i in range(self.dim):
            stiffness = 1.2 + 0.6 * np.sin(0.8 * x[i] + 0.3) * np.cos(0.4 * x[i]**2)
            # Temporal stiffness variation
            temporal_stiffness = 1.0 + 0.15 * np.sin(0.3 * x[i]**3)
            conditioning += 0.6 * stiffness * temporal_stiffness * x[i]**4
        
        # Saddle-point interactions with modified phase couplings
        saddle_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                phase_coupling = np.sin(0.6 * (x[i] + x[j]) + 0.2) * np.cos(0.4 * (x[i] - x[j]))
                # Memory effect on phase coupling
                if i > 0 and j > 0:
                    memory_phase = 0.9 + 0.1 * np.sin(x[i-1] - x[j-1])
                    saddle_interaction += phase_coupling * memory_phase * (x[i]**3 + x[j]**3)
                else:
                    saddle_interaction += phase_coupling * (x[i]**3 + x[j]**3)
        
        # Multi-scale harmonic potential with modified scale and exponential modulation
        harmonic_potential = 0.0
        for i in range(self.dim):
            scale = 2.5 + np.sin(0.9 * x[i] + 0.4) * np.cos(0.7 * x[i]**2)
            # Memory effect on scale
            if i > 0:
                memory_scale = 1.1 + 0.2 * np.sin(x[i-1])
                harmonic_potential += scale * memory_scale * np.sin(3.5 * x[i]) * np.exp(-0.25 * np.abs(x[i]))
            else:
                harmonic_potential += scale * np.sin(3.5 * x[i]) * np.exp(-0.25 * np.abs(x[i]))
        
        # Dimensionally adaptive normalization with modified memory effect
        norm_factor = 1.6 + 0.3 * np.log(self.dim + 1) * np.exp(-0.04 * self.dim)
        # Memory effect on normalization factor
        if self.dim > 1:
            memory_norm = 1.0 + 0.15 * np.sin(x[0] + x[-1])
            norm_factor *= memory_norm
        
        return (0.22 * chaotic_modulation + 0.25 * gaussian_peaks + 
                0.18 * polynomial_coupling + 0.16 * conditioning + 
                0.13 * saddle_interaction + 0.06 * harmonic_potential) * norm_factor