import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-wave interactions with dynamic frequency modulation
        chaotic = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.3 * np.sin(0.2 * (i + 1) * np.sum(x))
            chaotic += np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i] * 0.7) * np.exp(-0.08 * x[i]**2)
        
        # Adaptive elliptic valleys with time-varying conditioning
        elliptic = 0.0
        for i in range(self.dim):
            condition = 1.0 + 0.5 * np.sin(0.3 * (i + 1) * np.sum(x))
            elliptic += condition * (x[i]**2 + 0.1 * np.sin(3 * x[i])**2)
        
        # Multi-scale Gaussian mixtures with asymmetric variance
        gaussian = 0.0
        scales = [0.5, 1.0, 2.0]
        for scale in scales:
            for i in range(self.dim):
                mean_shift = 0.3 * np.sin(0.4 * (i + 1) * np.sum(x))
                variance = 0.2 + 0.3 * np.cos(scale * x[i])
                asymmetry = 0.1 * np.sin(0.6 * x[i])
                gaussian += (1.0 + asymmetry) * np.exp(-0.5 * ((x[i] - scale + mean_shift)**2 / variance))
        
        # Asymmetric boundary penalties with directional weighting
        boundary = 0.0
        for i in range(self.dim):
            dist_from_boundary = min(5.0 - np.abs(x[i]), 2.0)
            direction_weight = 1.0 + 0.4 * np.cos(0.3 * x[i])
            penalty = 15.0 * np.exp(-dist_from_boundary) * direction_weight
            boundary += penalty
        
        # Cross-dimensional coupling with dynamic strength
        coupling = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                coupling_strength = 0.4 + 0.3 * np.cos(0.25 * (i + 1) * np.sum(x))
                coupling += coupling_strength * np.sin(0.3 * x[i]) * np.cos(0.3 * x[i+1])
        
        # Time-varying phase interference with quantum-like behavior
        phase = 0.0
        for i in range(self.dim):
            time_phase = 0.2 * (i + 1) * np.sum(x)
            phase += np.sin(x[i] + time_phase) * np.cos(x[i] - time_phase) * np.exp(-0.1 * x[i]**2)
        
        # Adaptive weighting scheme based on position and dimensionality
        total_weight = 0.4 + 0.3 * np.sin(0.15 * np.sum(x))
        chaotic_weight = 0.25 * (1.0 + 0.2 * np.cos(0.2 * np.sum(x)))
        elliptic_weight = 0.2 * (1.0 + 0.2 * np.sin(0.2 * np.sum(x)))
        gaussian_weight = 0.25 * (1.0 + 0.2 * np.cos(0.3 * np.sum(x)))
        boundary_weight = 0.15 * (1.0 + 0.2 * np.sin(0.3 * np.sum(x)))
        coupling_weight = 0.08 * (1.0 + 0.2 * np.cos(0.4 * np.sum(x)))
        phase_weight = 0.07 * (1.0 + 0.2 * np.sin(0.4 * np.sum(x)))
        
        return (chaotic_weight * chaotic + 
                elliptic_weight * elliptic + 
                gaussian_weight * gaussian + 
                boundary_weight * boundary + 
                coupling_weight * coupling + 
                phase_weight * phase)