import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Time-varying harmonic oscillations with chaotic modulation
        oscillation_term = 0.0
        for i in range(self.dim):
            freq = 2.5 + 1.2 * np.sin(0.8 * i + np.sin(0.35 * i))
            amp = 1.2 + 0.4 * np.cos(0.45 * i + np.cos(0.25 * i))
            oscillation_term += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Adaptive conditioning with dynamic scaling factors
        condition_term = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.9 * np.sin(0.55 * x[i] + np.sin(0.25 * x[i]))
            condition_term += scale_factor * x[i]**4
        
        # Cross-dimensional coupling with chaotic interaction terms (modified strength)
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                dist = np.abs(x[i] - x[j])
                coupling_factor = 1.0 + 0.4 * np.sin(2.5 * (x[i] + x[j]))
                coupling_term += coupling_factor * np.exp(-0.25 * dist) * np.sin(3.5 * (x[i] - x[j]))
        
        # Chaotic gradient modulation with multi-scale harmonic components
        gradient_term = 0.0
        for i in range(self.dim):
            grad_component = 0.0
            for k in range(1, 7):
                freq_k = k * (1.2 + 0.15 * np.sin(0.35 * i + np.sin(0.12 * i)))
                amp_k = 1.1 + 0.4 * np.cos(0.22 * k + np.cos(0.12 * k))
                grad_component += amp_k * np.sin(freq_k * x[i])
            gradient_term += grad_component**3
        
        # Fractal-like basin structure with time-varying depth
        basin_term = 0.0
        for i in range(self.dim):
            basin_depth = 2.5 + 0.8 * np.sin(0.65 * i + np.sin(0.22 * i))
            basin_term += basin_depth * (np.abs(x[i]) - 2.0)**2 * np.exp(-0.12 * x[i]**2)
        
        # Mixed polynomial and trigonometric components with chaotic mixing
        mixed_term = 0.0
        for i in range(self.dim):
            mixed_term += (x[i]**5 + 0.6 * x[i]**3) * np.sin(4.2 * x[i]) * np.cos(2.2 * x[i])
        
        # Time-varying penalty with chaotic oscillation (modified amplitude)
        penalty_term = 0.0
        for i in range(self.dim):
            penalty_factor = 1.0 + 0.35 * np.sin(0.85 * x[i] + np.sin(0.42 * x[i]))
            penalty_term += penalty_factor * (x[i]**2 - 25.0)**2
        
        # Combine all terms with optimized weights
        result = 0.18 * oscillation_term + 0.27 * condition_term + 0.13 * coupling_term + 0.11 * gradient_term + 0.09 * basin_term + 0.11 * mixed_term + 0.06 * penalty_term
        
        return result