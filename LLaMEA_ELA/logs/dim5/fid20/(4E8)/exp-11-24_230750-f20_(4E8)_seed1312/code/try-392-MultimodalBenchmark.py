import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced hyperchaotic sine-wave modulations with improved memory effects
        chaotic_modulation = 0.0
        for i in range(self.dim):
            freq = 6.0 + 3.0 * np.sin(0.8 * x[i] + 0.4) * np.cos(1.1 * x[i]**2)
            amp = 3.0 + 1.5 * np.sin(0.9 * x[i] + 0.7)
            phase = 0.6 * np.sin(2.2 * x[i] + 0.4) * np.cos(1.3 * x[i]**2)
            # Enhanced memory effect: cumulative influence of previous values
            memory_factor = 0.8 + 0.2 * np.sin(x[i-1] if i > 0 else 0.0)
            chaotic_modulation += amp * np.sin(freq * x[i] + phase) * np.exp(-0.15 * x[i]**2) * memory_factor
        
        # Dynamic Gaussian peak structures with enhanced temporal dependencies
        gaussian_peaks = 0.0
        for i in range(self.dim):
            center = -4.0 + 8.0 * np.sin(0.7 * x[i] + 0.5) / (1.0 + np.abs(x[i]))
            variance = 1.5 + 0.8 * np.cos(0.8 * x[i])
            height = 3.0 + 0.6 * np.sin(1.2 * x[i] + 0.6)
            # Enhanced temporal dependency
            temporal_factor = 1.0 + 0.5 * np.sin(0.4 * x[i]**2)
            gaussian_peaks += height * temporal_factor * np.exp(-0.5 * ((x[i] - center) / variance)**2)
        
        # Cross-dimensional cubic polynomial couplings with enhanced memory
        polynomial_coupling = 0.0
        for i in range(self.dim):
            exp_factor = 1.5 + 0.4 * np.sin(0.9 * x[i] + 0.8)
            poly_term = 0.0
            for j in range(i+1, min(i+6, self.dim)):
                weight = 0.8 + 0.2 * np.cos(0.7 * (x[i] - x[j]))
                # Enhanced memory effect on coupling weights
                memory_weight = 0.95 + 0.05 * np.sin(x[i-1] + x[j-1] if i > 0 and j > 0 else 0.0)
                poly_term += weight * memory_weight * (x[i]**3 + x[j]**3)
            polynomial_coupling += poly_term
        
        # Enhanced adaptive conditioning with temporal stiffness
        conditioning = 0.0
        for i in range(self.dim):
            stiffness = 2.5 + 1.2 * np.sin(1.0 * x[i] + 0.6) * np.cos(0.8 * x[i]**2)
            # Enhanced temporal stiffness variation
            temporal_stiffness = 1.0 + 0.4 * np.sin(0.7 * x[i]**3)
            conditioning += 0.8 * stiffness * temporal_stiffness * x[i]**4
        
        # Saddle-point interactions with enhanced phase couplings and memory
        saddle_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):
                phase_coupling = np.sin(0.8 * (x[i] + x[j]) + 0.5) * np.cos(0.6 * (x[i] - x[j]))
                # Enhanced memory effect on phase coupling
                memory_phase = 0.9 + 0.1 * np.sin(x[i-1] - x[j-1] if i > 0 and j > 0 else 0.0)
                saddle_interaction += phase_coupling * memory_phase * (x[i]**3 + x[j]**3)
        
        # Enhanced multi-scale harmonic potential with exponential modulation and memory
        harmonic_potential = 0.0
        for i in range(self.dim):
            scale = 4.5 + np.sin(1.2 * x[i] + 0.7) * np.cos(0.9 * x[i]**2)
            # Enhanced memory effect on scale
            memory_scale = 1.4 + 0.2 * np.sin(x[i-1] if i > 0 else 0.0)
            harmonic_potential += scale * memory_scale * np.sin(6.0 * x[i]) * np.exp(-0.25 * np.abs(x[i]))
        
        # Enhanced dimensionally adaptive normalization with memory
        norm_factor = 3.0 + 0.5 * np.log(self.dim + 1) * np.exp(-0.05 * self.dim)
        # Enhanced memory effect on normalization factor
        if self.dim > 1:
            memory_norm = 1.25 + 0.15 * np.sin(x[0] + x[-1])
            norm_factor *= memory_norm
        
        return (0.32 * chaotic_modulation + 0.28 * gaussian_peaks + 
                0.22 * polynomial_coupling + 0.18 * conditioning + 
                0.12 * saddle_interaction + 0.08 * harmonic_potential) * norm_factor