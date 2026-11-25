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
            freq = 2.0 + 1.5 * np.sin(0.7 * i + np.sin(0.3 * i))
            amp = 1.0 + 0.5 * np.cos(0.4 * i + np.cos(0.2 * i))
            oscillation_term += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Adaptive conditioning with dynamic scaling factors
        condition_term = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.8 * np.sin(0.5 * x[i] + np.sin(0.2 * x[i]))
            condition_term += scale_factor * x[i]**4
        
        # Cross-dimensional coupling with chaotic interaction terms
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                dist = np.abs(x[i] - x[j])
                coupling_factor = 1.0 + 0.3 * np.sin(2.0 * (x[i] + x[j]))
                coupling_term += coupling_factor * np.exp(-0.2 * dist) * np.sin(3.0 * (x[i] - x[j]))
        
        # Chaotic gradient modulation with multi-scale harmonic components
        gradient_term = 0.0
        for i in range(self.dim):
            grad_component = 0.0
            for k in range(1, 6):
                freq_k = k * (1.0 + 0.2 * np.sin(0.3 * i + np.sin(0.1 * i)))
                amp_k = 1.0 + 0.5 * np.cos(0.2 * k + np.cos(0.1 * k))
                grad_component += amp_k * np.sin(freq_k * x[i])
            gradient_term += grad_component**3
        
        # Fractal-like basin structure with time-varying depth
        basin_term = 0.0
        for i in range(self.dim):
            basin_depth = 2.0 + 1.0 * np.sin(0.6 * i + np.sin(0.2 * i))
            basin_term += basin_depth * (np.abs(x[i]) - 2.0)**2 * np.exp(-0.1 * x[i]**2)
        
        # Mixed polynomial and trigonometric components with chaotic mixing
        mixed_term = 0.0
        for i in range(self.dim):
            mixed_term += (x[i]**5 + 0.5 * x[i]**3) * np.sin(4.0 * x[i]) * np.cos(2.0 * x[i])
        
        # Time-varying penalty with chaotic oscillation
        penalty_term = 0.0
        for i in range(self.dim):
            penalty_factor = 1.0 + 0.4 * np.sin(0.8 * x[i] + np.sin(0.4 * x[i]))
            penalty_term += penalty_factor * (x[i]**2 - 25.0)**2
        
        # Combine all terms with optimized weights
        result = 0.2 * oscillation_term + 0.25 * condition_term + 0.15 * coupling_term + 0.1 * gradient_term + 0.1 * basin_term + 0.1 * mixed_term + 0.05 * penalty_term
        
        return result